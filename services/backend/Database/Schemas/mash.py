
from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Mash(BaseModel):
    """
    Represents the mash table in the database.

    Attributes:
        id (UUID): The unique identifier for the mash.
        created_at (DateTime): The timestamp when the mash was created.
        updated_at (DateTime): The timestamp when the mash was last updated.
        name (str): The name of the mash.
        version (int): The version number of the mash.
        grain_temp (int): The temperature of the grain in Celsius.
        tun_temp (int): The temperature of the mash tun in Celsius.
        sparge_temp (int): The temperature of the sparge water in Celsius.
        ph (int): The pH of the mash.
        tun_weight (int): The weight of the mash tun in kilograms.
        tun_specific_heat (int): The specific heat of the mash tun.
        equip_adjust (bool): Whether to adjust the equipment.
        notes (str): Additional notes about the mash.
        display_grain_temp (str): Formatted temperature of the grain.
        display_tun_temp (str): Formatted temperature of the mash tun.
        display_sparge_temp (str): Formatted temperature of the sparge water.
        display_tun_weight (str): Formatted weight of the mash tun.
        mash_steps (relationship): Relationship to the MashStep table.
        recipe_id (UUID): The unique identifier for the recipe.
        recipe (relationship): Relationship to the Recipe table.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    grain_temp: int
    tun_temp: int
    sparge_temp: int
    ph: int
    tun_weight: int
    tun_specific_heat: int
    # equip_adjust: bool
    notes: str
    display_grain_temp: str
    display_tun_temp: str
    display_sparge_temp: str
    display_tun_weight: str

    class Config:
        from_attributes = True
