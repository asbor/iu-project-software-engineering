from sqlalchemy import Column, Integer, ForeignKey

from database import Base





class RecipeSugar(Base):

    """

    Recipe-specific sugar table.

    """



    __tablename__ = "recipe_sugar"

    id = Column(Integer, primary_key=True, index=True)

    fermentable_id = Column(Integer, ForeignKey("recipe_fermentables.id"))





class InventorySugar(Base):

    """

    Inventory-specific sugar table.

    """



    __tablename__ = "inventory_sugar"

    id = Column(Integer, primary_key=True, index=True)

    fermentable_id = Column(Integer, ForeignKey("inventory_fermentables.id"))
