from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

engine = create_async_engine('postgres+asyncpg:///user:password@localhost:5432/MainData')

AsyncSessionLocal= async_sessionmaker(
    bind=engine,
    expire_on_commit = False
)

async def get_db():
    async with AsyncSessionLocal() as session:
     yield session


class Model(BaseModel):
    username: str
    password: int
    id: int

@app.get('/items/')
async def get_items():
    async with AsyncSessionLocal() as session:
     result = await session.execute()
    return result.scalars().all()

@app.post('/create')
def create(Model: id):
    return {'id': Model}

@app.get ('/users')
def list_users():
    return {"Users": Model.username}

@app.get('/users/{id}')
def get_users():
    return {'id': id}

@app.put('/update')
def update():


 @app.delete('/delete/{id}')
 def delete(id: int):
    return {'id': id}

