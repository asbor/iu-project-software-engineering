from pydantic import BaseModel
from typing import Optional


class WaterProfileBase(BaseModel):
    """
    Description:
    This class represents the water_profile table in the database.

    Use cases:
    - Validate data before entering it into the database.

    Notes:
    - the id field is optional because it is generated by the database.
    """

    name: Optional[str]
    version: Optional[int]
    amount: Optional[int]
    calcium: Optional[int]
    bicarbonate: Optional[int]
    sulfate: Optional[int]
    chloride: Optional[int]
    sodium: Optional[int]
    magnesium: Optional[int]
    ph: Optional[int]
    notes: Optional[str]
    display_amount: Optional[str]
    inventory: Optional[int]
