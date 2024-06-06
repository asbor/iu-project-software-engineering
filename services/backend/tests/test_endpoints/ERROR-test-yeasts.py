import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
import Database.Models as models
import Database.Schemas as schemas

# Use a separate test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_yeasts.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# Override the get_db function to use the test database


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Create the database and tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after the test
    Base.metadata.drop_all(bind=engine)


def test_create_inventory_yeast():
    response = client.post(
        "/inventory/yeasts",
        json={
            "name": "Test Yeast",
            "type": "Ale",
            "form": "Dry",
            "amount": 10.0,
            "amount_is_weight": True,
            "laboratory": "Test Lab",
            "product_id": "T123",
            "min_temperature": 18.0,
            "max_temperature": 22.0,
            "flocculation": "High",
            "attenuation": 75.0,
            "notes": "Test notes",
            "best_for": "Test Ale",
            "times_cultured": 5,
            "max_reuse": 10,
            "add_to_secondary": True,
            "batch_id": 1
        }
    )
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    yeast = response.json()
    assert yeast["name"] == "Test Yeast"
    assert yeast["type"] == "Ale"


def test_get_all_inventory_yeasts():
    response = client.get("/inventory/yeasts")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    yeasts = response.json()
    assert isinstance(yeasts, list)


def test_get_inventory_yeast():
    response = client.post(
        "/inventory/yeasts",
        json={
            "name": "Test Yeast",
            "type": "Ale",
            "form": "Dry",
            "amount": 10.0,
            "amount_is_weight": True,
            "laboratory": "Test Lab",
            "product_id": "T123",
            "min_temperature": 18.0,
            "max_temperature": 22.0,
            "flocculation": "High",
            "attenuation": 75.0,
            "notes": "Test notes",
            "best_for": "Test Ale",
            "times_cultured": 5,
            "max_reuse": 10,
            "add_to_secondary": True,
            "batch_id": 1
        }
    )
    yeast = response.json()
    yeast_id = yeast["id"]

    response = client.get(f"/inventory/yeasts/{yeast_id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    yeast = response.json()
    assert yeast["name"] == "Test Yeast"
    assert yeast["id"] == yeast_id


def test_update_inventory_yeast():
    response = client.post(
        "/inventory/yeasts",
        json={
            "name": "Test Yeast",
            "type": "Ale",
            "form": "Dry",
            "amount": 10.0,
            "amount_is_weight": True,
            "laboratory": "Test Lab",
            "product_id": "T123",
            "min_temperature": 18.0,
            "max_temperature": 22.0,
            "flocculation": "High",
            "attenuation": 75.0,
            "notes": "Test notes",
            "best_for": "Test Ale",
            "times_cultured": 5,
            "max_reuse": 10,
            "add_to_secondary": True,
            "batch_id": 1
        }
    )
    yeast = response.json()
    yeast_id = yeast["id"]

    response = client.put(
        f"/inventory/yeasts/{yeast_id}",
        json={
            "name": "Updated Test Yeast",
            "type": "Lager",
            "form": "Liquid",
            "amount": 20.0,
            "amount_is_weight": False,
            "laboratory": "Updated Lab",
            "product_id": "U123",
            "min_temperature": 10.0,
            "max_temperature": 15.0,
            "flocculation": "Low",
            "attenuation": 80.0,
            "notes": "Updated notes",
            "best_for": "Updated Lager",
            "times_cultured": 6,
            "max_reuse": 12,
            "add_to_secondary": False,
            "batch_id": 2
        }
    )
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    updated_yeast = response.json()
    assert updated_yeast["name"] == "Updated Test Yeast"
    assert updated_yeast["type"] == "Lager"


def test_delete_inventory_yeast():
    response = client.post(
        "/inventory/yeasts",
        json={
            "name": "Test Yeast",
            "type": "Ale",
            "form": "Dry",
            "amount": 10.0,
            "amount_is_weight": True,
            "laboratory": "Test Lab",
            "product_id": "T123",
            "min_temperature": 18.0,
            "max_temperature": 22.0,
            "flocculation": "High",
            "attenuation": 75.0,
            "notes": "Test notes",
            "best_for": "Test Ale",
            "times_cultured": 5,
            "max_reuse": 10,
            "add_to_secondary": True,
            "batch_id": 1
        }
    )
    yeast = response.json()
    yeast_id = yeast["id"]

    response = client.delete(f"/inventory/yeasts/{yeast_id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    deleted_yeast = response.json()
    assert deleted_yeast["id"] == yeast_id

    response = client.get(f"/inventory/yeasts/{yeast_id}")
    assert response.status_code == 404, f"Unexpected status code: {response.status_code}"


if __name__ == "__main__":
    pytest.main()
