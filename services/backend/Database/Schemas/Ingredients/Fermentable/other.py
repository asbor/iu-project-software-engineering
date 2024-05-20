from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


class OtherBase(BaseModel):
    """
    Other model

    Attributes:
        id : The unique identifier for the other.
        total_ibu_per_kg (decimal): The total IBU per kg of the other.

    Relationships:
        fermentable_id : The fermentable relationship.
    """

    total_ibu_per_kg: float
    total_ibu_per_kg: float
