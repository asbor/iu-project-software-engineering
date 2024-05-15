from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Other(BaseModel):
    """
    Other model

    Attributes:
        id (UUID): The unique identifier for the other.
        total_ibu_per_kg (decimal): The total IBU per kg of the other.

    Relationships:
        fermentable_id (uuid): The fermentable relationship.
    """

    id: uuid.UUID
    total_ibu_per_kg: float
    total_ibu_per_kg: float
    fermentable_id: uuid.UUID

    class Config:
        from_attributes = True
