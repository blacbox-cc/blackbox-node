from fastapi import FastAPI
from core.state import state

app = FastAPI(title="Blackbox Node API")

@app.get("/health")
async def health():
    return {"status": state.status}

@app.get("/metrics")
async def metrics():
    return {
        "cpu": state.cpu_percent,
        "ram": state.ram_percent,
        "status": state.status
    }