import uvicorn
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base
from StructTableSQL import Users


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
app = FastAPI()

engine = create_async_engine(
'postgresql+asyncpg://user:password@localhost:5432/MainData',
    pool_size = 10,
    max_overflow = 5,
    pool_timeout = 20,
    pool_pre_ping= False
)

AsyncSessionLocal= async_sessionmaker(
    bind=engine,
    expire_on_commit = False
)

async def get_db():
    async with AsyncSessionLocal() as session:
     yield session

Base = declarative_base()

class Model(BaseModel):
    username: str
    password: int
    id: int

@app.get('/items')
async def get_items(db: AsyncSession = Depends(get_db)):
       result = await db.execute(select(Users))
       return result.scalars().all()

@app.post('/create')
async def create(item: Model):
    return {
        'id': Model.id,
        'username': Model.username,
        'password': Model.password
    }
@app.get ('/users')
async def list_users():
    return {"Users": Model.username}

@app.get('/users/{id}')
async def get_users():
    return {'id': id, 'username': Model.username}

@app.put('/update')
async def update():
 @app.delete('/delete/{id}')
 async def delete(id: int):
    return {'id': id}

