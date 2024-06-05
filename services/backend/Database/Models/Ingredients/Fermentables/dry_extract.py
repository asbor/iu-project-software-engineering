from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class RecipeDryExtract(Base):
    """
    Recipe-specific DryExtract table.
    """

    __tablename__ = "recipe_dry_extract"
    id = Column(Integer, primary_key=True, index=True)
    fermentable_id = Column(Integer, ForeignKey("recipe_fermentables.id"))


class InventoryDryExtract(Base):
    """
    Inventory-specific DryExtract table.
    """

    __tablename__ = "inventory_dry_extract"
    id = Column(Integer, primary_key=True, index=True)
    fermentable_id = Column(Integer, ForeignKey("inventory_fermentables.id"))
