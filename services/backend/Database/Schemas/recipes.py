from pydantic import BaseModel
from typing import Optional, List
from .hops import HopInput


class RecipeBase(BaseModel):
    name: str
    version: int
    type: Optional[str]
    brewer: Optional[str]
    asst_brewer: Optional[str]
    batch_size: Optional[float]
    boil_size: Optional[float]
    boil_time: Optional[int]
    efficiency: Optional[float]
    notes: Optional[str]
    taste_notes: Optional[str]
    taste_rating: Optional[int]
    og: Optional[float]
    fg: Optional[float]
    fermentation_stages: Optional[int]
    primary_age: Optional[int]
    primary_temp: Optional[float]
    secondary_age: Optional[int]
    secondary_temp: Optional[float]
    tertiary_age: Optional[int]
    age: Optional[int]
    age_temp: Optional[float]
    carbonation_used: Optional[str]
    est_og: Optional[float]
    est_fg: Optional[float]
    est_color: Optional[float]
    ibu: Optional[float]
    ibu_method: Optional[str]
    est_abv: Optional[float]
    abv: Optional[float]
    actual_efficiency: Optional[float]
    calories: Optional[float]
    display_batch_size: Optional[str]
    display_boil_size: Optional[str]
    display_og: Optional[str]
    display_fg: Optional[str]
    display_primary_temp: Optional[str]
    display_secondary_temp: Optional[str]
    display_tertiary_temp: Optional[str]
    display_age_temp: Optional[str]

    hops: Optional[List[HopInput]] = None

    class Config:
        orm_mode = True
