from src.engine_session.database import Base
from sqlalchemy import Integer, Column, String, LargeBinary


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=False, index=True)
    password = Column(LargeBinary, unique=False, index=True)

