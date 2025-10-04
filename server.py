import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Sample FastAPI Application",
    docs_url="/swagger",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
