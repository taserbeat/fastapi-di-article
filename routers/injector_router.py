from fastapi import APIRouter

injector_router = APIRouter(prefix="/api/injector", tags=["Injector"])


@injector_router.get("")
def get_something():
    return {
        "message": "This is injector endpoint"
    }
