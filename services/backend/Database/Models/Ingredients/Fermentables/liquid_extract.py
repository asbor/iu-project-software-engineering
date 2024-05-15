import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class LiquidExtract(Base):
    """
    Liquid Extract model

    Attributes:
        id (UUID): The unique identifier for the liquid extract.

    Relationships:
        fermentable_id (uuid): The fermentable relationship.
    """
    __tablename__ = 'liquid_extracts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Relationships for the fermentable types 1:1
    fermentable_id = Column(UUID(as_uuid=True), ForeignKey('fermentable.id'))
    fermentable = relationship(
        "Fermentable", uselist=False, back_populates="liquid_extract")

    def __repr__(self):
        return f"<LiquidExtract {self.id}>"
