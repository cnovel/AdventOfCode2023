import time
from abc import ABC, abstractmethod


class Day(ABC):
    def __init__(self) -> None:
        with open(self._file(), 'r') as f:
            self.lines = f.readlines()
    
    @abstractmethod
    def _process(self):
        pass

    @abstractmethod
    def _name(self):
        pass

    @abstractmethod
    def _file(self):
        pass

    def run(self):
        print(self._name())
        s = time.perf_counter()
        self._process()
        e = time.perf_counter()
        print(f"Took {e - s:0.4f} seconds")
        print("-------------------------------")
