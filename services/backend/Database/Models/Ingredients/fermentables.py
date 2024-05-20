from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from database import Base
from sqlalchemy.orm import relationship


class Fermentables(Base):
    """
    """

    __tablename__ = "fermentables"

    # Metadata
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True, unique=True)
    type = Column(String, nullable=True)
    yield_ = Column(Float, nullable=True)
    color = Column(Integer, nullable=True)
    origin = Column(String, nullable=True)
    supplier = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    potential = Column(Integer, nullable=True)
    amount = Column(Float, nullable=True)
    cost_per_unit = Column(Float, nullable=True)
    manufacturing_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)
    lot_number = Column(String, nullable=True)
    exclude_from_total = Column(Boolean, nullable=True)
    not_fermentable = Column(Boolean, nullable=True)
    description = Column(String, nullable=True)
    substitutes = Column(String, nullable=True)
    used_in = Column(String, nullable=True)

    # Foreign key to Recipes
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Many-to-one relationship with Recipes
    # recipe = relationship("Recipes", back_populates="fermentables")
