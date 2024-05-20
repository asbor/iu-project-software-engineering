from pydantic import BaseModel
from typing import Optional


class HopBase(BaseModel):
    name: str
    origin: Optional[str] = None
    alpha: Optional[float] = None
    type: Optional[str] = None
    form: Optional[str] = None
    beta: Optional[float] = None
    hsi: Optional[float] = None
    amount: Optional[float] = None
    use: Optional[str] = None
    time: Optional[int] = None
    notes: Optional[str] = None
    display_amount: Optional[str] = None
    inventory: Optional[str] = None
    display_time: Optional[str] = None

    # class Config:
    #    from_attributes = True  # Use from_attributes for Pydantic v2
