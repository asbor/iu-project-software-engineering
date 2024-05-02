from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Users(BaseModel):
    """
    A class representing the User table in the database.

    This table stores information about users, including their name, email, and birth date.

    Attributes:
        id (UUID): The unique identifier for the user.
        name (str): The name of the user.
        surname (str): The surname of the user.
        email (str): The email address of the user.
        birth_date (Date): The birth date of the user.
        personal_identificator (str): The personal identification number of the user.
        created_at (DateTime): The timestamp when the user was created.
        updated_at (DateTime): The timestamp when the user was last updated.
        recipes (relationship): Relationship to the Recipes table.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    surname: str
    email: str
    birth_date: date
    personal_identificator: str
    recipes: List[uuid.UUID]

    class Config:
        orm_mode = True
