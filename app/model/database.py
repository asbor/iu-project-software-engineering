from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


print(os.environ["DATABASE_USER"])


user = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
dbname = os.getenv("DATABASE_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
