import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class Style(Base):
    """
    Represents the style table in the database.

    Attributes:
        id (UUID): The unique identifier for the style.
        name (str): The name of the style.
        category (str): The category of the style.
        color (str): The color of the style.
        clarity (str): The clarity of the style.
        perceived_malt_and_aroma (str): The perceived malt and aroma of the style.
        perceived_hop_and_aroma (str): The perceived hop and aroma of the style.
        perceived_bitterness (str): The perceived bitterness of the style.
        fermentation_characteristics (str): The fermentation characteristics of the style.
        body (str): The body of the style.
        additional_notes (str): Additional notes about the style.
        og (str): The original gravity of the style.
        fg (str): The final gravity of the style.
        abv (str): The alcohol by volume of the style.
        ibu (str): The international bitterness units of the style.
        ebc (str): The European Brewery Convention of the style.
        og_min (int): The minimum original gravity of the style.
        og_max (int): The maximum original gravity of the style.
        fg_min (int): The minimum final gravity of the style.
        fg_max (int): The maximum final gravity of the style.
        ibu_min (int): The minimum international bitterness units of the style.
        ibu_max (int): The maximum international bitterness units of the style.
        ebc_min (int): The minimum European Brewery Convention of the style.
        ebc_max (int): The maximum European Brewery Convention of the style.
        recipe_id (UUID): The unique identifier for the recipe.
    """
    __tablename__ = "style"
    id = Column(Integer, nullable=True, primary_key=True)
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
    # recipe_id = Column(UUID(as_uuid=True), ForeignKey('recipe.id'))
    # recipe = relationship("Recipe", back_populates="style")

    def __repr__(self):
        return f"Style(id={self.id}, \
            name={self.name}, \
            category={self.category}, \
            color={self.color}, \
            clarity={self.clarity}, \
            perceived_malt_and_aroma={self.perceived_malt_and_aroma}, \
            perceived_hop_and_aroma={self.perceived_hop_and_aroma}, \
            perceived_bitterness={self.perceived_bitterness}, \
            fermentation_characteristics={self.fermentation_characteristics}, \
            body={self.body}, \
            additional_notes={self.additional_notes}, \
            og={self.og}, \
            fg={self.fg}, \
            abv={self.abv}, \
            ibu={self.ibu}, \
            ebc={self.ebc})"
