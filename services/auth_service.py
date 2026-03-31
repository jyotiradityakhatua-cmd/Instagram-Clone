from app.services.user_service import get_user
from app.core.security import verify_password, create_access_token

def login(username, password):
    user = get_user(username)

    if not user or not verify_password(password, user["password"]):
        return None

    token= create_access_token({"username": user["username"]})
    return token
    