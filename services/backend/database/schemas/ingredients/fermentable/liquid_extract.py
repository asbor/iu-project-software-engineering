from ...base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class LiquidExtract(BaseModel):
    """
    Liquid Extract model

    Attributes:
        id (UUID): The unique identifier for the liquid extract.

    Relationships:
        fermentable_id (uuid): The fermentable relationship.
    """

    id: uuid.UUID
    total_ibu_per_kg: float
    fermentable_id: uuid.UUID

    class Config:
        orm_mode = True
