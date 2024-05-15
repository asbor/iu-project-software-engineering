import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class Other(Base):
    """
    Other model

    Attributes:
        id (UUID): The unique identifier for the other.
        total_ibu_per_kg (decimal): The total IBU per kg of the other.

    Relationships:
        fermentable_id (uuid): The fermentable relationship.
    """
    __tablename__ = 'others'

    # Attributes
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    total_ibu_per_kg = Column(Float)

    # Relationships for the fermentable types 1:1
    fermentable_id = Column(UUID(as_uuid=True), ForeignKey('fermentable.id'))
    fermentable = relationship(
        "Fermentable", uselist=False, back_populates="other")

    def __repr__(self):
        return f"<Other {self.id}, \
                total_ibu_per_kg={self.total_ibu_per_kg}>"
