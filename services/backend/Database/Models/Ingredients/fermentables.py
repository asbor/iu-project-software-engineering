# Database/Models/Ingredients/fermentables.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import relationship
from database import Base


class RecipeFermentable(Base):
    __tablename__ = "recipe_fermentables"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
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
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    recipe = relationship("Recipes", back_populates="fermentables")


class InventoryFermentable(Base):
    __tablename__ = "inventory_fermentables"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
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
    alpha = Column(Float, nullable=True)
    beta = Column(Float, nullable=True)
    form = Column(String, nullable=True)
    use = Column(String, nullable=True)
    amount_is_weight = Column(Boolean, nullable=True)
    product_id = Column(String, nullable=True)
    min_temperature = Column(Float, nullable=True)
    max_temperature = Column(Float, nullable=True)
    flocculation = Column(String, nullable=True)
    attenuation = Column(Float, nullable=True)
    max_reuse = Column(Integer, nullable=True)
    inventory = Column(Float, nullable=True)
    display_amount = Column(String, nullable=True)
    display_time = Column(String, nullable=True)
    batch_size = Column(Float, nullable=True)
    batch_id = Column(Integer, ForeignKey("batches.id"), nullable=True)
    batch = relationship("Batches", back_populates="inventory_fermentables")
