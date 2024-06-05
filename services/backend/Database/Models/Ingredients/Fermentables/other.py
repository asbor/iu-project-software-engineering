from sqlalchemy import Column, Integer, ForeignKey

from database import Base





class RecipeOther(Base):

    """

    Recipe-specific Other table.

    """



    __tablename__ = "recipe_other"

    id = Column(Integer, primary_key=True, index=True)

    fermentable_id = Column(Integer, ForeignKey("recipe_fermentables.id"))





class InventoryOther(Base):

    """

    Inventory-specific Other table.

    """



    __tablename__ = "inventory_other"

    id = Column(Integer, primary_key=True, index=True)

    fermentable_id = Column(Integer, ForeignKey("inventory_fermentables.id"))
