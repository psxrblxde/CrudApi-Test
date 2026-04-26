from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from TableModel import Users
from database import get_db, engine, async_sessionmaker

app = FastAPI()

class Model(BaseModel):
    username: str
    password: int
    id: int

@app.get('/user')
async def get_user(db: AsyncSession = Depends(get_db)):
       result = await db.execute(select(Users))
       return result.scalars().all()

@app.post('/user_create')
async def user_create(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Users))
    return result.scalars().all()

@app.get ('/users')
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Users))
    return result.scalars().all()

@app.get('/users')
async def get_user(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Users))
    return result.scalars().all()

@app.put('/update')
async def update(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Users))
    return result.scalars