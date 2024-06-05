from pydantic import BaseModel
from typing import Optional


class EquipmentProfileBase(BaseModel):
    """
    Description:

    This class represents the EquipmentProfile table in the database.

    Use cases:

    - Validate the data of a new EquipmentProfile object

    - Validate the data of a EquipmentProfile object to be updated

    Notes:

    - The id field is not included in the base model because it is generated
    by the database

    """

    name: Optional[str]
    version: Optional[int]
    boil_size: Optional[int]
    batch_size: Optional[int]
    tun_volume: Optional[int]
    tun_weight: Optional[int]
    tun_specific_heat: Optional[int]
    top_up_water: Optional[int]
    trub_chiller_loss: Optional[int]
    evap_rate: Optional[int]
    boil_time: Optional[int]
    calc_boil_volume: bool
    lauter_deadspace: Optional[int]
    top_up_kettle: Optional[int]
    hop_utilization: Optional[int]
    notes: Optional[str]
    display_boil_size: Optional[str]
    display_batch_size: Optional[str]
    display_tun_volume: Optional[str]
    display_tun_weight: Optional[str]
    display_top_up_water: Optional[str]
    display_trub_chiller_loss: Optional[str]
    display_lauter_deadspace: Optional[str]
    display_top_up_kettle: Optional[str]
