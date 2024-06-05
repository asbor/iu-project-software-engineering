from pydantic import BaseModel
from typing import Optional


class MashProfileBase(BaseModel):
    """
    Description:

    This class represents the MashProfile table in the database.

    Use cases:

    - Validate the data of a new MashProfile object

    - Validate the data of a MashProfile object to be updated

    Notes:

    - The id field is not included in the base model because it is generated
    by the database

    """

    name: Optional[str]
    version: Optional[int]
    grain_temp: Optional[int]
    tun_temp: Optional[int]
    sparge_temp: Optional[int]
    ph: Optional[int]
    tun_weight: Optional[int]
    tun_specific_heat: Optional[int]
    # equip_adjust: bool

    notes: Optional[str]
    display_grain_temp: Optional[str]
    display_tun_temp: Optional[str]
    display_sparge_temp: Optional[str]
    display_tun_weight: Optional[str]
