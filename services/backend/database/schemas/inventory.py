from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Inventory(BaseModel):

    """
    Inventory model

    Attributes:
        id (UUID): The unique identifier for the inventory.
        stock (decimal): The stock of the inventory.
        cost_per_unit (decimal): The cost per unit of the inventory.
        eng_units (string): The energy units of the inventory.

    Relationships:
        fermentable_id (uuid): [adjuncts, dry_extracts, grains, liquid_extracts, other, sugars] The fermentable relationship.
        hop_id (uuid): [hops] The hop relationship.
        yeast_id (uuid): [yeast] The yeast relationship.
        misc_id (uuid): [miscs] The misc relationship.
    """

    id: uuid.UUID
    stock: float
    cost_per_unit: float
    eng_units: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
