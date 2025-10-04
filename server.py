from fastapi_injector import InjectorMiddleware, attach_injector
from injector import Injector
import uvicorn
from fastapi import FastAPI

from modules.di_module import AppModule
from routers.standard_router import standard_router
from routers.injector_router import injector_router

app = FastAPI(
    title="Sample FastAPI Application",
    docs_url="/swagger",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

injector = Injector([AppModule()])
app.add_middleware(InjectorMiddleware, injector=injector)
attach_injector(app=app, injector=injector)

app.include_router(standard_router)
app.include_router(injector_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
