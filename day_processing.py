import time
from abc import ABC, abstractmethod


class Day(ABC):
    def __init__(self, in_path: str) -> None:
        with open(in_path, 'r') as f:
            self.lines = f.readlines()
    
    @abstractmethod
    def _process(self):
        pass

    def run(self):
        print(type(self).__name__ + ":")
        s = time.perf_counter()
        self._process()
        e = time.perf_counter()
        print(f"Took {e - s:0.4f} seconds")
        print("-------------------------------")
