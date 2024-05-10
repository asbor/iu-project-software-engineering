import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ...base import Base


class Adjunct(Base):
    """
    Adjunct model

    Attributes:
        id (UUID): The unique identifier for the adjunct.
        total_ibu_per_kg (decimal): The total IBU per kg of the adjunct.

    Relationships:
        fermentable_id (uuid): The fermentable relationship.
    """
    __tablename__ = 'adjunct'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    total_ibu_per_kg = Column(Float)

    # Relationships for the fermentable types 1:1
    fermentable_id = Column(UUID, ForeignKey("fermentable.id"))
    fermentable = relationship(
        "Fermentable", uselist=False, back_populates="adjunct")

    def __repr__(self):
        return f"<Adjunct {self.id}, \
                total_ibu_per_kg={self.total_ibu_per_kg}>"
