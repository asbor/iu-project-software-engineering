from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Author(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class User(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    surname: str
    email: str
    birth_date: date
    personal_identificator: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Recipes(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    created_at: datetime
    updated_at: datetime
    name: str
    version: str
    type: str
    brewer: str
    asst_brewer: str
    batch_size: float
    boil_size: float
    boil_time: float
    efficiency: float
    hops: List[str]
    fermentables: List[str]
    miscs: List[str]
    yeasts: List[str]
    waters: List[str]
    style: str
    equipment: str
    mash: str
    notes: str
    taste_notes: str
    taste_rating: int
    og: float
    fg: float
    fermentation_stages: int
    primary_age: int
    primary_temp: float
    secondary_age: int
    secondary_temp: float
    tertiary_age: int
    tertiary_temp: float
    age: int
    age_temp: float
    carbonation_used: str
    date: date
    est_og: float
    est_fg: float
    est_color: float
    ibu: float
    ibu_method: str
    est_abv: float
    abv: float
    actual_efficiency: float
    calories: float
    display_boil_size: float
    display_batch_size: float
    display_og: float
    display_fg: float
    display_primary_temp: float
    display_secondary_temp: float
    display_tertiary_temp: float
    display_age_temp: float

    class Config:
        orm_mode = True
