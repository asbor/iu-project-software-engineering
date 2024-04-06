from sqlalchemy import CheckConstraint, Column, Date, DateTime, Enum, Integer, String, ForeignKey, Table, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from datetime import datetime, date
from sqlalchemy.ext.declarative import declarative_base
import uuid


Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,
                unique=True, nullable=False, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    surname = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    # define many-to-many relationship with publications
    publications = relationship(
        "Publication", secondary="publication_author", back_populates="authors")

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name}, surname={self.surname})"


class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    publications = relationship(
        "Publication", secondary="category_publication")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}, created_at={self.created_at}, updated_at={self.updated_at})"


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    birth_date = Column(Date, default=date.today, nullable=False)
    personal_identificator = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    reservation = relationship("Reservation", back_populates="user")
    rentals = relationship("Rental", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, \
                name={self.name}, \
                surname={self.surname}, \
                email={self.email}, \
                birth_date={self.birth_date}, \
                personal_identificator={self.personal_identificator}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at})"
