from pydantic import BaseModel
from typing import Optional, List


class StyleGuidelineBase(BaseModel):
    """
    Description:
    This class represents the style guidelines provided by the BJCP.

    Use cases:
    - Validate the data of a new Style object
    - Validate the data of a Style object to be updated
    """
    block_heading: str
    circle_image: str
    category: str
    color: Optional[str]
    clarity: Optional[str]
    perceived_malt_and_aroma: Optional[str]
    perceived_hop_and_aroma: Optional[str]
    perceived_bitterness: Optional[str]
    fermentation_characteristics: Optional[str]
    body: Optional[str]
    additional_notes: Optional[str]

    # Vitals
    og: Optional[str]
    fg: Optional[str]
    abv: Optional[str]
    ibu: Optional[str]
    ebc: Optional[str]

    # Calculated
