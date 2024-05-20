from pydantic import BaseModel
from typing import Optional, List


class StyleBase(BaseModel):
    """
    Description:
    This class represents the actual style of a beer.

    Use cases:
    - Validate the data of a new Style object
    - Validate the data of a Style object to be updated
    """

    name: str
    version: int
    category: Optional[str]
    category_number: Optional[int]
    style_letter: Optional[str]
    style_guide: Optional[str]
    type: Optional[str]
    og_min: Optional[str]
    og_max: Optional[str]
    fg_min: Optional[str]
    fg_max: Optional[str]
    ibu_min: Optional[str]
    ibu_max: Optional[str]
    color_min: Optional[str]
    color_max: Optional[str]
    carb_min: Optional[str]
    carb_max: Optional[str]
    abv_max: Optional[str]
    abv_min: Optional[str]
    notes: Optional[str]
    profile: Optional[str]
    ingredients: Optional[str]
    examples: Optional[str]
    display_og_min: Optional[str]
    display_og_max: Optional[str]
    display_fg_min: Optional[str]
    display_fg_max: Optional[str]
    display_color_min: Optional[str]
    display_color_max: Optional[str]
    og_range: Optional[str]
    fg_range: Optional[str]
    ibu_range: Optional[str]
    carb_range: Optional[str]
    color_range: Optional[str]
    abv_range: Optional[str]
