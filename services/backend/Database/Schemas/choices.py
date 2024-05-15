from pydantic import BaseModel


class Choices(BaseModel):
    """
    Description:
    This class represents the Choice table in the database.

    Use cases:
    - Validate the data of a new Choice object
    - Validate the data of a Choice object to be updated
    """
    choice_text: str
    is_correct: bool
