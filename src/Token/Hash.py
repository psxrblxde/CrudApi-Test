import hashlib
import os
from fastapi import Depends, HTTPException
from src.Models.pySchema import UserLogin



def hash_password_function(plain_password):

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




