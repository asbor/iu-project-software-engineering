from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Water(BaseModel):
    """
    Represents the water table in the database.

    Attributes:
        id (UUID): The unique identifier for the water.
        created_at (DateTime): The timestamp when the water were created.
        updated_at (DateTime): The timestamp when the water were last updated.
        name (str): The name of the water.
        version (int): The version number of the water.
        amount (int): The amount of the water.
        calcium (int): The calcium of the water.
        bicarbonate (int): The bicarbonate of the water.
        sulfate (int): The sulfate of the water.
        chloride (int): The chloride of the water.
        sodium (int): The sodium of the water.
        magnesium (int): The magnesium of the water.
        ph (int): The pH of the water.
        notes (str): Additional notes about the water.
        display_amount (str): Formatted amount of the water.
        inventory (int): The inventory of the water.
        recipe_id (UUID): The unique identifier for the recipe.
        recipe (relationship): Relationship to the Recipe table.
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
    recipe_id: uuid.UUID
    recipe: List[uuid.UUID]

    class Config:
        from_attributes = True
