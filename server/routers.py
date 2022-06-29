from fastapi import APIRouter

from app.user.views import user_router
from app.auth.views import auth_router
from app.exam.views import exam_router

routers = APIRouter()

routers.include_router(user_router, prefix="")
routers.include_router(auth_router, prefix="/auth")
routers.include_router(exam_router, prefix="/exam")