from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


class SugarBase(BaseModel):
    """
    Sugar model

    Attributes:
        id : The unique identifier for the sugar.

    Relationships:
        fermentable_id : The fermentable relationship.
    """

    total_ibu_per_kg: float
