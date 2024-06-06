import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
import logging

# Use a separate test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_miscs.db"
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


def test_create_misc(client):
    response = client.post(
        "/inventory/miscs",
        json={
            "name": "Test Misc",
            "type": "Spice",
            "use": "Boil",
            "amount_is_weight": True,
            "use_for": "Flavor",
            "notes": "Test Notes",
            "amount": 10,
            "time": 15,
            "display_amount": "10g",
            "inventory": 100,
            "display_time": "15min",
            "batch_size": 20,
        },
    )

    assert response.status_code == 200, f'''
    Unexpected status code: {response.status_code}, 
    response: {response.json()}"'''

    misc = response.json()
    assert misc["name"] == "Test Misc"
    assert misc["type"] == "Spice"
    assert misc["use"] == "Boil"
    assert misc["amount_is_weight"] is True
    assert misc["use_for"] == "Flavor"
    assert misc["notes"] == "Test Notes"
    assert misc["amount"] == 10
    assert misc["time"] == 15
    assert misc["display_amount"] == "10g"
    assert misc["inventory"] == 100
    assert misc["display_time"] == "15min"
    assert misc["batch_size"] == 20


def test_get_all_miscs(client):
    # Create a new misc to ensure there's at least one entry
    client.post(
        "/inventory/miscs",
        json={
            "name": "Test Misc",
            "type": "Spice",
            "use": "Boil",
            "amount_is_weight": True,
            "use_for": "Flavor",
            "notes": "Test Notes",
            "amount": 10,
            "time": 15,
            "display_amount": "10g",
            "inventory": 100,
            "display_time": "15min",
            "batch_size": 20,
        }
    )
    response = client.get("/inventory/miscs")
    assert response.status_code == 200
    miscs = response.json()
    assert isinstance(miscs, list)
    assert len(miscs) > 0


def test_get_misc_by_id(client):
    # First create a misc
    response = client.post(
        "/inventory/miscs",
        json={
            "name": "Test Misc",
            "type": "Spice",
            "use": "Boil",
            "amount_is_weight": True,
            "use_for": "Flavor",
            "notes": "Test Notes",
            "amount": 10,
            "time": 15,
            "display_amount": "10g",
            "inventory": 100,
            "display_time": "15min",
            "batch_size": 20,
        },
    )
    misc_id = response.json()["id"]

    # Get the created misc by ID
    response = client.get(f"/inventory/miscs/{misc_id}")
    assert response.status_code == 200
    misc = response.json()
    assert misc["id"] == misc_id


def test_update_misc(client):
    # First create a misc
    response = client.post(
        "/inventory/miscs",
        json={
            "name": "Test Misc",
            "type": "Spice",
            "use": "Boil",
            "amount_is_weight": True,
            "use_for": "Flavor",
            "notes": "Test Notes",
            "amount": 10,
            "time": 15,
            "display_amount": "10g",
            "inventory": 100,
            "display_time": "15min",
            "batch_size": 20,
        },
    )
    misc_id = response.json()["id"]

    # Update the created misc
    response = client.put(
        f"/inventory/miscs/{misc_id}",
        json={
            "name": "Updated Test Misc",
            "type": "Herb",
            "use": "Fermentation",
            "amount_is_weight": False,
            "use_for": "Aroma",
            "notes": "Updated Notes",
            "amount": 20,
            "time": 30,
            "display_amount": "20g",
            "inventory": 200,
            "display_time": "30min",
            "batch_size": 40,
        },
    )
    assert response.status_code == 200
    updated_misc = response.json()
    assert updated_misc["name"] == "Updated Test Misc"
    assert updated_misc["type"] == "Herb"
    assert updated_misc["use"] == "Fermentation"
    assert updated_misc["amount_is_weight"] is False
    assert updated_misc["use_for"] == "Aroma"
    assert updated_misc["notes"] == "Updated Notes"
    assert updated_misc["amount"] == 20
    assert updated_misc["time"] == 30
    assert updated_misc["display_amount"] == "20g"
    assert updated_misc["inventory"] == 200
    assert updated_misc["display_time"] == "30min"
    assert updated_misc["batch_size"] == 40


def test_delete_misc(client):
    # First create a misc
    response = client.post(
        "/inventory/miscs",
        json={
            "name": "Test Misc",
            "type": "Spice",
            "use": "Boil",
            "amount_is_weight": True,
            "use_for": "Flavor",
            "notes": "Test Notes",
            "amount": 10,
            "time": 15,
            "display_amount": "10g",
            "inventory": 100,
            "display_time": "15min",
            "batch_size": 20,
        },
    )
    misc_id = response.json()["id"]

    # Delete the created misc
    response = client.delete(f"/inventory/miscs/{misc_id}")
    assert response.status_code == 200

    # Verify the misc is deleted
    response = client.get(f"/inventory/miscs/{misc_id}")
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()
