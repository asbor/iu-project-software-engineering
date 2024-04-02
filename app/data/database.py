from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# BUG: This is a workaround for the fact that the database URL is not being passed to the container correctly

# remove special characters (except . and _) from string and convert to lowercase


def clean_string(string):
    return "".join([char for char in string if char.isalnum() or char in ["_", "."]]).lower()


user = clean_string(os.getenv("DATABASE_USER"))
password = clean_string(os.getenv("DATABASE_PASSWORD"))
host = clean_string(os.getenv("DATABASE_HOST"))
port = clean_string(os.getenv("DATABASE_PORT"))
dbname = clean_string(os.getenv("DATABASE_NAME"))

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{dbname}"
# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:postgres@host.docker.internal/library_db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/library_db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
