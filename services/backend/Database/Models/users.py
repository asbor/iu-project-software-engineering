from sqlalchemy import Column, Integer, String
from database import Base


class Users(Base):
    """
    Description:

    This class represents the User table in the database.

    The user is also referred to as the brewer.

    Relationships:

    - ONE user/brewer can have ZERO or MANY recipes

    - ONE user/brewer can have ZERO or MANY equipment_profiles

    - ONE user/brewer can have ZERO or MANY fermentation_profiles

    - ONE user/brewer can have ZERO or MANY mash_profiles

    - ONE user/brewer can have ZERO or MANY water_profiles

    Notes:

    - The relationship between the User and Recipe tables is defined in the

    Recipe table

    - The relationship between the User and EquipmentProfile tables is defined

    in the EquipmentProfile table

    - The relationship between the User and FermentationProfile tables is

    defined in the FermentationProfile table

    - The relationship between the User and MashProfile tables is defined in

    the MashProfile table

    - The relationship between the User and WaterProfile tables is defined in

    the WaterProfile table

    """

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    email = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
