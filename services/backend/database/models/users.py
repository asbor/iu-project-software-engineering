import uuid
from datetime import datetime, timezone, date
from sqlalchemy import Column, String, DateTime, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from .base import Base


class Users(Base):
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
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    birth_date = Column(Date, default=date.today, nullable=False)
    personal_identificator = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)

    recipes = relationship("Recipes", back_populates="created_by")

    def __repr__(self):
        return f"User(id={self.id}, \
                name={self.name}, \
                surname={self.surname}, \
                email={self.email}, \
                birth_date={self.birth_date}, \
                personal_identificator={self.personal_identificator}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at})"
