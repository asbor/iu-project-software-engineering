from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime


class MashStepCreate(BaseModel):
    """
    Mash step creation schema

    Attributes:
        name (str): The name of the mash step.
        type (str): The type of the mash step (e.g., infusion, decoction).
        step_time (int): The duration of the step in minutes.
        step_temp (int): The temperature of the step in Celsius.
        ramp_time (Optional[int]): The ramp time in minutes (optional).
        end_temp (Optional[int]): The target temperature of the step (optional).
        description (Optional[str]): Additional description of the step (optional).
        display_step_time (str): Formatted duration of the step.
        display_step_temp (str): Formatted temperature of the step.
    """
    name: str
    type: str
    step_time: int
    step_temp: int
    ramp_time: Optional[int] = None
    end_temp: Optional[int] = None
    description: Optional[str] = None
    display_step_time: str
    display_step_temp: str


class MashCreate(BaseModel):
    """
    Mash creation schema

    Attributes:
        id (uuid.UUID): The unique identifier for the mash.
        created_at (datetime): The timestamp when the mash was created.
        updated_at (datetime): The timestamp when the mash was last updated.
        name (str): The name of the mash.
        version (int): The version number of the mash.
        grain_temp (int): The temperature of the grain in Celsius.
        tun_temp (int): The temperature of the mash tun in Celsius.
        sparge_temp (int): The temperature of the sparge water in Celsius.
        ph (int): The pH of the mash.
        tun_weight (int): The weight of the mash tun in kilograms.
        tun_specific_heat (int): The specific heat of the mash tun.
        equip_adjust (bool): Whether to adjust the equipment.
        notes (Optional[str]): Additional notes about the mash (optional).
        display_grain_temp (str): Formatted temperature of the grain.
        display_tun_temp (str): Formatted temperature of the mash tun.
        display_sparge_temp (str): Formatted temperature of the sparge water.
        display_tun_weight (str): Formatted weight of the mash tun.
        mash_steps (Optional[List[MashStepCreate]]): List of mash steps (optional).
        recipe_id (uuid.UUID): The unique identifier for the recipe.
        recipe (str): Relationship to the Recipe table.
    """
    name: str
    version: int
    grain_temp: int
    tun_temp: int
    sparge_temp: int
    ph: int
    tun_weight: int
    tun_specific_heat: int
    # equip_adjust: bool
    notes: Optional[str] = None
    display_grain_temp: str
    display_tun_temp: str
    display_sparge_temp: str
    display_tun_weight: str
    # mash_steps: Optional[List[MashStepCreate]] = None
    # recipe_id: uuid.UUID
    # recipe: str
