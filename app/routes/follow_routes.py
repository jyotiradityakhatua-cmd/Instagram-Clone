from fastapi import APIRouter, Depends
from app.dependencies.auth_dependencies import get_current_user
from app.services.follow_service import follow_user

router = APIRouter()

@router.post("/follow/{target_username}")
def follow(target_username: str, current_user: str = Depends(get_current_user)):
    return follow_user(current_user, target_username)