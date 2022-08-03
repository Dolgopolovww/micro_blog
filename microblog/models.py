from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.app.db.db import Base

class Post(Base):
    __tablename__ = 'microblog_posts'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    user = Column(Integer,  ForeignKey('users.id'))

    user_id = relationship('User')
