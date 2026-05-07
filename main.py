from http.client import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import  AsyncSession
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from src.Models.TableModel import Users
from contextlib import asynccontextmanager
from database import Base, get_db, engine


app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.connection = {}
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    app.state.connection.clear = {}
    await conn.dispose()

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

class ListUsers(BaseModel):
    id: int
    username: str
    password: str


    class Config:
        from_attributes = True


@app.post('/user', response_model = UserResponse, status_code = 201)
async def create_user(UserData: UserCreate, db: AsyncSession = Depends(get_db)):

    ExistingRequest = select(Users).where(Users.username == UserData.username)
    ResultRequest = await db.execute(ExistingRequest)
    existing_user = ResultRequest.scalar_one_or_none()

    if existing_user:

        raise HTTPException(status_code = 404, detail = 'This name already exist')

    else:

        new_user = Users(username = UserData.username, password = UserData.password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

    return new_user

@app.get ('/ListUsers/', response_model = ListUsers)
async def list_users(GetUsers: ListUsers, db: AsyncSession = Depends(get_db)):

    ViewUsers = select(Users)
    Request = await db.execute(ViewUsers)

    return Request.scalars()
@app.put('/update')
async def update_data(db: AsyncSession = Depends(get_db)):
    pass

