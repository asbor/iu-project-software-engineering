import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, DateTime, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ...base import Base


class Sugar(Base):
    """
    Sugar model

    Attributes:
        id (UUID): The unique identifier for the sugar.

    Relationships:
        fermentable (Fermentable): The fermentable relationship.
        inventory (Inventory): The inventory relationship.
    """
    __tablename__ = "sugar"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Attributes

    # Relationships for the fermentable types 1:1
    fermentable_id = Column(UUID(as_uuid=True), ForeignKey("fermentable.id"))
    fermentable = relationship(
        "Fermentable", uselist=False, back_populates="sugar")

    def __repr__(self):
        return f"<Sugar {self.id}>"
