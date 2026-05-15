import hashlib
import os
from fastapi import Depends, HTTPException
from src.Models.pySchema import UserLogin


def hash_password_function(plain_password):

    salt = os.urandom(16)
    transform = hashlib.pbkdf2_hmac('sha256', plain_password.encode('utf-8'), salt, 100_000)

    return salt + transform


async def verify_password_function(hashed_password: bytes, plain_password) -> bool:

    salt_first = hashed_password[:16]
    salt_beyond = hashed_password[16:]

    transform = hashlib.pbkdf2_hmac('sha256', plain_password.endcode('utf-8'), salt_first, 100_000)

    return salt_beyond == transform









