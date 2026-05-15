from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base

DATABASE_URL = 'postgresql+asyncpg://postgres:123321@localhost:5432/DataBaseToUsers'

Base = declarative_base()

engine = create_async_engine(
    DATABASE_URL,
    pool_size = 10,
    max_overflow = 5,
    pool_timeout = 20,
    pool_pre_ping= False
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit = False
)

async def get_db():
    async with AsyncSessionLocal() as session:
     yield session


