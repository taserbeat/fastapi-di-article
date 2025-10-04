from abc import ABC, abstractmethod


class ICounterService(ABC):
    @abstractmethod
    def increment(self) -> int:
        pass

    @abstractmethod
    def get_count(self) -> int:
        pass


class CounterService(ICounterService):
    def __init__(self):
        self._count = 0
        return

    def increment(self) -> int:
        self._count += 1
        return self._count

    def get_count(self) -> int:
        return self._count
