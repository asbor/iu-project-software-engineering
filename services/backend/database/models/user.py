import uuid
from datetime import datetime, timezone, date
from sqlalchemy import Column, String, DateTime, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from .base import Base


class User(Base):
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
        recipe (relationship): Relationship to the Recipe table.
    """
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, \
            username={self.username}, \
            password={self.password})"
