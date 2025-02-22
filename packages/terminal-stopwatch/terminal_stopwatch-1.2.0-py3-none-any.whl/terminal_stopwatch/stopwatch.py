"""스톱워치 핵심 로직"""

import time
from typing import List

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False
        self.laps: List[float] = []

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.running = True

    def pause(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed = 0
        self.laps = []

    def lap(self):
        if self.running:
            lap_time = time.time() - self.start_time
            self.laps.append(lap_time)

    def get_elapsed(self) -> float:
        return time.time() - self.start_time if self.running else self.elapsed 