# Database/Schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BatchBase(BaseModel):
    recipe_id: int
    batch_name: str
    batch_size: float

    class Config:
        orm_mode = True
