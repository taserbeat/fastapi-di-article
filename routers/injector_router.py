from fastapi import APIRouter
from fastapi_injector import Injected

from services.fuga_service import IFugaService
from services.hoge_service import IHogeService

injector_router = APIRouter(prefix="/api/injector", tags=["Injector"])


@injector_router.get("")
def get_something(hoge_service: IHogeService = Injected(IHogeService), fuga_service=Injected(IFugaService)):
    print("=== Startup ===")
    print(f"count via hoge: {hoge_service.get_inner_count()}")
    print(f"count via fuga: {fuga_service.get_inner_count()}")

    hoge_service.do_something()

    print("=== After doing something by Hoge ===")
    print(f"count via hoge: {hoge_service.get_inner_count()}")
    print(f"count via fuga: {fuga_service.get_inner_count()}")

    fuga_service.do_something()

    print("=== After doing something by Fuga ===")
    print(f"count via hoge: {hoge_service.get_inner_count()}")
    print(f"count via fuga: {fuga_service.get_inner_count()}")

    return {
        "message": "This is injector endpoint"
    }
