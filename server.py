import uvicorn
from fastapi import FastAPI

from routers.standard_router import standard_router
from routers.injector_router import injector_router

app = FastAPI(
    title="Sample FastAPI Application",
    docs_url="/swagger",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(standard_router)
app.include_router(injector_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
