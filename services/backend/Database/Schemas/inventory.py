from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


class Inventory(BaseModel):
    """
    Description:
    This class represents the Inventory table in the database.

    Use cases:
    - Validate the data of a new Inventory object
    - Validate the data of a Inventory object to be updated

    Notes:
    - The id field is not included in the base model because it is generated by the database

    """

    stock: Optional[float]
    cost_per_unit: Optional[float]
    eng_units: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]