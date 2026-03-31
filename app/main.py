from fastapi import FastAPI
from app.routes.user_routes import router as user_routes
from app.routes.follow_routes import router as follow_routes
from app.routes.auth_routes import router as auth_routes


app = FastAPI()

app.include_router(user_routes, prefix="/users")
app.include_router(follow_routes, prefix="/social")
app.include_router(auth_routes, prefix="/auth")