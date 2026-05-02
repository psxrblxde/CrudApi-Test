from database import Base
from sqlalchemy import Integer, Column, String


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String, unique=False, index=True)

