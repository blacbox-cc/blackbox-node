import asyncio
from core.state import state
from telemetry.logging import logger
from configs.settings_loader import settings
from monitoring.collectors.psutil_collector import PsutilCollector

class CPUMonitor:
    def __init__(self):
        self.collector = PsutilCollector()
        self.interval = settings.get("monitoring.cpu_interval", 1.0)

    async def start(self):
        logger.info(f"[MONITORING] CPU monitor started (interval: {self.interval}s)")
        while True:
            state.cpu_percent = self.collector.get_cpu_usage()
            await asyncio.sleep(self.interval)