from typing import Optional
from pydantic import BaseModel


class UserInSchema(BaseModel):
    username: str
    email: str
    full_name: str
    password: str


class UserOutSchema(BaseModel):
    id: int
    username: str
    email: str
    full_name: str


class UserDatabaseSchema(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
