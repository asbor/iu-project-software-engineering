import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Fermentable(Base):
    """
    Fermentable model

    Attributes:
        id (UUID): The unique identifier for the fermentable.
        created_at (datetime): The date and time the fermentable was created.
        updated_at (datetime): The date and time the fermentable was last updated.
        name (str): The name of the fermentable.
        amount (int): The amount of the fermentable in kilograms.
        cost_per_unit (float): The cost per unit in Euros.
        supplier (str): The supplier of the fermentable.
        origin (str): The origin of the fermentable.
        type (str): The type of the fermentable.
        color (int): The color of the fermentable in EBC.
        potential (int): The potential of the fermentable in PPG (Points Per Gallon).
        yield_ (float): The yield of the fermentable as a percentage.
        manufacturing_date (str): The manufacturing date of the fermentable.
        expiry_date (str): The expiry date of the fermentable.
        lot_number (str): The lot number of the fermentable.
        exclude_from_total (bool): Indicates whether to exclude the fermentable from the total.
        not_fermentable (bool): Indicates whether the fermentable is not fermentable.
        notes (str): Additional notes about the fermentable.
        description (str): Description of the fermentable.
        substitutes (str): Substitutes for the fermentable.
        used_in (str): Where the fermentable is used.
    """
    __tablename__ = "fermentable"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    cost_per_unit = Column(Integer, nullable=False)
    supplier = Column(String, nullable=False)
    origin = Column(String, nullable=False)
    type = Column(String, nullable=False)
    color = Column(Integer, nullable=False)
    potential = Column(Integer, nullable=False)
    yield_ = Column(Integer, nullable=False)
    manufacturing_date = Column(DateTime, default=datetime.now(timezone.utc))
    expiry_date = Column(DateTime, default=datetime.now(timezone.utc))
    lot_number = Column(String, nullable=False)
    exclude_from_total = Column(Boolean, nullable=False)
    not_fermentable = Column(Boolean, nullable=False)
    notes = Column(String, nullable=False)
    description = Column(String, nullable=False)
    substitutes = Column(String, nullable=False)
    used_in = Column(String, nullable=False)

    def __repr__(self):
        return f"Fermentable(id={self.id}, \
            name={self.name}, \
            amount={self.amount}, \
            cost_per_unit={self.cost_per_unit}, \
            supplier={self.supplier}, \
            origin={self.origin}, \
            type={self.type}, \
            color={self.color}, \
            potential={self.potential}, \
            yield_={self.yield_}, \
            manufacturing_date={self.manufacturing_date}, \
            expiry_date={self.expiry_date}, \
            lot_number={self.lot_number}, \
            exclude_from_total={self.exclude_from_total}, \
            not_fermentable={self.not_fermentable}, \
            notes={self.notes}, \
            description={self.description}, \
            substitutes={self.substitutes}, \
            used_in={self.used_in})"
