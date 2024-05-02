import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Fermentables(Base):
    """
    Fermentables model

    Attributes:
        id (UUID): The unique identifier for the fermentables.
        created_at (DateTime): The timestamp when the fermentables were created.
        updated_at (DateTime): The timestamp when the fermentables were last updated.
        name (str): The name of the fermentables.
        version (int): The version number of the fermentables.
        type (str): The type of fermentables.
        amount (int): The amount of fermentables used.
        yield_ (int): The yield of the fermentables.
        color (int): The color of the fermentables.
        add_after_boil (bool): Whether to add the fermentables after the boil.
        origin (str): The origin of the fermentables.
        supplier (str): The supplier of the fermentables.
        notes (str): Additional notes about the fermentables.
        coarse_fine_diff (int): The difference between coarse and fine grind of the fermentables.
        moisture (int): The moisture content of the fermentables.
        diastatic_power (int): The diastatic power of the fermentables.
        protein (int): The protein content of the fermentables.
        max_in_batch (int): The maximum amount of fermentables in a batch.
        recommend_mash (bool): Whether to recommend mashing the fermentables.
        ibu_gal_per_lb (int): The IBU per gallon per pound of fermentables.
        display_amount (str): Formatted amount of fermentables.
        inventory (int): The amount of fermentables in inventory.
        potential (int): The potential of the fermentables.
        display_color (str): Formatted color of the fermentables.
        recipes_id (UUID): The unique identifier for the recipes.
        recipes (relationship): Relationship to the Recipes table.
    """
    __tablename__ = "fermentables"
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

    recipes_id = Column(UUID(as_uuid=True), ForeignKey("recipes.id"))
    recipes = relationship("Recipes", back_populates="fermentables")

    def __repr__(self):
        return f"Fermentables(id={self.id}, \
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
