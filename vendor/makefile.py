
class MakeFile:
    def __init__(self, name):
        self.name = name

    def controller(self):
        try:
            namefile = 'app/controllers/' + self.name + '.py'
            f = open(namefile, 'x')
            f.write("""from fastapi import HTTPException

async def main(data, session):
    pass""")
            f.close()
        except Exception as e:
            print(e)


    def model(self):
        try:
            namefile = 'app/models/' + self.name + '.py'
            f = open(namefile, 'x')
            f.write("""from sqlalchemy import Column, Integer, String, Date
from config.database import Base
from pydantic import BaseModel

# this is class for table (database)
class {}(Base):
    __tablename__ = "{}"

# this is class for request body
class Register(BaseModel):
    pass""".format(self.name.title(), self.name.lower() + 's'))
            f.close()
        except Exception as e:
            print(e)


    def route(self):
        try:
            namefile = 'routes/' + self.name + 'Route.py'
            f = open(namefile, 'x')
            f.write("""from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from config.session import get_session


router = APIRouter()

@router.get('/', status_code=200)
async def main():
    return 'ok'""")
            f.close()

            f = open('main.py', 'a')
            f.write("""
from routes import {0}Route
app.include_router({0}Route.router, prefix="/api/{0}", tags=["{0}"])
""".format(self.name))
            f.close()
        except Exception as e:
            print(e)