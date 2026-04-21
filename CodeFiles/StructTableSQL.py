from postgresql import base
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

class Users(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
