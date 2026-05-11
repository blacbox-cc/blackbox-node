import time


class SafetyGuard:
    """
    Kill-switch y reglas de protección del sistema.
    """

    def __init__(self):
        self.disabled = False
        self.last_trigger = None

    def check_system(self, cpu: float, ram: float):
        if cpu > 95 or ram > 95:
            self.trigger_shutdown("CRITICAL_LOAD")

    def trigger_shutdown(self, reason: str):
        self.disabled = True
        self.last_trigger = {
            "reason": reason,
            "timestamp": time.time()
        }
        print(f"[SAFETY] SYSTEM DISABLED: {reason}")

    def allow_action(self, action: str, cpu: float):
        if self.disabled:
            return False

        if action == "SPAWN_DUMMY" and cpu > 70:
            return False

        return True


safety_guard = SafetyGuard()