from collections import defaultdict
from typing import Callable, Any, Dict, List

class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: Callable):
        self.subscribers[event_type].append(handler)

    def emit(self, event_type: str, data: Any = None):
        if event_type not in self.subscribers:
            return

        for handler in self.subscribers[event_type]:
            try:
                handler(data)
            except Exception as e:
                print(f"[EventBus] Error in {event_type}: {e}")


# Singleton global (simple, sin overengineering aún)
event_bus = EventBus()