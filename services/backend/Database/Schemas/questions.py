from pydantic import BaseModel
from typing import List
from .choices import ChoiceBase


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

    class Config:
        orm_mode = True


class QuestionWithID(QuestionBase):
    id: int

    class Config:
        orm_mode = True
