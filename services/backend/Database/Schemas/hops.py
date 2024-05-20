from pydantic import BaseModel
from typing import Optional


class MasterHopBase(BaseModel):
    name: str
    origin: Optional[str]
    alpha: Optional[float]
    type: Optional[str]
    form: Optional[str]
    beta: Optional[float]
    hsi: Optional[float]

    class Config:
        orm_mode = True


class RecipeHopBase(BaseModel):
    amount: float
    use: Optional[str]
    time: Optional[int]
    notes: Optional[str]
    display_amount: Optional[str]
    inventory: Optional[float]
    display_time: Optional[str]
    # No master_hop_id here since it's backend responsibility

    class Config:
        orm_mode = True


class HopInput(MasterHopBase, RecipeHopBase):
    pass
