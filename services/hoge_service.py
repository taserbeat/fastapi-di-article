from abc import ABC, abstractmethod
from injector import inject

from services.counter_service import ICounterService


class IHogeService(ABC):
    @abstractmethod
    def do_something(self) -> str:
        pass

    @abstractmethod
    def get_inner_count(self) -> int:
        pass


class HogeService(IHogeService):
    @inject
    def __init__(self, counter_service: ICounterService):
        self._counter_service = counter_service
        return

    def do_something(self) -> str:
        self._counter_service.increment()
        return "HogeService did something!"

    def get_inner_count(self) -> int:
        return self._counter_service.get_count()
