from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Sugar(BaseModel):
    """
    Sugar model

    Attributes:
        id (UUID): The unique identifier for the sugar.

    Relationships:
        fermentable_id (uuid): The fermentable relationship.
    """

    id: uuid.UUID
    total_ibu_per_kg: float
    fermentable_id: uuid.UUID

    class Config:
        from_attributes = True
