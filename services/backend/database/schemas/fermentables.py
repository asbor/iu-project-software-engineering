from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Fermentables(BaseModel):
    """
    Fermentables model

    Attributes:
        id (UUID): The unique identifier for the fermentables.
        created_at (DateTime): The timestamp when the fermentables were created.
        updated_at (DateTime): The timestamp when the fermentables were last updated.
        name (str): The name of the fermentables.
        version (int): The version number of the fermentables.
        type (str): The type of fermentables.
        amount (int): The amount of fermentables used.
        yield_ (int): The yield of the fermentables.
        color (int): The color of the fermentables.
        add_after_boil (bool): Whether to add the fermentables after the boil.
        origin (str): The origin of the fermentables.
        supplier (str): The supplier of the fermentables.
        notes (str): Additional notes about the fermentables.
        coarse_fine_diff (int): The difference between coarse and fine grind of the fermentables.
        moisture (int): The moisture content of the fermentables.
        diastatic_power (int): The diastatic power of the fermentables.
        protein (int): The protein content of the fermentables.
        max_in_batch (int): The maximum amount of fermentables in a batch.
        recommend_mash (bool): Whether to recommend mashing the fermentables.
        ibu_gal_per_lb (int): The IBU per gallon per pound of fermentables.
        display_amount (str): Formatted amount of fermentables.
        inventory (int): The amount of fermentables in inventory.
        potential (int): The potential of the fermentables.
        display_color (str): Formatted color of the fermentables.
        recipes_id (UUID): The unique identifier for the recipes.
        recipes (relationship): Relationship to the Recipes table.
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
    recipes_id: uuid.UUID
    recipes: List[uuid.UUID]

    class Config:
        orm_mode = True
