from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.api.user import userApi

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


app.include_router(userApi, prefix="/api/v1/user", tags=["user"])

@app.get("/")
async def read_root():
    return FileResponse("dist/index.html")

app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")