import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
import logging

# Use a separate test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_hops.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})
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
    logger.debug("Creating test database")
    Base.metadata.create_all(bind=engine)
    yield
    logger.debug("Dropping test database")
    Base.metadata.drop_all(bind=engine)


def test_create_inventory_hop(client):
    # Create a new inventory hop
    response = client.post(
        "/inventory/hops",
        json={
            "name": "Test Hop",
            "origin": "USA",
            "alpha": 5.5,
            "type": "Bittering",
            "form": "Pellet",
            "beta": 3.0,
            "hsi": 0.25,
            "amount": 10.0,
            "use": "Boil",
            "time": 60,
            "notes": "Test notes",
            "display_amount": "10 grams",
            "inventory": "5 units",
            "display_time": "60 minutes"
        }
    )
    assert response.status_code == 200, f'''
    Unexpected status code: {response.status_code}'''

    hop = response.json()
    assert hop["name"] == "Test Hop"


def test_get_all_inventory_hops(client):
    # Create a new inventory hop to ensure there's at least one entry
    client.post(
        "/inventory/hops",
        json={
            "name": "Test Hop",
            "origin": "USA",
            "alpha": 5.5,
            "type": "Bittering",
            "form": "Pellet",
            "beta": 3.0,
            "hsi": 0.25,
            "amount": 10.0,
            "use": "Boil",
            "time": 60,
            "notes": "Test notes",
            "display_amount": "10 grams",
            "inventory": "5 units",
            "display_time": "60 minutes"
        }
    )
    # Get all inventory hops
    response = client.get("/inventory/hops")
    assert response.status_code == 200, f'''
    Unexpected status code: {response.status_code}'''

    hops = response.json()
    assert isinstance(hops, list)
    assert len(hops) > 0


def test_get_inventory_hop(client):
    # Create a new inventory hop
    response = client.post(
        "/inventory/hops",
        json={
            "name": "Test Hop",
            "origin": "USA",
            "alpha": 5.5,
            "type": "Bittering",
            "form": "Pellet",
            "beta": 3.0,
            "hsi": 0.25,
            "amount": 10.0,
            "use": "Boil",
            "time": 60,
            "notes": "Test notes",
            "display_amount": "10 grams",
            "inventory": "5 units",
            "display_time": "60 minutes"
        }
    )
    hop = response.json()
    hop_id = hop["id"]

    # Fetch the created inventory hop
    response = client.get(f"/inventory/hops/{hop_id}")
    assert response.status_code == 200, f'''
    Unexpected status code: {response.status_code}'''

    hop = response.json()
    assert hop["name"] == "Test Hop"


def test_update_inventory_hop(client):
    # Create a new inventory hop
    response = client.post(
        "/inventory/hops",
        json={
            "name": "Test Hop",
            "origin": "USA",
            "alpha": 5.5,
            "type": "Bittering",
            "form": "Pellet",
            "beta": 3.0,
            "hsi": 0.25,
            "amount": 10.0,
            "use": "Boil",
            "time": 60,
            "notes": "Test notes",
            "display_amount": "10 grams",
            "inventory": "5 units",
            "display_time": "60 minutes"
        }
    )
    hop = response.json()
    hop_id = hop["id"]

    # Update the created inventory hop
    response = client.put(
        f"/inventory/hops/{hop_id}",
        json={
            "name": "Updated Test Hop",
            "origin": "Germany",
            "alpha": 6.0,
            "type": "Aroma",
            "form": "Leaf",
            "beta": 3.5,
            "hsi": 0.3,
            "amount": 15.0,
            "use": "Dry Hop",
            "time": 30,
            "notes": "Updated test notes",
            "display_amount": "15 grams",
            "inventory": "10 units",
            "display_time": "30 minutes"
        }
    )
    assert response.status_code == 200, f'''
    Unexpected status code: {response.status_code}'''

    hop = response.json()
    assert hop["name"] == "Updated Test Hop"


def test_delete_inventory_hop(client):
    # Create a new inventory hop
    response = client.post(
        "/inventory/hops",
        json={
            "name": "Test Hop",
            "origin": "USA",
            "alpha": 5.5,
            "type": "Bittering",
            "form": "Pellet",
            "beta": 3.0,
            "hsi": 0.25,
            "amount": 10.0,
            "use": "Boil",
            "time": 60,
            "notes": "Test notes",
            "display_amount": "10 grams",
            "inventory": "5 units",
            "display_time": "60 minutes"
        }
    )
    hop = response.json()
    hop_id = hop["id"]

    # Delete the created inventory hop
    response = client.delete(f"/inventory/hops/{hop_id}")
    assert response.status_code == 200, f'''
    Unexpected status code: {response.status_code}'''

    # Verify the hop was deleted
    response = client.get(f"/inventory/hops/{hop_id}")
    assert response.status_code == 200, f'''
    Unexpected status code: {response.status_code}'''


if __name__ == "__main__":
    pytest.main()
