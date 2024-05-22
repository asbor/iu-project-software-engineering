from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class RecipeHop(Base):
    __tablename__ = 'recipe_hops'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    origin = Column(String)
    alpha = Column(Float)
    type = Column(String)
    form = Column(String)
    beta = Column(Float)
    hsi = Column(Float)
    amount = Column(Float)
    use = Column(String)
    time = Column(Integer)
    notes = Column(String)
    display_amount = Column(String)
    inventory = Column(String)
    display_time = Column(String)

    # Foreign key to Recipes
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Many-to-one relationship with Recipes
    recipe = relationship("Recipes", back_populates="hops")


class InventoryHop(Base):
    __tablename__ = 'inventory_hops'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    origin = Column(String)
    alpha = Column(Float)
    type = Column(String)
    form = Column(String)
    beta = Column(Float)
    hsi = Column(Float)
    amount = Column(Float)
    use = Column(String)
    time = Column(Integer)
    notes = Column(String)
    display_amount = Column(String)
    inventory = Column(String)
    display_time = Column(String)
