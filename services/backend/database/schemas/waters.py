from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Waters(BaseModel):
    """
    Represents the waters table in the database.

    Attributes:
        id (UUID): The unique identifier for the waters.
        created_at (DateTime): The timestamp when the waters were created.
        updated_at (DateTime): The timestamp when the waters were last updated.
        name (str): The name of the waters.
        version (int): The version number of the waters.
        amount (int): The amount of the waters.
        calcium (int): The calcium of the waters.
        bicarbonate (int): The bicarbonate of the waters.
        sulfate (int): The sulfate of the waters.
        chloride (int): The chloride of the waters.
        sodium (int): The sodium of the waters.
        magnesium (int): The magnesium of the waters.
        ph (int): The pH of the waters.
        notes (str): Additional notes about the waters.
        display_amount (str): Formatted amount of the waters.
        inventory (int): The inventory of the waters.
        recipes_id (UUID): The unique identifier for the recipes.
        recipes (relationship): Relationship to the Recipes table.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    amount: int
    calcium: int
    bicarbonate: int
    sulfate: int
    chloride: int
    sodium: int
    magnesium: int
    ph: int
    notes: str
    display_amount: str
    inventory: int
    recipes_id: uuid.UUID
    recipes: List[uuid.UUID]

    class Config:
        orm_mode = True
