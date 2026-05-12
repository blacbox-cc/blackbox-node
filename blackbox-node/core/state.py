from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class NodeState:
    cpu_percent: float = 0.0
    ram_percent: float = 0.0
    status: str = "starting"
    active_workloads: list = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

# Instancia global para ser compartida entre hilos/loops
state = NodeState()