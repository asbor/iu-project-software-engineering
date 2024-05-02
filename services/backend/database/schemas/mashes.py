from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Mashes(BaseModel):
    """
        Represents the mashes table in the database.

        Attributes:
            id (UUID): The unique identifier for the mashes.
            created_at (DateTime): The timestamp when the mashes were created.
            updated_at (DateTime): The timestamp when the mashes were last updated.
            name (str): The name of the mashes.
            version (int): The version number of the mashes.
            grain_temp (int): The temperature of the grain in Celsius.
            tun_temp (int): The temperature of the mash tun in Celsius.
            sparge_temp (int): The temperature of the sparge water in Celsius.
            ph (int): The pH of the mashes.
            tun_weight (int): The weight of the mash tun in kilograms.
            tun_specific_heat (int): The specific heat of the mash tun.
            equip_adjust (bool): Whether to adjust the equipment.
            notes (str): Additional notes about the mashes.
            display_grain_temp (str): Formatted temperature of the grain.
            display_tun_temp (str): Formatted temperature of the mash tun.
            display_sparge_temp (str): Formatted temperature of the sparge water.
            display_tun_weight (str): Formatted weight of the mash tun.
            mash_steps (relationship): Relationship to the MashStep table.
            recipes_id (UUID): The unique identifier for the recipes.
            recipes (relationship): Relationship to the Recipes table.
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
    equip_adjust: bool
    notes: str
    display_grain_temp: str
    display_tun_temp: str
    display_sparge_temp: str
    display_tun_weight: str
    mash_steps: List[uuid.UUID]
    recipes_id: uuid.UUID
    recipes: List[uuid.UUID]

    class Config:
        orm_mode = True
