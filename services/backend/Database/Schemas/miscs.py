from pydantic import BaseModel
from typing import Optional


class MiscBase(BaseModel):
    name: str
    type: Optional[str]
    use: Optional[str]
    amount_is_weight: Optional[bool]
    use_for: Optional[str]
    notes: Optional[str]
    amount: float
    time: Optional[int]
    display_amount: Optional[str]
    inventory: Optional[float]
    display_time: Optional[str]
    batch_size: Optional[float]

    # class Config:
    #    from_attributes = True  # Use from_attributes for Pydantic v2
