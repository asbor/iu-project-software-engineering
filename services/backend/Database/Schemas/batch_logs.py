from pydantic import BaseModel

from datetime import datetime


class BatchLogBase(BaseModel):

    log_entry: str


class BatchLogCreate(BatchLogBase):

    batch_id: int


class BatchLog(BatchLogBase):

    id: int

    created_at: datetime

    class Config:

        from_attributes = True
