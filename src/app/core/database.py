from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import config
from app.models import BaseModel

engine = create_async_engine(url=config.DB_URL)
session_factory = async_sessionmaker(engine, expire_on_commit=False)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session


async def init_models() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def drop_models() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
