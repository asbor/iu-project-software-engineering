from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


class DryExtractBase(BaseModel):
    """
    Dry Extract model

    Attributes:
        id : The unique identifier for the dry extract.

    Relationships:
        fermentable_id : The fermentable relationship.
    """

    total_ibu_per_kg: float
