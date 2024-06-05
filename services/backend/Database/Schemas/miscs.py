from pydantic import BaseModel

from typing import Optional


class MiscBase(BaseModel):

    name: str

    type: Optional[str]

    use: Optional[str]

    amount_is_weight: Optional[bool]

    use_for: Optional[str]

    notes: Optional[str]

    amount: Optional[int]

    time: Optional[int]

    display_amount: Optional[str]

    inventory: Optional[int]

    display_time: Optional[str]

    batch_size: Optional[int]


class RecipeMisc(MiscBase):

    recipe_id: int

    class Config:

        orm_mode: bool = True


class InventoryMiscBase(MiscBase):

    pass


class InventoryMiscCreate(InventoryMiscBase):

    pass


class InventoryMisc(InventoryMiscBase):

    id: int

    batch_id: Optional[int] = None  # Allow batch_id to be None

    class Config:

        orm_mode: bool = True
