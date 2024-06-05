from pydantic import BaseModel

from datetime import datetime

from typing import Optional, List

from .batch_logs import BatchLog

from .hops import InventoryHop

from .fermentables import InventoryFermentable

from .miscs import InventoryMisc

from .yeasts import InventoryYeast





class BatchBase(BaseModel):

    batch_name: str

    batch_number: int

    batch_size: float

    brewer: str

    brew_date: datetime





class BatchCreate(BatchBase):

    recipe_id: int





class BatchUpdate(BaseModel):

    batch_name: Optional[str]

    batch_number: Optional[int]

    batch_size: Optional[float]

    brewer: Optional[str]

    brew_date: Optional[datetime]





class Batch(BatchBase):

    id: int

    created_at: datetime

    updated_at: datetime

    batch_log: Optional[BatchLog]

    inventory_hops: List[InventoryHop]

    inventory_fermentables: List[InventoryFermentable]

    inventory_miscs: List[InventoryMisc]

    inventory_yeasts: List[InventoryYeast]



    class Config:

        orm_mode = True
