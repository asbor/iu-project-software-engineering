# Database/Schemas/fermentables.py

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
    recipe_id: int

    class Config:
        orm_mode: bool = True


class InventoryFermentableBase(FermentableBase):
    alpha: Optional[float] = None  # Specific to hops
    beta: Optional[float] = None  # Specific to hops
    form: Optional[str] = None  # Specific to hops
    use: Optional[str] = None  # Specific to hops and miscs
    amount_is_weight: Optional[bool] = None  # Specific to miscs and yeasts
    product_id: Optional[str] = None  # Specific to yeasts
    min_temperature: Optional[float] = None  # Specific to yeasts
    max_temperature: Optional[float] = None  # Specific to yeasts
    flocculation: Optional[str] = None  # Specific to yeasts
    attenuation: Optional[float] = None  # Specific to yeasts
    max_reuse: Optional[int] = None  # Specific to yeasts
    inventory: Optional[float] = None  # Specific to all
    display_amount: Optional[str] = None  # Specific to all
    display_time: Optional[str] = None  # Specific to all
    batch_size: Optional[float] = None  # Specific to miscs


class InventoryFermentableCreate(InventoryFermentableBase):
    pass


class InventoryFermentable(InventoryFermentableBase):
    id: int
    batch_id: Optional[int] = None  # Allow batch_id to be None

    class Config:
        orm_mode: bool = True
