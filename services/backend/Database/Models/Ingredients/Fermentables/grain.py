from sqlalchemy import Column, Integer, Float, ForeignKey
from database import Base

class RecipeGrain(Base):
    """
    Recipe-specific Grain table.

    """

    __tablename__ = "recipe_grain"
    id = Column(Integer, primary_key=True, index=True)
    diastatic_power = Column(Float, nullable=True)
    moisture = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    coarse_fine_diff = Column(Float, nullable=True)
    extract = Column(Float, nullable=True)
    acidity = Column(Float, nullable=True)
    friability = Column(Float, nullable=True)
    free_amino_nitrogen = Column(Float, nullable=True)
    max_in_batch = Column(Float, nullable=True)
    fermentable_id = Column(Integer, ForeignKey("recipe_fermentables.id"))

class InventoryGrain(Base):
    """
    Inventory-specific Grain table.

    """

    __tablename__ = "inventory_grain"
    id = Column(Integer, primary_key=True, index=True)
    diastatic_power = Column(Float, nullable=True)
    moisture = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    coarse_fine_diff = Column(Float, nullable=True)
    extract = Column(Float, nullable=True)
    acidity = Column(Float, nullable=True)
    friability = Column(Float, nullable=True)
    free_amino_nitrogen = Column(Float, nullable=True)
    max_in_batch = Column(Float, nullable=True)
    fermentable_id = Column(Integer, ForeignKey("inventory_fermentables.id"))
