from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.post("/api/v1/user/register")
async def register_user():
    return {"message": "User registered successfully"}

app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

@app.get("/")
async def read_root():
    return FileResponse("dist/index.html")