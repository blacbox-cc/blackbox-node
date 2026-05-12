import asyncio
from core.state import state
from telemetry.logging import logger

class NodeLifecycle:
    @staticmethod
    async def shutdown():
        logger.info("[LIFECYCLE] Shutdown initiated...")
        state.status = "offline"
        # Aquí cerraríamos conexiones a DB o sockets en el futuro
        logger.info("[LIFECYCLE] Cleanup complete. Goodbye.")