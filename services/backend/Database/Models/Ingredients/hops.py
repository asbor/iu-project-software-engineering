from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database import Base


class MasterHops(Base):
    __tablename__ = "master_hops"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    origin = Column(String, nullable=True)
    alpha = Column(Float, nullable=True)
    type = Column(String, nullable=True)
    form = Column(String, nullable=True)
    beta = Column(Float, nullable=True)
    hsi = Column(Float, nullable=True)


class RecipeHops(Base):
    __tablename__ = "recipe_hops"
    id = Column(Integer, primary_key=True, index=True)
    master_hop_id = Column(Integer, ForeignKey("master_hops.id"))
    amount = Column(Float, nullable=False)
    use = Column(String, nullable=True)
    time = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)
    display_amount = Column(String, nullable=True)
    inventory = Column(Float, nullable=True)
    display_time = Column(String, nullable=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    master_hop = relationship("MasterHops")
    recipe = relationship("Recipes", back_populates="hops")
