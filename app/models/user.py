from sqlalchemy import Column, Integer, String, Float,DateTime
from app.database import Base
from pydantic import EmailStr
import datetime

class Timestamp:
    
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime,default=datetime.datetime.now, onupdate=datetime.datetime.now)

class Users(Base, Timestamp):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password =  Column(String,nullable=False)
