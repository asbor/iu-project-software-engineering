from pydantic import BaseModel
from typing import List
from .choices import Choices


class QuestionBase(BaseModel):
    """
    Description:
    This class represents the Question table in the database.

    Use cases:
    - Validate the data of a new Question object
    - Validate the data of a Question object to be updated

    Notes:
    - The id field is not included in the base model because it is generated by the database
    - The choices field is a list of Choices objects
    """
    question_text: str
    choices: List[Choices]