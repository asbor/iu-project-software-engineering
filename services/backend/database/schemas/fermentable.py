from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Fermentable(BaseModel):
    """
    Fermentable model

    Attributes:
        id (UUID): The unique identifier for the fermentable.
        created_at (DateTime): The timestamp when the fermentable was created.
        updated_at (DateTime): The timestamp when the fermentable was last updated.
        name (str): The name of the fermentable.
        version (int): The version number of the fermentable.
        type (str): The type of fermentable.
        amount (int): The amount of fermentable used.
        yield_ (int): The yield of the fermentable.
        color (int): The color of the fermentable.
        add_after_boil (bool): Whether to add the fermentable after the boil.
        origin (str): The origin of the fermentable.
        supplier (str): The supplier of the fermentable.
        notes (str): Additional notes about the fermentable.
        coarse_fine_diff (int): The difference between coarse and fine grind of the fermentable.
        moisture (int): The moisture content of the fermentable.
        diastatic_power (int): The diastatic power of the fermentable.
        protein (int): The protein content of the fermentable.
        max_in_batch (int): The maximum amount of fermentable in a batch.
        recommend_mash (bool): Whether to recommend mashing the fermentable.
        ibu_gal_per_lb (int): The IBU per gallon per pound of fermentable.
        display_amount (str): Formatted amount of fermentable.
        inventory (int): The amount of fermentable in inventory.
        potential (int): The potential of the fermentable.
        display_color (str): Formatted color of the fermentable.
        recipe_id (UUID): The unique identifier for the recipe.
        recipe (relationship): Relationship to the Recipe table.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    type: str
    amount: int
    yield_: int
    color: int
    add_after_boil: bool
    origin: str
    supplier: str
    notes: str
    coarse_fine_diff: int
    moisture: int
    diastatic_power: int
    protein: int
    max_in_batch: int
    recommend_mash: bool
    ibu_gal_per_lb: int
    display_amount: str
    inventory: int
    potential: int
    display_color: str

    class Config:
        orm_mode = True
