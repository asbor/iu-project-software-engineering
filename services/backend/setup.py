import os
import logging.config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


import time

load_dotenv()

print(os.getenv("DATABASE_USER"))

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}/{os.environ['DATABASE_NAME']}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# wait for the database to be available before connecting
while not database_exists(SQLALCHEMY_DATABASE_URL):
    print("Waiting for the database to be available")
    time.sleep(1)

    if not database_exists(engine.url):
        create_database(engine.url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
