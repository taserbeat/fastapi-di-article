from abc import ABC, abstractmethod
from injector import inject

from services.counter_service import ICounterService


class IFugaService(ABC):
    @abstractmethod
    def do_something(self) -> str:
        pass

    @abstractmethod
    def get_inner_count(self) -> int:
        pass


class FugaService(IFugaService):
    @inject
    def __init__(self, counter_service: ICounterService):
        self._counter_service = counter_service
        return

    def do_something(self) -> str:
        self._counter_service.increment()
        return "FugaService did something!"

    def get_inner_count(self) -> int:
        return self._counter_service.get_count()
