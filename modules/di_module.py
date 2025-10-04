from injector import Module, Binder, singleton  # noqa
from fastapi_injector import request_scope  # noqa

from services.counter_service import CounterService, ICounterService
from services.hoge_service import HogeService, IHogeService
from services.fuga_service import FugaService, IFugaService


class AppModule(Module):
    def configure(self, binder: Binder):
        # scope=singletonでシングルトンでインスタンスを生成
        # scope=request_scopeでrequestごとにインスタンスが生成される(同一リクエスト内で同じインスタンス)
        # scopeを指定しない場合は、Transientでインスタンスが生成される(常に新しいインスタンスを生成)
        binder.bind(ICounterService, to=CounterService, scope=singleton)
        binder.bind(IHogeService, to=HogeService)
        binder.bind(IFugaService, to=FugaService)

        return
