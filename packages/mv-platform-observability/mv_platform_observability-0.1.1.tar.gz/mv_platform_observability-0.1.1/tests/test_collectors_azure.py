import time
from unittest.mock import patch, AsyncMock

import pytest
from mv_platform_observability.collectors.metrics import EventHubsMetricCollector


class TestEventHubsMetricCollector:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Patch the EventHubProducerClient at the correct import path
        self.mock_producer_patcher = patch('mv_platform_observability.collectors.metrics.EventHubProducerClient', autospec=True)
        self.mock_producer_class = self.mock_producer_patcher.start()
        self.mock_producer = AsyncMock()
        self.mock_producer_class.from_connection_string.return_value = self.mock_producer
        self.mock_batch = AsyncMock()
        self.mock_producer.create_batch.return_value = self.mock_batch

        yield

        self.mock_producer_patcher.stop()

    @pytest.mark.asyncio
    async def test_send_metric(self):
        collector = EventHubsMetricCollector("connection", "event_hub")

        # Mock the _process_metrics method
        collector._process_metrics = AsyncMock()

        metric_data = {"name": "test", "value": 1}
        await collector.send_metric(metric_data)

        # Assert that the metric was added to the queue
        assert collector._metrics_queue.qsize() == 1
        queued_metric = await collector._metrics_queue.get()
        assert queued_metric == metric_data

        # Assert that _process_metrics was called
        collector._process_metrics.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_metrics_flush_interval(self):
        collector = EventHubsMetricCollector("connection", "event_hub", flush_interval=1, batch_size=100)
        collector._send_batch = AsyncMock()

        # Set last flush time to simulate flush interval
        collector._last_flush_time = time.time() - 2

        # Add a metric to the queue
        await collector._metrics_queue.put({"name": "test", "value": 1})

        # Call _process_metrics
        await collector._process_metrics()

        # Assert that _send_batch was called
        collector._send_batch.assert_called_once()

        # Assert the queue is empty
        assert collector._metrics_queue.qsize() == 0

    @pytest.mark.asyncio
    async def test_process_metrics_batch_size(self):
        collector = EventHubsMetricCollector("connection", "event_hub", flush_interval=60, batch_size=2)
        collector._send_batch = AsyncMock()

        # Add metrics to the queue
        await collector._metrics_queue.put({"name": "test1", "value": 1})
        await collector._metrics_queue.put({"name": "test2", "value": 2})

        # Call _process_metrics
        await collector._process_metrics()

        # Assert that _send_batch was called
        collector._send_batch.assert_called_once()

        # Assert the queue is empty
        assert collector._metrics_queue.qsize() == 0

    @pytest.mark.asyncio
    async def test_send_batch(self):
        collector = EventHubsMetricCollector("connection", "event_hub")
        batch = [{"name": "test1", "value": 1}, {"name": "test2", "value": 2}]

        await collector._send_batch(batch)

        # Assert that create_batch was called
        self.mock_producer.create_batch.assert_called_once()

        # Assert that add was called on the batch for each metric
        assert self.mock_batch.add.call_count == 2

        # Assert that send_batch was called with the mock batch
        self.mock_producer.send_batch.assert_called_once_with(self.mock_batch)
