# Database/Schemas/recipes_fermentables.py

from pydantic import BaseModel
from typing import Optional
from datetime import date


class FermentableBase(BaseModel):
    name: str
    type: Optional[str]
    yield_: Optional[float]
    color: Optional[int]
    origin: Optional[str]
    supplier: Optional[str]
    notes: Optional[str]
    potential: Optional[int]
    amount: Optional[float]
    cost_per_unit: Optional[float]
    manufacturing_date: Optional[date]
    expiry_date: Optional[date]
    lot_number: Optional[str]
    exclude_from_total: Optional[bool]
    not_fermentable: Optional[bool]
    description: Optional[str]
    substitutes: Optional[str]
    used_in: Optional[str]


class RecipeFermentable(FermentableBase):
    pass


class InventoryFermentable(FermentableBase):
    pass
