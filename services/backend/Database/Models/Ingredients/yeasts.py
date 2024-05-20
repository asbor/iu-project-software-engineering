from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from database import Base
from sqlalchemy.orm import relationship


class Yeasts(Base):
    __tablename__ = "yeasts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=True)
    form = Column(String, nullable=True)
    laboratory = Column(String, nullable=True)
    product_id = Column(String, nullable=True)
    min_temperature = Column(Float, nullable=True)
    max_temperature = Column(Float, nullable=True)
    flocculation = Column(String, nullable=True)
    attenuation = Column(Float, nullable=True)
    notes = Column(String, nullable=True)
    best_for = Column(String, nullable=True)
    max_reuse = Column(Integer, nullable=True)
    amount = Column(Float, nullable=False)
    amount_is_weight = Column(Boolean, nullable=True)
    inventory = Column(Float, nullable=True)
    display_amount = Column(String, nullable=True)

    # Foreign key to Recipes
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Many-to-one relationship with Recipes
    # recipe = relationship("Recipes", back_populates="yeasts")
