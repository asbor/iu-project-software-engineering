from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class User(BaseModel):
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
    """

    id: uuid.UUID
    username: str
    password: str

    class Config:
        from_attributes = True
