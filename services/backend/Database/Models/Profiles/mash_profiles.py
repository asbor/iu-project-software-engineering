from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class MashProfiles(Base):

    """

    Description:

    This class represents the MashProfile table in the database.

    The mash profile NAME needs to be unique.


    Relationships:

    - ONE mash_profile can have ZERO or MANY recipes

    - ONE mash_profile can have ZERO or MANY batches

    """

    __tablename__ = "mash"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=True)

    version = Column(Integer, nullable=True)

    grain_temp = Column(Integer, nullable=True)

    tun_temp = Column(Integer, nullable=True)

    sparge_temp = Column(Integer, nullable=True)

    ph = Column(Integer, nullable=True)

    tun_weight = Column(Integer, nullable=True)

    tun_specific_heat = Column(Integer, nullable=True)

    # equip_adjust = Column(Boolean, nullable=True)

    notes = Column(String(255), nullable=True)

    display_grain_temp = Column(String(255), nullable=True)

    display_tun_temp = Column(String(255), nullable=True)

    display_sparge_temp = Column(String(255), nullable=True)

    display_tun_weight = Column(String(255), nullable=True)


class MashStep(Base):

    """

    Description:

    This class represents the MashStep table in the database.


    Relationships:

    - ONE mash_step can have ONE mash_profile

    """

    __tablename__ = "mash_step"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=True)

    version = Column(Integer, nullable=True)

    type = Column(String(255), nullable=True)

    infuse_amount = Column(Integer, nullable=True)

    step_time = Column(Integer, nullable=True)

    step_temp = Column(Integer, nullable=True)

    ramp_time = Column(Integer, nullable=True)

    end_temp = Column(Integer, nullable=True)

    description = Column(String(255), nullable=True)

    water_grain_ratio = Column(String(255), nullable=True)

    decoction_amt = Column(String(255), nullable=True)

    infuse_temp = Column(Integer, nullable=True)

    display_step_temp = Column(String(255), nullable=True)

    display_infuse_amt = Column(String(255), nullable=True)

    # Relationships

    mash_id = Column(Integer, ForeignKey("mash.id"))
