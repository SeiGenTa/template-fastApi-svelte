from fastapi import APIRouter, Depends, HTTPException
from .modelsApi.userApi import LoginUser, RegisterUser, UserUpdate

userApi = APIRouter()

@userApi.post("/register")
async def register_user(data: RegisterUser):
    return {"message": "User registered successfully"}

@userApi.post("/login")
async def login_user(data: LoginUser):
    return {"message": "User logged in successfully"}

@userApi.get("/")
async def get_user():
    return {"message": "User details retrieved successfully"}

@userApi.put("/")
async def update_user(data: UserUpdate):
    return {"message": "User details updated successfully"}

@userApi.post("/revalidateJWT")
async def revalidate_jwt():
    return {"message": "JWT revalidated successfully"}