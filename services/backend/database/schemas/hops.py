from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Hops(BaseModel):
    """
    Hops schema

    Attributes:
        id (UUID): The unique identifier for the hops.
        created_at (DateTime): The timestamp when the hops were created.
        updated_at (DateTime): The timestamp when the hops were last updated.
        name (str): The name of the hops.
        version (int): The version number of the hops.
        origin (str): The origin of the hops.
        alpha (int): The alpha acid content of the hops.
        amount (int): The amount of hops used.
        use (str): The usage of the hops.
        time (int): The time the hops are added.
        notes (str): Additional notes about the hops.
        type (str): The type of hops.
        form (str): The form of the hops.
        beta (int): The beta acid content of the hops.
        hsi (int): The hop stability index of the hops.
        display_amount (str): Formatted amount of hops.
        inventory (int): The amount of hops in inventory.
        display_time (str): Formatted time the hops are added.
        recipes (relationship): Relationship to the Recipes table.
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
    recipes: List[uuid.UUID]

    class Config:
        orm_mode = True
