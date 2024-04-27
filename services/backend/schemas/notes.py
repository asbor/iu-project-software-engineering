from typing import Optional
from pydantic import BaseModel
from schemas.users import UserOutSchema


class NoteInSchema(BaseModel):
    title: str
    content: str


class NoteOutSchema(BaseModel):
    id: int
    title: str
    content: str
    created_at: Optional[str]
    author: UserOutSchema


class UpdateNote(BaseModel):
    title: Optional[str]
    content: Optional[str]
