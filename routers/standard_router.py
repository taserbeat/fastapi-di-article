from fastapi import APIRouter

standard_router = APIRouter(prefix="/api/standard", tags=["Standard"])


@standard_router.get("")
def get_something():
    return {
        "message": "This is standard endpoint"
    }
