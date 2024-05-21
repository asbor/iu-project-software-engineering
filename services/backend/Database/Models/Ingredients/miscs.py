from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from database import Base
from sqlalchemy.orm import relationship


class Miscs(Base):
    """
    """

    __tablename__ = "miscs"
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

    # Foreign key to Recipes
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Many-to-one relationship with Recipes
    recipe = relationship("Recipes", back_populates="miscs")
