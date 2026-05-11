import numpy as np
from collections import deque

class AnomalyDetector:
    def __init__(self, window_size=30, z_threshold=2.5):
        self.window_size = window_size
        self.z_threshold = z_threshold
        self.history = deque(maxlen=window_size)

    def update(self, value: float):
        self.history.append(value)

    def is_anomaly(self, value: float) -> bool:
        if len(self.history) < 10:
            return False

        arr = np.array(self.history)
        mean = np.mean(arr)
        std = np.std(arr) + 1e-6

        z_score = abs((value - mean) / std)

        return z_score > self.z_threshold