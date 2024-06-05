# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import time
from logger_config import get_logger

# Get logger instance

logger = get_logger("Setup")

# Load environment variables

logger.info("Loading environment variables")
load_dotenv()

# Determine if we are in testing mode

IS_TESTING = os.getenv("TESTING", "0") == "1"
logger.info(f"IS_TESTING: {IS_TESTING}")
if IS_TESTING:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
else:
    SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"

# Connect to the database

logger.info(f"Connecting to the database: {SQLALCHEMY_DATABASE_URL}")
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
if not IS_TESTING:
    from sqlalchemy_utils import database_exists, create_database

    # Wait for the database to be available before connecting

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
