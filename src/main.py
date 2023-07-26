from fastapi import FastAPI
from config.database import get_db, criar_db
from src.routers import routers

app = FastAPI()

criar_db()

app.include_router(routers.router)
# syntax=docker/dockerfile:1

# FROM python:3.8-slim-buster

# WORKDIR /app
# ENV FLASK_APP run.py

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" , "--port=5000"]

