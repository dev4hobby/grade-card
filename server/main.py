from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from core.config import SECRET_KEY, DATABASE_URL, APPS_MODELS
from routers import routers

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app=app,
    db_url=DATABASE_URL,
    modules={"models": APPS_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(routers)