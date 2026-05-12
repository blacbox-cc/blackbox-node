from fastapi import APIRouter
from core.state import state

router = APIRouter()

@router.get("/metrics")
async def get_metrics():
    return {
        "node_id": "blackbox-01", # O traer de settings
        "status": state.status,
        "stats": {
            "cpu": state.cpu_percent,
            "ram": state.ram_percent
        }
    }