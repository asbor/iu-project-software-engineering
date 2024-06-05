import os
import pytest
import logging
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db

# Setup logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Set environment variable for testing

os.environ["TESTING"] = "1"
logger.debug(f"Environment variable TESTING set to: {os.environ['TESTING']}")

# Database setup for testing

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
logger.debug(f"SQLALCHEMY_DATABASE_URL set to: {SQLALCHEMY_DATABASE_URL}")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client():
    logger.debug("Creating test database")
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    logger.debug("Dropping test database")
    Base.metadata.drop_all(bind=engine)
