import hashlib
import os
from authx import AuthXConfig, AuthX
from fastapi import Depends, HTTPException
from src.Models.pySchema import UserLogin

config = AuthXConfig(
    JWT_SECRET_KEY = 'SECRET_KEY',
    JWT_ACCESS_COOKIE_NAME= 'JWT_ACCESS_COOKIE',
    JWT_ALGORITHM = 'HS256',
    JWT_TOKEN_LOCATION = ['cookies']

)

auth = AuthX(config = config)

def hash_password_function(self, hashed_password) -> bytes:

    self.hashed_password = hashed_password

    generate_random_symbol = os.urandom(16)
    sorted_key = generate_random_symbol[:16]

    crypto_password = hashlib.sha256(hashed_password.encoded('utf-8')).hexdigest()
    crypto_password = bytes.fromhex(crypto_password)
    transform = hashlib.pbkdf2_hmac('sha256', hashed_password, sorted_key.encoded('utf-8'), 100_000)

    return transform + crypto_password


def verify_password_function(self, user: UserLogin, key = Depends(hash_password_function)):

    if user.password == user.password:

        self.hashed_password = user.password
        coded_password = key(self.hasehd_password)

        return coded_password

    else:

        raise HTTPException(status_code=500, detail='Error')




