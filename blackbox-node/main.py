import uvicorn
import asyncio
# Cambiado: eliminamos el prefijo blackbox_node
from core.node_manager import NodeManager 
from telemetry.logging import logger
from configs.settings_loader import settings # Importamos settings

async def start_app():
    manager = NodeManager()
    
    # Leemos la config en lugar de hardcodear
    host = settings.get("api.host", "0.0.0.0")
    port = settings.get("api.port", 8000)
    
    config = uvicorn.Config(
        "api.server:app", 
        host=host, 
        port=port, 
        log_level="info"
    )
    server = uvicorn.Server(config)
    
    logger.info(f"[API] Listening on {host}:{port}")

    await asyncio.gather(
        server.serve(),
        manager.start_services()
    )


def main():
    logger.info("[BOOT] Config loaded")
    try:
        asyncio.run(start_app())
    except KeyboardInterrupt:
        logger.info("[BOOT] Node stopped by user")

if __name__ == "__main__":
    main()