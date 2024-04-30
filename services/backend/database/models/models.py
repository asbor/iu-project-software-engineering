from sqlalchemy import CheckConstraint, Column, Date, DateTime, Enum, Integer, String, ForeignKey, Table, UniqueConstraint, Boolean, Object
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from datetime import datetime, timezone, date

from sqlalchemy.ext.declarative import declarative_base
import uuid

# ************************************************************
# *                     DATABASE MODELS                      *
# ************************************************************
# The models are to be used to create the database tables
# The schemas are to be used to validate the data that is being sent to the database
# The endpoints are to be used to interact with the database

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,
                unique=True, nullable=False, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    surname = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc),
                        onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name}, surname={self.surname})"


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    birth_date = Column(Date, default=date.today, nullable=False)
    personal_identificator = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)

    reservation = relationship("Reservation", back_populates="user")
    rentals = relationship("Rental", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, \
                name={self.name}, \
                surname={self.surname}, \
                email={self.email}, \
                birth_date={self.birth_date}, \
                personal_identificator={self.personal_identificator}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at})"


class Recipes(Base):
    __tablename__ = "recipes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)

    def __repr__(self):
        return f"Recipe(id={self.id}, \
                name={self.name}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at})"


class EquipmentProfile(Base):
    __tablename__ = "equipment_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    boil_time = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    batch_volume_target = Column(Object, nullable=False)
    batch_volume_fermenter = Column(Integer, nullable=False)
    calculated_boil_volume = Column(Boolean, nullable=False)
    pre_boil_volume = Column(Integer, nullable=False)
    boil_off_rate = Column(Integer, nullable=False)
    trube_chiller_loss = Column(Integer, nullable=False)
    mash_tune_deadspace = Column(Integer, nullable=False)
    mash_tune_loss = Column(Integer, nullable=False)
    hlt_deadspace = Column(Integer, nullable=False)
    fermenter_loss = Column(Integer, nullable=False)
    fermenter_top_up = Column(Integer, nullable=False)
    post_boil_kettle_volume = Column(Integer, nullable=False)
    botteling_volume = Column(Integer, nullable=False)
    brew_house_efficiency = Column(Integer, nullable=False)
    mash_efficiency = Column(Integer, nullable=False)
    calc_mash_efficiency = Column(bool, nullable=False)
    hop_utilization_multiplier = Column(Integer, nullable=False)
    aroma_hop_utilization_multiplier = Column(Integer, nullable=False)
    calc_aroma_hop_utilization = Column(bool, nullable=False)
    hop_stand_temp = Column(Integer, nullable=False)
    whirlpool_time = Column(Integer, nullable=False)
    altitude_boil_temp = Column(Integer, nullable=False)
    altitude_adjustment = Column(bool, nullable=False)
    boil_temp = Column(Integer, nullable=False)
    cooling_shrinkage = Column(Integer, nullable=False)
    grain_absorption_rate = Column(Integer, nullable=False)
    water_grain_ratio = Column(Integer, nullable=False)
    mash_sparge_water_calc_method = Column(String, nullable=False)
    sparge_water_reminder = Column(Integer, nullable=False)
    time_left_of_mash = Column(Integer, nullable=False)
    include_grain_volume_in_mash_limit = Column(bool, nullable=False)
    mash_limit_min = Column(Integer, nullable=False)
    mash_limit_max = Column(Integer, nullable=False)
    sparge_water_limit_min = Column(Integer, nullable=False)
    sparge_water_limit_max = Column(Integer, nullable=False)
    overflow_target = Column(Integer, nullable=False)
    hlt_water_limit_min = Column(Integer, nullable=False)
    calc_strike_temp = Column(bool, nullable=False)
    sparge_temp = Column(Integer, nullable=False)
