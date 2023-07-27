from fastapi import FastAPI
from src.config.database import get_db, criar_db
from src.routers import routers

app = FastAPI()

criar_db()

app.include_router(routers.router)
