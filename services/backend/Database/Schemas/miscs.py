from pydantic import BaseModel
from typing import Optional


class MasterMiscBase(BaseModel):
    name: str
    type: Optional[str]
    use: Optional[str]
    notes: Optional[str]

    class Config:
        orm_mode = True


class RecipeMiscBase(BaseModel):
    master_misc_id: Optional[int] = None
    amount: float
    time: Optional[int]
    amount_is_weight: Optional[bool]
    use_for: Optional[str]
    display_amount: Optional[str]
    inventory: Optional[float]
    display_time: Optional[str]
    batch_size: Optional[float]

    class Config:
        orm_mode = True
