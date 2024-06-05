from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class RecipeYeast(Base):
    __tablename__ = "recipe_yeasts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    type = Column(String, nullable=True)
    form = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    amount_is_weight = Column(Boolean, nullable=True)
    laboratory = Column(String, nullable=True)
    product_id = Column(String, nullable=True)
    min_temperature = Column(Float, nullable=True)
    max_temperature = Column(Float, nullable=True)
    flocculation = Column(String, nullable=True)
    attenuation = Column(Float, nullable=True)
    notes = Column(String, nullable=True)
    best_for = Column(String, nullable=True)
    times_cultured = Column(Integer, nullable=True)
    max_reuse = Column(Integer, nullable=True)
    add_to_secondary = Column(Boolean, nullable=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    recipe = relationship("Recipes", back_populates="yeasts")


class InventoryYeast(Base):
    __tablename__ = "inventory_yeasts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    type = Column(String, nullable=True)
    form = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    amount_is_weight = Column(Boolean, nullable=True)
    laboratory = Column(String, nullable=True)
    product_id = Column(String, nullable=True)
    min_temperature = Column(Float, nullable=True)
    max_temperature = Column(Float, nullable=True)
    flocculation = Column(String, nullable=True)
    attenuation = Column(Float, nullable=True)
    notes = Column(String, nullable=True)
    best_for = Column(String, nullable=True)
    times_cultured = Column(Integer, nullable=True)
    max_reuse = Column(Integer, nullable=True)
    add_to_secondary = Column(Boolean, nullable=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    batch = relationship("Batches", back_populates="inventory_yeasts")
