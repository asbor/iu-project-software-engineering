# Database/batches.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Batches(Base):
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True, index=True)
    batch_name = Column(String, nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    batch_size = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    recipe = relationship("Recipes", back_populates="batches")
