from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: str
    password: str

class ListUsers(BaseModel):
    id: int
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True