from collections import deque
import random


class ReplayBuffer:
    """
    Memoria de experiencias para entrenamiento offline.
    """

    def __init__(self, max_size=5000):
        self.buffer = deque(maxlen=max_size)

    def add(self, state, action, reward, next_state):
        self.buffer.append((state, action, reward, next_state))

    def sample(self, batch_size=32):
        return random.sample(self.buffer, min(batch_size, len(self.buffer)))

    def size(self):
        return len(self.buffer)

    def clear(self):
        self.buffer.clear()


replay_buffer = ReplayBuffer()