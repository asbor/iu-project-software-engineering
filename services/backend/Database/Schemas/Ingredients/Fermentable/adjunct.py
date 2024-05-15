from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Adjunct(BaseModel):
    """
    Adjunct model

    Attributes:
        id (UUID): The unique identifier for the adjunct.
        total_ibu_per_kg (float): The total IBU per kg of the adjunct.
    Relationships:
        fermentable (Fermentable): The associated fermentable.
    """

    id: uuid.UUID
    total_ibu_per_kg: float
    fermentable_id: uuid.UUID

    class Config:
        from_attributes = True
