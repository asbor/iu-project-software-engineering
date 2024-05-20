from pydantic import BaseModel
from typing import Optional


class MasterYeastBase(BaseModel):
    name: str
    type: Optional[str]
    form: Optional[str]
    laboratory: Optional[str]
    product_id: Optional[str]
    min_temperature: Optional[float]
    max_temperature: Optional[float]
    flocculation: Optional[str]
    attenuation: Optional[float]
    notes: Optional[str]
    best_for: Optional[str]
    max_reuse: Optional[int]

    class Config:
        orm_mode = True


class RecipeYeastBase(BaseModel):
    master_yeast_id: Optional[int] = None
    amount: float
    amount_is_weight: Optional[bool]
    inventory: Optional[float]
    display_amount: Optional[str]

    class Config:
        orm_mode = True
