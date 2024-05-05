from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Yeast(BaseModel):
    """
    Represents the yeast table in the database.

    Attributes:
        id (UUID): The unique identifier for the yeast.
        created_at (DateTime): The timestamp when the yeast was created.
        updated_at (DateTime): The timestamp when the yeast was last updated.
        name (str): The name of the yeast.
        version (int): The version number of the yeast.
        type (str): The type of the yeast.
        form (str): The form of the yeast.
        amount (int): The amount of the yeast.
        amount_is_weight (bool): Whether the amount is weight.
        laboratory (str): The laboratory of the yeast.
        product_id (str): The product ID of the yeast.
        min_temperature (int): The minimum temperature of the yeast.
        max_temperature (int): The maximum temperature of the yeast.
        flocculation (str): The flocculation of the yeast.
        attenuation (int): The attenuation of the yeast.
        notes (str): Additional notes about the yeast.
        best_for (str): The best for of the yeast.
        max_reuse (int): The maximum reuse of the yeast.
        times_cultured (int): The times cultured of the yeast.
        add_to_secondary (bool): Whether to add to secondary.
        display_amount (str): Formatted amount of the yeast.
        display_min_temp (str): Formatted minimum temperature of the yeast.
        display_max_temp (str): Formatted maximum temperature of the yeast.
        inventory (int): The inventory of the yeast.
        culture_date (Date): The culture date of the yeast.
        recipe_id (UUID): The unique identifier for the recipe.
        recipe (relationship): Relationship to the Recipe table.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    type: str
    form: str
    amount: int
    amount_is_weight: bool
    laboratory: str
    product_id: str
    min_temperature: int
    max_temperature: int
    flocculation: str
    attenuation: int
    notes: str
    best_for: str
    max_reuse: int
    times_cultured: int
    add_to_secondary: bool
    display_amount: str
    display_min_temp: str
    display_max_temp: str
    inventory: int
    culture_date: date
    recipe_id: uuid.UUID
    recipe: List["Recipe"]

    def __init__(self, **data):
        super().__init__(**data)
        self.id = uuid.UUID(data["id"])
        self.created_at = datetime.fromisoformat(data["created_at"])
        self.updated_at = datetime.fromisoformat(data["updated_at"])
        self.culture_date = date.fromisoformat(data["culture_date"])
