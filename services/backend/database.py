from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils import database_exists, create_database

import time
import os
from dotenv import load_dotenv
from logger_config import get_logger

# Get logger instance
logger = get_logger('Setup')

# Load environment variables
logger.info("Loading environment variables")
load_dotenv()

# Connect to the database
logger.info("Connecting to the database")
SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}/{os.environ['DATABASE_NAME']}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# wait for the database to be available before connecting
logger.info("Waiting for the database to be available")
while not database_exists(SQLALCHEMY_DATABASE_URL):
    time.sleep(1)

    # Create the database if it does not exist
    if not database_exists(engine.url):
        logger.info("Creating the database")
        create_database(engine.url)

# Create a session local
logger.info("Database is available")
logger.info("Creating a session local")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the models to inherit from (declarative base)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
