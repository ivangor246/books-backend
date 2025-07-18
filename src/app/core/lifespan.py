from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.init_models()
    yield
