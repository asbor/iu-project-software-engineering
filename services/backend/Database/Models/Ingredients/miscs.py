from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class RecipeMisc(Base):
    __tablename__ = "recipe_miscs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    type = Column(String, nullable=True)
    use = Column(String, nullable=True)
    amount_is_weight = Column(Boolean, nullable=True)
    use_for = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    amount = Column(Integer, nullable=True)
    time = Column(Integer, nullable=True)
    display_amount = Column(String, nullable=True)
    inventory = Column(Integer, nullable=True)
    display_time = Column(String, nullable=True)
    batch_size = Column(Integer, nullable=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    recipe = relationship("Recipes", back_populates="miscs")


class InventoryMisc(Base):
    __tablename__ = "inventory_miscs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    type = Column(String, nullable=True)
    use = Column(String, nullable=True)
    amount_is_weight = Column(Boolean, nullable=True)
    use_for = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    amount = Column(Integer, nullable=True)
    time = Column(Integer, nullable=True)
    display_amount = Column(String, nullable=True)
    inventory = Column(Integer, nullable=True)
    display_time = Column(String, nullable=True)
    batch_size = Column(Integer, nullable=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    batch = relationship("Batches", back_populates="inventory_miscs")
