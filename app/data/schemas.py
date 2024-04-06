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


class User(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    surname: str
    email: str
    birth_date: date
    personal_identificator: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
