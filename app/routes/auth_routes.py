from fastapi import APIRouter, HTTPException
from app.services.auth_servuce import create_user
from app.services.auth_servuce import login_user

from database.connection import db

router = APIRouter()

@router.post("/register")
def register(username: str, email: str, password: str):
    user= create_user(username, email, password)

    if not user:
        raise HTTPException(status_code=400, detail="Username already exists")

    return {"message": "User registered successfully"}

@router.post("/login")
def login(username: str, password: str):
    token = login_user(username, password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"access_token": token}