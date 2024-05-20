from pydantic import BaseModel
from typing import Optional


class MasterFermentableBase(BaseModel):
    name: str
    type: Optional[str]
    yield_: Optional[float]
    color: Optional[int]
    origin: Optional[str]
    supplier: Optional[str]
    notes: Optional[str]
    potential: Optional[int]

    class Config:
        orm_mode = True


class RecipeFermentableBase(BaseModel):
    master_fermentable_id: Optional[int] = None
    amount: float
    cost_per_unit: Optional[float]
    manufacturing_date: Optional[str]
    expiry_date: Optional[str]
    lot_number: Optional[str]
    exclude_from_total: Optional[bool]
    not_fermentable: Optional[bool]
    description: Optional[str]
    substitutes: Optional[str]
    used_in: Optional[str]

    class Config:
        orm_mode = True
