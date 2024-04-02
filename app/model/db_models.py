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


class Publication(Base):
    __tablename__ = "publications"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,
                unique=True, nullable=False, default=uuid.uuid4)
    title = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    # define many-to-many relationship with authors
    authors = relationship(
        "Author", secondary="publication_author", back_populates="publications")
    categories = relationship(
        "Category", secondary="publication_category", back_populates="publications")

    def __repr__(self):
        return f"Publication(id={self.id}, title={self.title}, created_at={self.created_at}, updated_at={self.updated_at})"


class PublicationAuthor(Base):
    __tablename__ = "publication_author"

    publication_id = Column(UUID(as_uuid=True), ForeignKey(
        "publications.id"), primary_key=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey(
        "authors.id"), primary_key=True)


class CategoryPublication(Base):
    __tablename__ = "category_publication"

    id = Column(Integer, primary_key=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))
    publication_id = Column(UUID(as_uuid=True), ForeignKey("publications.id"))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    UniqueConstraint(category_id, publication_id)


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


class Card(Base):
    __tablename__ = "cards"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    magstripe = Column(String(20), CheckConstraint(
        'LENGTH(magstripe) >= 20 AND LENGTH(magstripe) <= 20'), nullable=False)
    status = Column(Enum('active', 'expired', 'inactive',
                    name='card_status'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Card(id={self.id}, \
                user_id={self.user_id}, \
                magstripe={self.magstripe}, \
                status={self.status}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at})"


class Instance(Base):
    __tablename__ = "instances"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)
    type = Column(Enum('physical', 'ebook', 'audiobook',
                  'publisher', name='instance_type_enum'), nullable=False)
    publisher = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(Enum('available', 'reserved',
                    name='instance_status_enum'), nullable=False)
    publication_id = Column(UUID(as_uuid=True), ForeignKey(
        'publications.id'), nullable=False)
    created_at = Column(String(255), default=datetime.now(), nullable=False)
    updated_at = Column(String(255), default=datetime.now(), nullable=False)

    def __repr__(self):
        return f"Instance(id={self.id}, \
                type={self.type}, \
                publisher={self.publisher}, \
                year={self.year}, \
                status={self.status}, \
                publication_id={self.publication_id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at})"


class Rental(Base):
    __tablename__ = "rental"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    publication_id = Column(UUID(as_uuid=True), ForeignKey(
        'instances.id'), nullable=False)
    duration = Column(Integer, nullable=False)
    start_date = Column(String(255), nullable=False)
    end_date = Column(String(255), nullable=False)
    status = Column(Enum("active", "returned", "overdue",
                    name="rental_status"), nullable=False)
    created_at = Column(String(255), default=datetime.utcnow, nullable=False)
    updated_at = Column(String(255), default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="rentals")

    def __repr__(self):
        return f"Rental(id={self.id}, \
                user_id={self.user_id}, \
                publication_id={self.publication_id}, \
                duration={self.duration}, \
                start_date={self.start_date}, \
                end_date={self.end_date}, \
                status={self.status}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at})"


class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    publication_id = Column(UUID(as_uuid=True), ForeignKey(
        'publications.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", backref="reservations")

    def __repr__(self):
        return f"Reservation(id={self.id}, \
                user_id={self.user_id}, \
                publication_id={self.publication_id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at})"
