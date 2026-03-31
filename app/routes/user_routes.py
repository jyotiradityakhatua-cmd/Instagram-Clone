from fastapi import APIRouter, Depends
from app.dependencies.auth_dependencies import get_current_user
from app.database.collections import user_collection

router = APIRouter()

@router.get("/profile")
def profile(current_user: str = Depends(get_current_user)):
    user = users_collection.find_one({"username": current_user})

    return {
        "username": user["username"],
        "followers_count": user["followers_count"],
        "following_count": user["following_count"],
        "followers": user["followers"],
        "following": user["following"]
    }