from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Equipments(BaseModel):
    """
    Equipments schema

    Attributes:
        id (UUID): The unique identifier for the equipment.
        created_at (DateTime): The timestamp when the equipment was created.
        updated_at (DateTime): The timestamp when the equipment was last updated.
        name (str): The name of the equipment.
        version (int): The version number of the equipment.
        boil_size (int): The size of the boil in liters.
        batch_size (int): The size of the batch in liters.
        tun_volume (int): The volume of the mash tun in liters.
        tun_weight (int): The weight of the mash tun in kilograms.
        tun_specific_heat (int): The specific heat of the mash tun.
        top_up_water (int): The amount of top-up water in liters.
        trub_chiller_loss (int): The loss due to trub and chiller in liters.
        evap_rate (int): The evaporation rate as a percentage.
        boil_time (int): The duration of the boil in minutes.
        calc_boil_volume (bool): Whether to calculate the boil volume.
        lauter_deadspace (int): The dead space in the lauter tun in liters.
        top_up_kettle (int): The amount of top-up water in the kettle in liters.
        hop_utilization (int): The hop utilization as a percentage.
        notes (str): Additional notes about the equipment.
        display_boil_size (str): Formatted size of the boil.
        display_batch_size (str): Formatted size of the batch.
        display_tun_volume (str): Formatted volume of the mash tun.
        display_tun_weight (str): Formatted weight of the mash tun.
        display_top_up_water (str): Formatted amount of top-up water.
        display_trub_chiller_loss (str): Formatted loss due to trub and chiller.
        display_lauter_deadspace (str): Formatted dead space in the lauter tun.
        display_top_up_kettle (str): Formatted amount of top-up water in the kettle.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    boil_size: int
    batch_size: int
    tun_volume: int
    tun_weight: int
    tun_specific_heat: int
    top_up_water: int
    trub_chiller_loss: int
    evap_rate: int
    boil_time: int
    calc_boil_volume: bool
    lauter_deadspace: int
    top_up_kettle: int
    hop_utilization: int
    notes: str
    display_boil_size: str
    display_batch_size: str
    display_tun_volume: str
    display_tun_weight: str
    display_top_up_water: str
    display_trub_chiller_loss: str
    display_lauter_deadspace: str
    display_top_up_kettle: str
    recipes: List[uuid.UUID]

    class Config:
        orm_mode = True
