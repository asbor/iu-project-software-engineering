from pydantic import BaseModel

from typing import Optional





class HopBase(BaseModel):

    name: str

    origin: Optional[str]

    alpha: Optional[float]

    type: Optional[str]

    form: Optional[str]

    beta: Optional[float]

    hsi: Optional[float]

    amount: Optional[float]

    use: Optional[str]

    time: Optional[int]

    notes: Optional[str]

    display_amount: Optional[str]

    inventory: Optional[str]

    display_time: Optional[str]





class RecipeHop(HopBase):

    recipe_id: int



    class Config:

        orm_mode: bool = True





class InventoryHopBase(HopBase):

    pass





class InventoryHopCreate(InventoryHopBase):

    pass





class InventoryHop(InventoryHopBase):

    id: int

    batch_id: Optional[int] = None  # Allow batch_id to be None



    class Config:

        orm_mode: bool = True
