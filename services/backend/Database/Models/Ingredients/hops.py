# services/backend/Database/Models/Ingredients/hops.py



from sqlalchemy import Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import relationship

from database import Base





class RecipeHop(Base):

    __tablename__ = "recipe_hops"



    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=True)

    origin = Column(String, nullable=True)

    alpha = Column(Float, nullable=True)

    type = Column(String, nullable=True)

    form = Column(String, nullable=True)

    beta = Column(Float, nullable=True)

    hsi = Column(Float, nullable=True)

    amount = Column(Float, nullable=True)

    use = Column(String, nullable=True)

    time = Column(Integer, nullable=True)

    notes = Column(String, nullable=True)

    display_amount = Column(String, nullable=True)

    inventory = Column(String, nullable=True)

    display_time = Column(String, nullable=True)

    recipe_id = Column(Integer, ForeignKey("recipes.id"))



    recipe = relationship("Recipes", back_populates="hops")





class InventoryHop(Base):

    __tablename__ = "inventory_hops"



    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=True)

    origin = Column(String, nullable=True)

    alpha = Column(Float, nullable=True)

    type = Column(String, nullable=True)

    form = Column(String, nullable=True)

    beta = Column(Float, nullable=True)

    hsi = Column(Float, nullable=True)

    amount = Column(Float, nullable=True)

    use = Column(String, nullable=True)

    time = Column(Integer, nullable=True)

    notes = Column(String, nullable=True)

    display_amount = Column(String, nullable=True)

    inventory = Column(String, nullable=True)

    display_time = Column(String, nullable=True)

    batch_id = Column(Integer, ForeignKey("batches.id"))



    batch = relationship("Batches", back_populates="inventory_hops")
