from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .batch_logs import BatchLog


class BatchBase(BaseModel):
    batch_name: str
    batch_number: int
    batch_size: float
    brewer: str
    brew_date: datetime


class BatchCreate(BatchBase):
    recipe_id: int


class Batch(BatchBase):
    id: int
    created_at: datetime
    updated_at: datetime
    batch_log: Optional[BatchLog]

    class Config:
        from_attributes = True
