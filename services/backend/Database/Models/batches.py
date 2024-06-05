# services/backend/Database/Models/batches.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Batches(Base):
    __tablename__ = "batches"
    id = Column(Integer, primary_key=True, index=True)
    batch_name = Column(String, nullable=False)
    batch_number = Column(Integer, nullable=False)
    batch_size = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    brewer = Column(String, nullable=False)
    brew_date = Column(DateTime, nullable=False)
    # Relationships:

    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    recipe = relationship("Recipes", back_populates="batches")
    batch_log = relationship(
        "BatchLogs", back_populates="batch", uselist=False
    )
    inventory_fermentables = relationship(
        "InventoryFermentable", back_populates="batch"
    )
    inventory_hops = relationship("InventoryHop", back_populates="batch")
    inventory_miscs = relationship("InventoryMisc", back_populates="batch")
    inventory_yeasts = relationship("InventoryYeast", back_populates="batch")
