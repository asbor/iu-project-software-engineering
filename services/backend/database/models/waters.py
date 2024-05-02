import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Waters(Base):
    """
    Represents the waters table in the database.

    Attributes:
        id (UUID): The unique identifier for the waters.
        created_at (DateTime): The timestamp when the waters were created.
        updated_at (DateTime): The timestamp when the waters were last updated.
        name (str): The name of the waters.
        version (int): The version number of the waters.
        amount (int): The amount of the waters.
        calcium (int): The calcium of the waters.
        bicarbonate (int): The bicarbonate of the waters.
        sulfate (int): The sulfate of the waters.
        chloride (int): The chloride of the waters.
        sodium (int): The sodium of the waters.
        magnesium (int): The magnesium of the waters.
        ph (int): The pH of the waters.
        notes (str): Additional notes about the waters.
        display_amount (str): Formatted amount of the waters.
        inventory (int): The inventory of the waters.
        recipes_id (UUID): The unique identifier for the recipes.
        recipes (relationship): Relationship to the Recipes table.

    """
    __tablename__ = "waters"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    calcium = Column(Integer, nullable=False)
    bicarbonate = Column(Integer, nullable=False)
    sulfate = Column(Integer, nullable=False)
    chloride = Column(Integer, nullable=False)
    sodium = Column(Integer, nullable=False)
    magnesium = Column(Integer, nullable=False)
    ph = Column(Integer, nullable=False)
    notes = Column(String(255), nullable=False)
    display_amount = Column(String(255), nullable=False)
    inventory = Column(Integer, nullable=False)

    recipes_id = Column(UUID(as_uuid=True), ForeignKey("recipes.id"))
    recipes = relationship("Recipes", back_populates="waters")

    def __repr__(self):
        return f"Waters(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                version={self.version}, \
                amount={self.amount}, \
                calcium={self.calcium}, \
                bicarbonate={self.bicarbonate}, \
                sulfate={self.sulfate}, \
                chloride={self.chloride}, \
                sodium={self.sodium}, \
                magnesium={self.magnesium}, \
                ph={self.ph}, \
                notes={self.notes}, \
                display_amount={self.display_amount}, \
                inventory={self.inventory}"
