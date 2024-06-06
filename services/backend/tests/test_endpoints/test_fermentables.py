import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from datetime import datetime
import Database.Models as models
import logging

# Use a separate test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_batches.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Override the get_db function to use the test database


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Create the database and tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after the test
    Base.metadata.drop_all(bind=engine)


def test_create_fermentable():
    response = client.post(
        "/inventory/fermentables",
        json={
            "name": "Test Fermentable",
            "type": "Grain",
            "yield_": 75.0,
            "color": 10,
            "origin": "USA",
            "supplier": "Test Supplier",
            "notes": "Test Notes",
            "potential": 1.037,
            "amount": 5.0,
            "cost_per_unit": 1.5,
            "manufacturing_date": "2024-01-01",
            "expiry_date": "2025-01-01",
            "lot_number": "12345",
            "exclude_from_total": False,
            "not_fermentable": False,
            "description": "Test Description",
            "substitutes": "Test Substitutes",
            "used_in": "Test Used In",
        },
    )

    # Print the response for debugging
    print(response.json())

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response: {response.json()}"

    fermentable = response.json()
    assert fermentable["name"] == "Test Fermentable"
    assert fermentable["type"] == "Grain"
    assert fermentable["yield_"] == 75.0
    assert fermentable["color"] == 10
    assert fermentable["origin"] == "USA"
    assert fermentable["supplier"] == "Test Supplier"
    assert fermentable["notes"] == "Test Notes"
    # Allowing a small margin for float comparison
    assert fermentable["potential"] == pytest.approx(1.037, abs=1e-3)
