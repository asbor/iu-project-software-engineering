import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
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


def create_test_recipe(db):
    recipe = models.Recipes(
        name="Test Recipe",
        is_batch=False,
        version="1.0",
        type="Ale",
        brewer="Test Brewer",
        batch_size=20.0,
        boil_size=25.0,
        boil_time=60,
        efficiency=75.0,
        notes="Test Notes",
        taste_notes="Test Taste Notes",
        taste_rating=5,
        og=1.050,
        fg=1.010,
        fermentation_stages=1,
        primary_age=7,
        primary_temp=20.0,
        secondary_age=7,
        secondary_temp=20.0,
        age=14,
        age_temp=10.0,
        carbonation_used="CO2",
        est_og=1.050,
        est_fg=1.010,
        est_color=10.0,
        ibu=40.0,
        ibu_method="Tinseth",
        est_abv=5.0,
    )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    logger.debug(f"Created test recipe with ID: {recipe.id}")
    return recipe


def test_create_batch():
    # Create a test recipe
    # TODO: Create a test recipe
    pass
