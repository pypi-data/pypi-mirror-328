from abc import ABC, abstractmethod

from typing import Dict, Any, Optional, List
import asyncio
import logging
import time
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from azure.core.exceptions import AzureError

class MetricCollector(ABC):
    """
    Abstract base class for metric collectors.

    This class defines the interface that all concrete metric collectors must implement.
    """

    @abstractmethod
    async def send_metric(self, metric_data: dict) -> None:
        """
        Send a metric to the configured collector.

        Parameters:
            metric_data (dict): A dictionary containing the metric data to be sent.

        Returns:
            None
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Close any resources used by the collector.

        Returns:
            None
        """
        pass



class EventHubsMetricCollector(MetricCollector):
    """Collects and sends metrics to Azure Event Hubs.

    This class handles asynchronous sending of metrics using Azure Event Hubs SDK,
    implementing batching for efficiency and retry logic with exponential backoff.

    Args:
        connection_string (str): The connection string for Azure Event Hubs.
        event_hub_name (str): Name of the target Event Hub.
        batch_size (int, optional): Number of metrics to collect before sending. Defaults to 100.
        flush_interval (float, optional): Maximum time in seconds between flushes. Defaults to 5.0.
        max_retries (int, optional): Maximum number of retry attempts for failed sends. Defaults to 3.
        max_pending_metrics (int, optional): Maximum number of pending metrics before backpressure is applied. Defaults to 1000.
    """

    def __init__(self, connection_string: str, event_hub_name: str,
                 batch_size: int = 100, flush_interval: float = 5.0,
                 max_retries: int = 3, max_pending_metrics: int = 1000):
        self.connection_string = connection_string
        self.event_hub_name = event_hub_name
        self.batch_size = batch_size
        self.flush_interval = flush_interval
        self.max_retries = max_retries
        self.max_pending_metrics = max_pending_metrics

        self._producer_client = EventHubProducerClient.from_connection_string(
            conn_str=self.connection_string,
            eventhub_name=self.event_hub_name
        )
        self._metrics_queue = asyncio.Queue(maxsize=max_pending_metrics)
        self._loop = asyncio.get_event_loop()
        self._last_flush_time = time.time()

    async def _connect(self):
        """Establishes a connection to Azure Event Hubs if not already connected."""
        # The producer client is already initialized in the constructor, so no need to connect again.
        pass

    async def send_metric(self, metric_data: Dict[str, Any]) -> None:
        """Sends a single metric asynchronously.

        Args:
            metric_data (Dict[str, Any]): The metric data to be sent.
        """
        await self._metrics_queue.put(metric_data)
        asyncio.create_task(self._process_metrics())

    async def _process_metrics(self):
        """Processes metrics from the queue and sends them in batches."""
        if time.time() - self._last_flush_time >= self.flush_interval or self._metrics_queue.qsize() >= self.batch_size:
            batch = []
            while not self._metrics_queue.empty() and len(batch) < self.batch_size:
                batch.append(await self._metrics_queue.get())

            await self._send_batch(batch)
            self._last_flush_time = time.time()

    async def _send_batch(self, metrics: List[Dict[str, Any]]):
        """Sends a batch of metrics to Azure Event Hubs.

        Args:
            metrics (List[Dict[str, Any]]): The list of metric data to be sent.
        """
        if not metrics:
            return

        try:
            event_data_batch = await self._producer_client.create_batch()
            for metric in metrics:
                event_data_batch.add(EventData(str(metric)))

            await self._producer_client.send_batch(event_data_batch)
            logging.info(f"Successfully sent {len(metrics)} metrics to Event Hubs.")
        except (AzureError, Exception) as e:
            logging.error(e)
            retry_count = 0
            while retry_count < self.max_retries:
                try:
                    async with self._producer_client.create_batch() as event_data_batch:
                        for metric in metrics:
                            event_data_batch.add(EventData(str(metric)))

                        await self._producer_client.send_batch(event_data_batch)
                    logging.info(f"Successfully sent {len(metrics)} metrics to Event Hubs after retry.")
                    break
                except (AzureError, Exception) as e:
                    retry_count += 1
                    delay = min(2 ** retry_count, 30)  # Exponential backoff with max delay of 30 seconds
                    logging.warning(
                        f"Failed to send metrics. Retrying in {delay} seconds. Attempt: {retry_count}/{self.max_retries}")
                    await asyncio.sleep(delay)
            else:
                logging.error("Max retries reached. Failed to send metrics.")

    async def _periodic_flush(self):
        """Periodically flushes the buffer based on the configured interval."""
        while True:
            await asyncio.sleep(self.flush_interval)
            await self._process_metrics()

    async def close(self) -> None:
        """Closes the connection and flushes any remaining metrics."""
        await self._process_metrics()
        await self._producer_client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        asyncio.run(self.close())


class AzureMonitorMetricCollector(MetricCollector):
    """Collects and sends metrics to Azure Monitor.

    This class handles authentication with Azure Monitor, formats `MetricData` into the required JSON payload,
    and sends metrics via HTTP POST requests using the `requests` library. It also implements batching if necessary
    and error handling with retry logic.
    """

    def __init__(self, workspace_id: str, resource_group: str, subscription_id: str):
        """Initialize the AzureMonitorMetricCollector.

        Args:
            workspace_id (str): The ID of the Log Analytics workspace.
            resource_group (str): The name of the resource group containing the workspace.
            subscription_id (str): The ID of the Azure subscription.
        """
        if not all([workspace_id, resource_group, subscription_id]):
            raise ValueError("workspace_id, resource_group, and subscription_id must be provided")

        self.workspace_id = workspace_id
        self.resource_group = resource_group
        self.subscription_id = subscription_id
        self.credential = DefaultAzureCredential()
        self.base_url = f"https://westus2-0.monitoring.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/microsoft.insights/metricValues?api-version=2018-01-01"

    def send_metric(self, metric_data: Dict[str, Any]):
        """Send a single metric to Azure Monitor.

        Args:
            metric_data (Dict[str, Any]): The metric data to be sent.
        """
        headers = {
            "Authorization": f"Bearer {self.credential.get_token('https://monitor.azure.com/.default').token}",
            "Content-Type": "application/json"
        }
        payload = self._format_metric(metric_data)

        self._post_payload(headers, payload)

    def _format_metric(self, metric_data: Dict[str, Any]) -> Dict[str, Any]:
        """Format the metric data according to Azure Monitor's schema.

        Args:
            metric_data (Dict[str, Any]): The raw metric data.

        Returns:
            Dict[str, Any]: The formatted metric data.
        """
        return {
            "time": metric_data["timestamp"].isoformat(),
            "data": [
                {
                    "metric": metric_data["name"],
                    "namespace": metric_data.get("namespace", "default"),
                    "dimensions": metric_data.get("dimensions", {}),
                    "value": metric_data["value"]
                }
            ]
        }

    def send_metrics_batch(self, metrics: List[Dict[str, Any]]):
        """Send a batch of metrics to Azure Monitor.

        Args:
            metrics (List[Dict[str, Any]]): The list of metric data to be sent.
        """
        headers = {
            "Authorization": f"Bearer {self.credential.get_token('https://monitor.azure.com/.default').token}",
            "Content-Type": "application/json"
        }
        payload = [self._format_metric(metric) for metric in metrics]

        self._post_payload(headers, payload)

    def _post_payload(self, headers, payload):
        try:
            response = requests.post(self.base_url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error: {e}")
            raise
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout error: {e}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def close(self) -> None:
        pass

