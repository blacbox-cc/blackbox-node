from dataclasses import dataclass


@dataclass
class StateSnapshot:
    cpu: float
    ram: float
    processes: int
    load: float
    timestamp: float


class SnapshotFactory:

    @staticmethod
    def from_dict(data: dict) -> StateSnapshot:
        return StateSnapshot(
            cpu=data.get("cpu_percent", 0),
            ram=data.get("memory_percent", 0),
            processes=data.get("process_count", 0),
            load=(data.get("cpu_percent", 0) + data.get("memory_percent", 0)) / 100.0,
            timestamp=data.get("timestamp", 0)
        )