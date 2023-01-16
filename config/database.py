from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE            = "postgresql"
DATABASE_USERNAME   = os.getenv('DB_USER')
DATABASE_PASSWORD   = os.getenv('DB_PASSWORD')
DATABASE_URL        = os.getenv('DB_HOST')
DATABASE_PORT       = os.getenv('DB_PORT')
DATABASE_NAME       = os.getenv('DB_NAME')

engine = create_engine("{}://{}:{}@{}:{}/{}".format(DATABASE,DATABASE_USERNAME,DATABASE_PASSWORD,DATABASE_URL,DATABASE_PORT,DATABASE_NAME))

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)