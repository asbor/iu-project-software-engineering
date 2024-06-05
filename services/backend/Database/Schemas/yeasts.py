from pydantic import BaseModel
from typing import Optional


class YeastBase(BaseModel):
    name: str
    type: Optional[str]
    form: Optional[str]
    amount: Optional[float]
    amount_is_weight: Optional[bool]
    laboratory: Optional[str]
    product_id: Optional[str]
    min_temperature: Optional[float]
    max_temperature: Optional[float]
    flocculation: Optional[str]
    attenuation: Optional[float]
    notes: Optional[str]
    best_for: Optional[str]
    times_cultured: Optional[int]
    max_reuse: Optional[int]
    add_to_secondary: Optional[bool]


class RecipeYeast(YeastBase):
    recipe_id: int

    class Config:
        orm_mode: bool = True


class InventoryYeastBase(YeastBase):
    pass


class InventoryYeastCreate(InventoryYeastBase):
    pass


class InventoryYeast(InventoryYeastBase):
    id: int
    batch_id: Optional[int] = None  # Allow batch_id to be None

    class Config:
        orm_mode: bool = True
