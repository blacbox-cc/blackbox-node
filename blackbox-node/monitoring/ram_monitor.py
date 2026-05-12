import psutil
import asyncio
from core.state import state
from telemetry.logging import logger

class RAMMonitor:
    async def start(self):
        logger.info("[MONITORING] RAM monitor started")
        while True:
            state.ram_percent = psutil.virtual_memory().percent
            await asyncio.sleep(2)