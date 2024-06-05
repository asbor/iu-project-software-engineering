from pydantic import BaseModel

from typing import Optional





class StyleGuidelineBase(BaseModel):

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

    og: Optional[str]

    fg: Optional[str]

    abv: Optional[str]

    ibu: Optional[str]

    ebc: Optional[str]





class StyleGuidelineBaseCreate(StyleGuidelineBase):

    pass
