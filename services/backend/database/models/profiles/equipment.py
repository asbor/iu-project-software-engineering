from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from ..base import Base


class Equipment(Base):
    """
    A class representing the Equipment table in the database.

    This table stores information about brewing equipment, including details about
    the size, capacity, and other specifications.

    Attributes:
        id (UUID): The unique identifier for the equipment.
        created_at (DateTime): The timestamp when the equipment was created.
        updated_at (DateTime): The timestamp when the equipment was last updated.
        name (str): The name of the equipment.
        version (int): The version number of the equipment.
        boil_size (int): The size of the boil in liters.
        batch_size (int): The size of the batch in liters.
        tun_volume (int): The volume of the mash tun in liters.
        tun_weight (int): The weight of the mash tun in kilograms.
        tun_specific_heat (int): The specific heat of the mash tun.
        top_up_water (int): The amount of top-up water in liters.
        trub_chiller_loss (int): The loss due to trub and chiller in liters.
        evap_rate (int): The evaporation rate as a percentage.
        boil_time (int): The duration of the boil in minutes.
        calc_boil_volume (bool): Whether to calculate the boil volume.
        lauter_deadspace (int): The dead space in the lauter tun in liters.
        top_up_kettle (int): The amount of top-up water in the kettle in liters.
        hop_utilization (int): The hop utilization as a percentage.
        notes (str): Additional notes about the equipment.
        display_boil_size (str): Formatted size of the boil.
        display_batch_size (str): Formatted size of the batch.
        display_tun_volume (str): Formatted volume of the mash tun.
        display_tun_weight (str): Formatted weight of the mash tun.
        display_top_up_water (str): Formatted amount of top-up water.
        display_trub_chiller_loss (str): Formatted loss due to trub and chiller.
        display_lauter_deadspace (str): Formatted dead space in the lauter tun.
        display_top_up_kettle (str): Formatted amount of top-up water in the kettle.
    """
    __tablename__ = "equipment"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    version = Column(Integer, nullable=False)
    boil_size = Column(Integer, nullable=False)
    batch_size = Column(Integer, nullable=False)
    tun_volume = Column(Integer, nullable=False)
    tun_weight = Column(Integer, nullable=False)
    tun_specific_heat = Column(Integer, nullable=False)
    top_up_water = Column(Integer, nullable=False)
    trub_chiller_loss = Column(Integer, nullable=False)
    evap_rate = Column(Integer, nullable=False)
    boil_time = Column(Integer, nullable=False)
    calc_boil_volume = Column(Boolean, nullable=False)
    lauter_deadspace = Column(Integer, nullable=False)
    top_up_kettle = Column(Integer, nullable=False)
    hop_utilization = Column(Integer, nullable=False)
    notes = Column(String(255), nullable=False)
    display_boil_size = Column(String(255), nullable=False)
    display_batch_size = Column(String(255), nullable=False)
    display_tun_volume = Column(String(255), nullable=False)
    display_tun_weight = Column(String(255), nullable=False)
    display_top_up_water = Column(String(255), nullable=False)
    display_trub_chiller_loss = Column(String(255), nullable=False)
    display_lauter_deadspace = Column(String(255), nullable=False)
    display_top_up_kettle = Column(String(255), nullable=False)

    # Relationships
    recipe_id = Column(UUID(as_uuid=True), ForeignKey('recipe.id'))
    # recipe = relationship("Recipe", back_populates="equipment")

    def __repr__(self):
        return f"Equipment(id={self.id}, \
                name={self.name}"
