from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from database import Base


class EquipmentProfiles(Base):

    """

    Description:

    This class represents the EquipmentProfile table in the database.

    The equipment profile NAME needs to be unique.


    Relationships:

    - ONE equipment_profile can have ZERO or MANY recipes

    TODO: - ONE equipment_profile can have ZERO or MANY batches

    """

    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=True)

    version = Column(Integer, nullable=True)

    boil_size = Column(Integer, nullable=True)

    batch_size = Column(Integer, nullable=True)

    tun_volume = Column(Integer, nullable=True)

    tun_weight = Column(Integer, nullable=True)

    tun_specific_heat = Column(Integer, nullable=True)

    top_up_water = Column(Integer, nullable=True)

    trub_chiller_loss = Column(Integer, nullable=True)

    evap_rate = Column(Integer, nullable=True)

    boil_time = Column(Integer, nullable=True)

    calc_boil_volume = Column(Boolean, nullable=True)

    lauter_deadspace = Column(Integer, nullable=True)

    top_up_kettle = Column(Integer, nullable=True)

    hop_utilization = Column(Integer, nullable=True)

    notes = Column(String(255), nullable=True)

    display_boil_size = Column(String(255), nullable=True)

    display_batch_size = Column(String(255), nullable=True)

    display_tun_volume = Column(String(255), nullable=True)

    display_tun_weight = Column(String(255), nullable=True)

    display_top_up_water = Column(String(255), nullable=True)

    display_trub_chiller_loss = Column(String(255), nullable=True)

    display_lauter_deadspace = Column(String(255), nullable=True)

    display_top_up_kettle = Column(String(255), nullable=True)

    # Relationships

    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    # TODO: batch_id = Column(Integer, ForeignKey('batches.id'))
