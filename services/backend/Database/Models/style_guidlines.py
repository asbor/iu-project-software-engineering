from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, UUID, Text
from database import Base


class StyleGuidelines(Base):
    """
    Description:
    This class represents the style guidelines provided by the BJCP.

    Relationships:
    - ONE style can have ZERO or MANY recipes
    """

    __tablename__ = "style_guidelines"
    id = Column(Integer, nullable=True, primary_key=True)
    block_heading = Column(String(255), nullable=True)
    circle_image = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)
    color = Column(String(255), nullable=True)
    clarity = Column(String(255), nullable=True)
    perceived_malt_and_aroma = Column(Text, nullable=True)
    perceived_hop_and_aroma = Column(Text, nullable=True)
    perceived_bitterness = Column(Text, nullable=True)
    fermentation_characteristics = Column(Text, nullable=True)
    body = Column(String(255), nullable=True)
    additional_notes = Column(Text, nullable=True)

    # Vitals
    og = Column(String(255), nullable=True)
    fg = Column(String(255), nullable=True)
    abv = Column(String(255), nullable=True)
    ibu = Column(String(255), nullable=True)
    ebc = Column(String(255), nullable=True)

    # Calculated
    # og_min = Column(Integer, nullable=True)
    # og_max = Column(Integer, nullable=True)
    # fg_min = Column(Integer, nullable=True)
    # fg_max = Column(Integer, nullable=True)
    # ibu_min = Column(Integer, nullable=True)
    # ibu_max = Column(Integer, nullable=True)
    # ebc_min = Column(Integer, nullable=True)
    # ebc_max = Column(Integer, nullable=True)

    # Relationships
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
