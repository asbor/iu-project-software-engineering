from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Style(BaseModel):
    """
    Represents the style table in the database.

    Attributes:
        id (UUID): The unique identifier for the style.
        created_at (DateTime): The timestamp when the style was created.
        updated_at (DateTime): The timestamp when the style was last updated.
        name (str): The name of the style.
        version (int): The version number of the style.
        category (str): The category of the style.
        category_number (int): The category number of the style.
        style_letter (str): The letter of the style.
        style_guide (str): The guide of the style.
        type (str): The type of the style.
        og_min (int): The minimum original gravity of the style.
        og_max (int): The maximum original gravity of the style.
        fg_min (int): The minimum final gravity of the style.
        fg_max (int): The maximum final gravity of the style.
        ibu_min (int): The minimum IBU of the style.
        ibu_max (int): The maximum IBU of the style.
        color_min (int): The minimum color of the style.
        color_max (int): The maximum color of the style.
        carb_min (int): The minimum carbonation of the style.
        carb_max (int): The maximum carbonation of the style.
        abv_min (int): The minimum ABV of the style.
        abv_max (int): The maximum ABV of the style.
        notes (str): Additional notes about the style.
        profile (str): The profile of the style.
        ingredients (str): The ingredients of the style.
        examples (str): Examples of the style.
        display_og_min (str): Formatted minimum original gravity of the style.
        display_og_max (str): Formatted maximum original gravity of the style.
        display_fg_min (str): Formatted minimum final gravity of the style.
        display_fg_max (str): Formatted maximum final gravity of the style.
        display_color_min (str): Formatted minimum color of the style.
        display_color_max (str): Formatted maximum color of the style.
        og_range (str): The range of original gravity of the style.
        fg_range (str): The range of final gravity of the style.
        ibu_range (str): The range of IBU of the style.
        carb_range (str): The range of carbonation of the style.
        color_range (str): The range of color of the style.
        abv_range (str): The range of ABV of the style.
    """

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    category: str
    category_number: int
    style_letter: str
    style_guide: str
    type: str
    og_min: int
    og_max: int
    fg_min: int
    fg_max: int
    ibu_min: int
    ibu_max: int
    color_min: int
    color_max: int
    carb_min: int
    carb_max: int
    abv_min: int
    abv_max: int
    notes: str
    profile: str
    ingredients: str
    examples: str
    display_og_min: str
    display_og_max: str
    display_fg_min: str
    display_fg_max: str
    display_color_min: str
    display_color_max: str
    og_range: str
    fg_range: str
    ibu_range: str
    carb_range: str
    color_range: str
    abv_range: str

    class Config:
        orm_mode = True
