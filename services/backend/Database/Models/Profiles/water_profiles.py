from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base


class WaterProfiles(Base):
    """
    Description:
    This class represents the WaterProfile table in the database.
    The water profile NAME needs to be unique.

    Relationships:
    - ONE water_profile can have ZERO or MANY recipes
    TODO: - ONE water_profile can have ZERO or MANY batches
    """

    __tablename__ = "water"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    version = Column(Integer, nullable=True)
    amount = Column(Integer, nullable=True)
    calcium = Column(Integer, nullable=True)
    bicarbonate = Column(Integer, nullable=True)
    sulfate = Column(Integer, nullable=True)
    chloride = Column(Integer, nullable=True)
    sodium = Column(Integer, nullable=True)
    magnesium = Column(Integer, nullable=True)
    ph = Column(Integer, nullable=True)
    notes = Column(String(255), nullable=True)
    display_amount = Column(String(255), nullable=True)
    inventory = Column(Integer, nullable=True)

    # Relationships
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    # TODO: batch_id = Column(Integer, ForeignKey('batches.id'))
