import hashlib
import os
from authx import AuthXConfig, AuthX
from fastapi import Depends, HTTPException
from src.Models.pySchema import UserLogin
from typing_extensions import Buffer

config = AuthXConfig(
    JWT_SECRET_KEY = 'SECRET_KEY',
    JWT_ACCESS_COOKIE_NAME= 'JWT_ACCESS_COOKIE',
    JWT_ALGORITHM = 'HS256',
    JWT_TOKEN_LOCATION = ['cookies']

)

auth = AuthX(config = config)

def hash_password_function(plain_password: str):

    salt = os.urandom(16)
    transform = hashlib.pbkdf2_hmac('sha256', plain_password.encode('utf-8'), salt, 100_000)

    return salt + transform


def verify_password_function(self, user: UserLogin, key = Depends(hash_password_function)):

    if user.password == user.password:

        self.hashed_password = user.password
        coded_password = key(self.hasehd_password)

        return coded_password

    else:

        raise HTTPException(status_code=500, detail='Error')




