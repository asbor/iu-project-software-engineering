from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Hop(BaseModel):
    """
    A class representing the Hop table in the database.

    This table stores information about hop used in brewing recipe, including details about
    the origin, alpha acid content, and usage.

    Attributes:
        id (UUID): The unique identifier for the hop.
        created_at (DateTime): The timestamp when the hop was created.
        updated_at (DateTime): The timestamp when the hop was last updated.
        name (str): The name of the hop.
        version (int): The version number of the hop.
        origin (str): The origin of the hop.
        alpha (int): The alpha acid content of the hop.
        amount (int): The amount of hop used.
        use (str): The usage of the hop.
        time (int): The time the hop is added.
        notes (str): Additional notes about the hop.
        type (str): The type of hop.
        form (str): The form of the hop.
        beta (int): The beta acid content of the hop.
        hsi (int): The hop stability index of the hop.
        display_amount (str): Formatted amount of hop.
        inventory (int): The amount of hop in inventory.
        display_time (str): Formatted time the hop is added.
        recipe (relationship): Relationship to the Recipe table.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    origin: str
    alpha: int
    amount: int
    use: str
    time: int
    notes: str
    type: str
    form: str
    beta: int
    hsi: int
    display_amount: str
    inventory: int
    display_time: str

    class Config:
        orm_mode = True
