from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Fermentable(BaseModel):
    """
    Fermentable model

    Attributes:
        id (UUID): The unique identifier for the fermentable.
        created_at (datetime): The date and time the fermentable was created.
        updated_at (datetime): The date and time the fermentable was last updated.
        name (str): The name of the fermentable.
        amount (int): The amount of the fermentable in kilograms.
        cost_per_unit (float): The cost per unit in Euros.
        supplier (str): The supplier of the fermentable.
        origin (str): The origin of the fermentable.
        type (str): The type of the fermentable.
        color (int): The color of the fermentable in EBC.
        potential (int): The potential of the fermentable in PPG (Points Per Gallon).
        yield_ (float): The yield of the fermentable as a percentage.
        manufacturing_date (str): The manufacturing date of the fermentable.
        expiry_date (str): The expiry date of the fermentable.
        lot_number (str): The lot number of the fermentable.
        exclude_from_total (bool): Indicates whether to exclude the fermentable from the total.
        not_fermentable (bool): Indicates whether the fermentable is not fermentable.
        notes (str): Additional notes about the fermentable.
        description (str): Description of the fermentable.
        substitutes (str): Substitutes for the fermentable.
        used_in (str): Where the fermentable is used.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    amount: int
    cost_per_unit: float
    supplier: str
    origin: str
    type: str
    color: int
    potential: int
    yield_: float
    manufacturing_date: date
    expiry_date: date
    lot_number: str
    exclude_from_total: bool
    not_fermentable: bool
    notes: str
    description: str
    substitutes: str
    used_in: str

    class Config:
        orm_mode = True
