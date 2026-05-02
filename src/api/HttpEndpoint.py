
from http.client import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import  AsyncSession
from fastapi import Depends, HTTPException, APIRouter, FastAPI
from src.engine_session.database import get_db
from src.Models.pySchema import UserResponse, UserCreate, ListUsers, UserUpdate, UserLogin
from src.schema.TableModel import Users
from starlette import status
from authx import AuthX, AuthXConfig

router = APIRouter()

config = AuthXConfig(
    JWT_SECRET_KEY = 'SECRET_KEY',
    JWT_ACCESS_COOKIE_NAME= 'JWT_ACCESS_COOKIE',
    JWT_ALGORITHM = 'HS256',
    JWT_TOKEN_LOCATION = ['cookies']
)

auth = AuthX(config = config)


@router.post('/login', response_model=UserLogin, status_code = 200, tags = ['Login'], summary= "Login to user")
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    if user_data.username == user_data.username and user_data.password == user_data.password:

        user_token = auth.create_access_token(uid=user_data.username, fresh=True)
        await db.commit()
        return {'access_token': user_token}, status.HTTP_200_OK

    else:

        raise HTTPException(status_code = 401, detail = 'Incorrect username or password')

@router.post('/user', response_model = UserResponse, status_code = 201, tags = ['Users'], summary= "Create a new user")
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

@router.get('/ListUsers', response_model = list[ListUsers], status_code = 200,  tags = ['GetUsers'], summary= "Get all users")
async def list_users(user_id: ListUsers, username: ListUsers, db: AsyncSession = Depends(get_db)):

    query =  select(Users).where(Users.id == user_id, Users.username == username)
    users_query = await db.execute(query)

    return users_query.scalars().all(), status.HTTP_200_OK

@router.patch('/update')
async def update_data(update: UserUpdate, db: AsyncSession = Depends(get_db)):
   pass