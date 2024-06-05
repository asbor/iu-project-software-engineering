from sqlalchemy import Column, Integer, ForeignKey

from database import Base





class RecipeAdjunct(Base):

    """

    Recipe-specific Adjunct table.

    """



    __tablename__ = "recipe_adjunct"

    id = Column(Integer, primary_key=True, index=True)

    fermentable_id = Column(Integer, ForeignKey("recipe_fermentables.id"))





class InventoryAdjunct(Base):

    """

    Inventory-specific Adjunct table.

    """



    __tablename__ = "inventory_adjunct"

    id = Column(Integer, primary_key=True, index=True)

    fermentable_id = Column(Integer, ForeignKey("inventory_fermentables.id"))
