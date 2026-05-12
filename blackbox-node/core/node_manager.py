import asyncio
from core.state import state  # <--- AGREGAR ESTO
from monitoring.cpu_monitor import CPUMonitor
from monitoring.ram_monitor import RAMMonitor 
from health.heartbeat import Heartbeat
from telemetry.logging import logger

class NodeManager:
    def __init__(self):
        self.cpu_monitor = CPUMonitor()
        self.ram_monitor = RAMMonitor() 
        self.heartbeat = Heartbeat()

    async def start_services(self):
        logger.info("[CORE] Starting internal services...")
        
        # Ahora 'state' ya es visible aquí
        state.status = "healthy" 
        
        await asyncio.gather(
            self.cpu_monitor.start(),
            self.ram_monitor.start(),
            self.heartbeat.start()
        )