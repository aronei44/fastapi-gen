
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