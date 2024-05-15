import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class Water(Base):
    """
    Represents the water table in the database.

    Attributes:
        id (UUID): The unique identifier for the water.
        created_at (DateTime): The timestamp when the water were created.
        updated_at (DateTime): The timestamp when the water were last updated.
        name (str): The name of the water.
        version (int): The version number of the water.
        amount (int): The amount of the water.
        calcium (int): The calcium of the water.
        bicarbonate (int): The bicarbonate of the water.
        sulfate (int): The sulfate of the water.
        chloride (int): The chloride of the water.
        sodium (int): The sodium of the water.
        magnesium (int): The magnesium of the water.
        ph (int): The pH of the water.
        notes (str): Additional notes about the water.
        display_amount (str): Formatted amount of the water.
        inventory (int): The inventory of the water.
        recipe_id (UUID): The unique identifier for the recipe.
        recipe (relationship): Relationship to the Recipe table.
    """
    __tablename__ = "water"
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

    # Relationships
    # recipe_id = Column(UUID(as_uuid=True), ForeignKey('recipe.id'))
    # recipe = relationship("Recipe", back_populates="water")

    def __repr__(self):
        return f"Water(id={self.id}, \
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
                inventory={self.inventory})"
