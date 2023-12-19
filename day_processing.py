import time
from abc import ABC, abstractmethod
from colorama import Fore


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
        print(f"{Fore.RED}{self._name()}{Fore.RESET}")
        s = time.perf_counter()
        self._process()
        e = time.perf_counter()
        print(f"Took {Fore.LIGHTGREEN_EX}{e - s:0.3f}{Fore.RESET} seconds")
        print(f"{Fore.LIGHTBLACK_EX}-------------------------------{Fore.RESET}")
