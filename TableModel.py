from database import BaseTable
from sqlalchemy import Integer, Column, String


class Users(BaseTable):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
