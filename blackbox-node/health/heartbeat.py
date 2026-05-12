import asyncio
from telemetry.logging import logger

class Heartbeat:
    def __init__(self, interval: int = 5):
        self.interval = interval

    async def start(self):
        logger.info("[HEALTH] Heartbeat loop started")
        while True:
            # Por ahora solo loguea, luego será registro en el cluster
            logger.info("status: alive")
            await asyncio.sleep(self.interval)