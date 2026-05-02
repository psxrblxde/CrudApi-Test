from http.client import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import  AsyncSession,async_sessionmaker
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from TableModel import Users
from contextlib import asynccontextmanager
from database import Base, get_db, engine
from starlette import status


app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await conn.commit()
    await conn.dispose()

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

class UserUpdate(BaseModel):
    username: str
    password: str
class ListUsers(BaseModel):
    id: int
    username: str
    password: str


    class Config:
        from_attributes = True


@app.post('/user', response_model = UserResponse, status_code = 201)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):

    existing_request = select(Users).where(Users.username == user_data.username)
    result_request = await db.execute(existing_request)
    existing_user = result_request.scalar_one_or_none()

    if existing_user:

        raise HTTPException(status_code = 404, detail = 'This name already exist')

    else:

        new_user = Users(username = user_data.username, password = user_data.password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

    return new_user

@app.get('/ListUsers', response_model = list[ListUsers], status_code = 200)
async def list_users(user_id: ListUsers, username: ListUsers, db: AsyncSession = Depends(get_db)):

    request =  select(Users).where(Users.id == user_id, Users.username == username)
    users_request = await db.execute(request)

    return users_request.scalars().all(), status.HTTP_200_OK

@app.patch('/update')
async def update_data(update: UserUpdate, db: AsyncSession = Depends(get_db)):
   pass

