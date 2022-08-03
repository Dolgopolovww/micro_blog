from sqlalchemy import Column, String, Text, DateTime, Integer, Boolean
from src.app.db.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    login = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    date = Column(DateTime) # дата регистрации
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

