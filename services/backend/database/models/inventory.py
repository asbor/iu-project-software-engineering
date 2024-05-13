import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Inventory(Base):
    """
    Inventory model

    Attributes:
        id (UUID): The unique identifier for the inventory.
        stock (decimal): The stock of the inventory.
        cost_per_unit (decimal): The cost per unit of the inventory.
        eng_units (string): The energy units of the inventory.

    Relationships:
        fermentable_id (uuid): [adjuncts, dry_extracts, grains, liquid_extracts, other, sugars] The fermentable relationship.
        hop_id (uuid): [hops] The hop relationship.
        yeast_id (uuid): [yeast] The yeast relationship.
        misc_id (uuid): [miscs] The misc relationship.
    """

    __tablename__ = "inventory"

    # Attributes
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stock = Column(Float, nullable=False)
    cost_per_unit = Column(Float, nullable=False)
    eng_units = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(
        timezone.utc), onupdate=datetime.now(timezone.utc))

    # Relationships
    fermentable_id = Column(UUID(as_uuid=True), ForeignKey("fermentable.id"))
    hop_id = Column(UUID(as_uuid=True), ForeignKey("hop.id"))
    yeast_id = Column(UUID(as_uuid=True), ForeignKey("yeast.id"))
    misc_id = Column(UUID(as_uuid=True), ForeignKey("misc.id"))
    fermentable = relationship(
        "Fermentable", uselist=False, back_populates="inventory")
    # hop = relationship("Hop", uselist=False, back_populates="inventory")
    yeast = relationship("Yeast", uselist=False, back_populates="inventory")
    misc = relationship("Misc", uselist=False, back_populates="inventory")

    def __repr__(self):
        return f"<Inventory {self.id}>"
