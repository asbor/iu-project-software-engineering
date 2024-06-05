from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class RecipeLiquidExtract(Base):
    """Recipe-specific LiquidExtract table."""

    __tablename__ = "recipe_liquid_extract"
    id = Column(Integer, primary_key=True, index=True)
    fermentable_id = Column(Integer, ForeignKey("recipe_fermentables.id"))


class InventoryLiquidExtract(Base):
    """Inventory-specific LiquidExtract table."""

    __tablename__ = "inventory_liquid_extract"
    id = Column(Integer, primary_key=True, index=True)
    fermentable_id = Column(Integer, ForeignKey("inventory_fermentables.id"))
