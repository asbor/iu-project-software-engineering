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
        created_at (DateTime): The timestamp when the fermentable was created.
        updated_at (DateTime): The timestamp when the fermentable was last updated.
        name (str): The name of the fermentable.
        version (int): The version number of the fermentable.
        type (str): The type of fermentable.
        amount (int): The amount of fermentable used.
        yield_ (int): The yield of the fermentable.
        color (int): The color of the fermentable.
        add_after_boil (bool): Whether to add the fermentable after the boil.
        origin (str): The origin of the fermentable.
        supplier (str): The supplier of the fermentable.
        notes (str): Additional notes about the fermentable.
        coarse_fine_diff (int): The difference between coarse and fine grind of the fermentable.
        moisture (int): The moisture content of the fermentable.
        diastatic_power (int): The diastatic power of the fermentable.
        protein (int): The protein content of the fermentable.
        max_in_batch (int): The maximum amount of fermentable in a batch.
        recommend_mash (bool): Whether to recommend mashing the fermentable.
        ibu_gal_per_lb (int): The IBU per gallon per pound of fermentable.
        display_amount (str): Formatted amount of fermentable.
        inventory (int): The amount of fermentable in inventory.
        potential (int): The potential of the fermentable.
        display_color (str): Formatted color of the fermentable.
        recipe_id (UUID): The unique identifier for the recipe.
        recipe (relationship): Relationship to the Recipe table.
    """
    __tablename__ = "fermentable"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    type = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)
    yield_ = Column(Integer, nullable=False)
    color = Column(Integer, nullable=False)
    add_after_boil = Column(Boolean, nullable=False)
    origin = Column(String(255), nullable=False)
    supplier = Column(String(255), nullable=False)
    notes = Column(String(255), nullable=False)
    coarse_fine_diff = Column(Integer, nullable=False)
    moisture = Column(Integer, nullable=False)
    diastatic_power = Column(Integer, nullable=False)
    protein = Column(Integer, nullable=False)
    max_in_batch = Column(Integer, nullable=False)
    recommend_mash = Column(Boolean, nullable=False)
    ibu_gal_per_lb = Column(Integer, nullable=False)
    display_amount = Column(String(255), nullable=False)
    inventory = Column(Integer, nullable=False)
    potential = Column(Integer, nullable=False)
    display_color = Column(String(255), nullable=False)

    def __repr__(self):
        return f"Fermentable(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                version={self.version}, \
                type={self.type}, \
                amount={self.amount}, \
                yield_={self.yield_}, \
                color={self.color}, \
                add_after_boil={self.add_after_boil}, \
                origin={self.origin}, \
                supplier={self.supplier}, \
                notes={self.notes}, \
                coarse_fine_diff={self.coarse_fine_diff}, \
                moisture={self.moisture}, \
                diastatic_power={self.diastatic_power}, \
                protein={self.protein}, \
                max_in_batch={self.max_in_batch}, \
                recommend_mash={self.recommend_mash}, \
                ibu_gal_per_lb={self.ibu_gal_per_lb}, \
                display_amount={self.display_amount}, \
                inventory={self.inventory}, \
                potential={self.potential}, \
                display_color={self.display_color}"
