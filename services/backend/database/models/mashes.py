import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Mashes(Base):
    """
    Represents the mashes table in the database.

    Attributes:
        id (UUID): The unique identifier for the mashes.
        created_at (DateTime): The timestamp when the mashes were created.
        updated_at (DateTime): The timestamp when the mashes were last updated.
        name (str): The name of the mashes.
        version (int): The version number of the mashes.
        grain_temp (int): The temperature of the grain in Celsius.
        tun_temp (int): The temperature of the mash tun in Celsius.
        sparge_temp (int): The temperature of the sparge water in Celsius.
        ph (int): The pH of the mashes.
        tun_weight (int): The weight of the mash tun in kilograms.
        tun_specific_heat (int): The specific heat of the mash tun.
        equip_adjust (bool): Whether to adjust the equipment.
        notes (str): Additional notes about the mashes.
        display_grain_temp (str): Formatted temperature of the grain.
        display_tun_temp (str): Formatted temperature of the mash tun.
        display_sparge_temp (str): Formatted temperature of the sparge water.
        display_tun_weight (str): Formatted weight of the mash tun.
        mash_steps (relationship): Relationship to the MashStep table.
        recipes_id (UUID): The unique identifier for the recipes.
        recipes (relationship): Relationship to the Recipes table.
    """
    __tablename__ = "mashes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    grain_temp = Column(Integer, nullable=False)
    tun_temp = Column(Integer, nullable=False)
    sparge_temp = Column(Integer, nullable=False)
    ph = Column(Integer, nullable=False)
    tun_weight = Column(Integer, nullable=False)
    tun_specific_heat = Column(Integer, nullable=False)
    equip_adjust = Column(Boolean, nullable=False)
    notes = Column(String(255), nullable=False)
    display_grain_temp = Column(String(255), nullable=False)
    display_tun_temp = Column(String(255), nullable=False)
    display_sparge_temp = Column(String(255), nullable=False)
    display_tun_weight = Column(String(255), nullable=False)
    mash_steps = relationship("MashStep", back_populates="mashes")

    recipes_id = Column(UUID(as_uuid=True), ForeignKey("recipes.id"))
    recipes = relationship("Recipes", back_populates="mashes")

    def __repr__(self):
        return f"Mashes(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                version={self.version}, \
                grain_temp={self.grain_temp}, \
                tun_temp={self.tun_temp}, \
                sparge_temp={self.sparge_temp}, \
                ph={self.ph}, \
                tun_weight={self.tun_weight}, \
                tun_specific_heat={self.tun_specific_heat}, \
                equip_adjust={self.equip_adjust}, \
                notes={self.notes}, \
                display_grain_temp={self.display_grain_temp}, \
                display_tun_temp={self.display_tun_temp}, \
                display_sparge_temp={self.display_sparge_temp}, \
                display_tun_weight={self.display_tun_weight}"


class MashStep(Base):
    __tablename__ = "mash_step"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    type = Column(String(255), nullable=False)
    infuse_amount = Column(Integer, nullable=False)
    step_time = Column(Integer, nullable=False)
    step_temp = Column(Integer, nullable=False)
    ramp_time = Column(Integer, nullable=False)
    end_temp = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    water_grain_ratio = Column(String(255), nullable=False)
    decoction_amt = Column(String(255), nullable=False)
    infuse_temp = Column(Integer, nullable=False)
    display_step_temp = Column(String(255), nullable=False)
    display_infuse_amt = Column(String(255), nullable=False)

    mashes_id = Column(UUID(as_uuid=True), ForeignKey("mashes.id"))
    mashes = relationship("Mashes", back_populates="mash_steps")

    def __repr__(self):
        return f"MashStep(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                version={self.version}, \
                type={self.type}, \
                infuse_amount={self.infuse_amount}, \
                step_time={self.step_time}, \
                step_temp={self.step_temp}, \
                ramp_time={self.ramp_time}, \
                end_temp={self.end_temp}, \
                description={self.description}, \
                water_grain_ratio={self.water_grain_ratio}, \
                decoction_amt={self.decoction_amt}, \
                infuse_temp={self.infuse_temp}, \
                display_step_temp={self.display_step_temp}, \
                display_infuse_amt={self.display_infuse_amt}"
