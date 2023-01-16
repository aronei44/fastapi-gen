from sqlalchemy import Column, Integer, String, Date
from config.database import Base
from pydantic import BaseModel

# this is class for table (database)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    email = Column(String(45))
    password = Column(String(256))
    status = Column(String(10))
    created_at = Column(Date)

# this is class for request body
class Register(BaseModel):
    name : str
    email : str
    password : str

class Login(BaseModel):
    email: str
    password: str