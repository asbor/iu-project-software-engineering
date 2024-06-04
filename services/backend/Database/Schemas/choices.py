# Database/Schemas/choices.py

from pydantic import BaseModel


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

    class Config:
        orm_mode = True
