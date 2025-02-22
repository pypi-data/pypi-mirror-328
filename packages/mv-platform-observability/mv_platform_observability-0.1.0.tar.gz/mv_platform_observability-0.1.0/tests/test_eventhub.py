import asyncio
import os
import pytest_asyncio
import pytest
from mv_platform_observability.collectors.metrics import EventHubsMetricCollector
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.tst")


class TestEventHub:

    @pytest_asyncio.fixture(scope="session")
    async def fix_collector(self):
        connection_string = os.getenv("12K-metrics-events")
        collector = EventHubsMetricCollector(
            connection_string=connection_string,
            event_hub_name="metrics-events",
            batch_size=1,
            flush_interval=0.1
        )
        yield collector
        await collector.close()  # Ensure the collector is closed after tests

    @pytest.mark.asyncio
    async def test_send_message(self, fix_collector):
        metric_data = {"name": "test", "value": 4}

        # Send the metric
        await fix_collector.send_metric(metric_data)

        # Wait for processing
        await asyncio.sleep(3)
        # Verify the metric was sent (queue should be empty)
        assert fix_collector._metrics_queue.qsize() == 0, "Queue should be empty after sending"
