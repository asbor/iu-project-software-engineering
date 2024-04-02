from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Author(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Category(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Publication(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    title: str
    authors: List[Author]
    categories: List[Category]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Reservation(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    user_id: uuid.UUID
    publication_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Rental(BaseModel):
    ALLOWED_STATUSES = ["active", "returned", "overdue"]

    id: uuid.UUID = uuid.uuid4()
    user_id: uuid.UUID
    publication_id: uuid.UUID
    duration: int
    start_date: str
    end_date: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class User(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    surname: str
    email: str
    birth_date: date
    personal_identificator: str
    reservations: List[Reservation] = []
    rentals: List[Rental] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Card(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    user_id: uuid.UUID
    magstripe: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Instance(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    type: str
    publisher: str
    year: int
    status: str
    publication_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
