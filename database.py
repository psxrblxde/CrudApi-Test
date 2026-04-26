from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
import uvicorn


DATABASE_URL = 'postgresql+asyncpg://user:password@localhost:5432/MainData'

engine = create_async_engine(
    DATABASE_URL,
    pool_size = 10,
    max_overflow = 5,
    pool_timeout = 20,
    pool_pre_ping= False
)

BaseTable = declarative_base()

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit = False
)

async def get_db():
    async with AsyncSessionLocal() as session:
     yield session


