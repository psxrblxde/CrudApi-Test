from pydantic import BaseModel

#Endpoint for crud operation
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

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

    class Config:
        from_attributes = True

