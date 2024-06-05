import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db

# Use a separate test database

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
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


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Create the database and tables

    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after the test

    Base.metadata.drop_all(bind=engine)


def test_create_and_get_all_questions():
    # Create a question and associated choices

    response = client.post(
        "/questions",
        json={
            "question_text": "What is the capital of France?",
            "choices": [
                {"choice_text": "Paris", "is_correct": True},
                {"choice_text": "Berlin", "is_correct": False},
                {"choice_text": "Madrid", "is_correct": False},
            ],
        },
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code},
    response: {response.json()}"

    response.json()["id"]
    # Get all questions

    response = client.get("/questions")
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code},
    response: {response.json()}"

    assert len(response.json()) == 1
    question = response.json()[0]
    assert question["question_text"] == "What is the capital of France?"
    assert len(question["choices"]) == 3
    assert any(
        choice["choice_text"] == "Paris" and choice["is_correct"]
        for choice in question["choices"]
    )


def test_delete_question():
    # Create a question and associated choices

    response = client.post(
        "/questions",
        json={
            "question_text": "What is the capital of France?",
            "choices": [
                {"choice_text": "Paris", "is_correct": True},
                {"choice_text": "Berlin", "is_correct": False},
                {"choice_text": "Madrid", "is_correct": False},
            ],
        },
    )
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code},
    response: {response.json()}"

    question_id = response.json()["id"]
    # Delete the question

    response = client.delete(f"/questions/{question_id}")
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code},
    response: {response.json()}"

    # Ensure the question is deleted

    response = client.get("/questions")
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code},
    response: {response.json()}"

    assert not any(q["id"] == question_id for q in response.json())
