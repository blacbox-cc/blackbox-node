import time
import random

class Scheduler:
    def __init__(self, base_delay=1.0, jitter=0.5):
        self.base_delay = base_delay
        self.jitter = jitter

    def sleep(self):
        delay = self.base_delay + random.uniform(0, self.jitter)
        time.sleep(delay)

    def adaptive_sleep(self, load_factor: float = 1.0):
        delay = self.base_delay * load_factor
        delay += random.uniform(0, self.jitter)
        time.sleep(max(0.1, delay))