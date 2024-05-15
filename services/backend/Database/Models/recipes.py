from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, UUID
from database import Base


class Recipes(Base):
    """
    Description:
    This class represents the Recipe table in the database.

    Relationships:
    - ONE recipe can have ZERO or MANY hops
    - ONE recipe can have ONE or MANY fermentables
    - ONE recipe can have ZERO or MANY miscs
    - ONE recipe can have ONE or MANY yeasts
    - ONE recipe can have ONE or MANY fermentation_profiles
    - ONE recipe can have only ONE style
    - ONE recipe can have only ONE equipment_profile
    - ONE recipe can have only ONE mash_profile
    - ONE recipe can have only ONE water_profile
    - ONE recipe can have only ONE carbonation_profile
    """

    __tablename__ = "recipes"

    # id = Column(UUID(as_uuid=True), primary_key=True)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    version = Column(Integer, nullable=True)
    type = Column(String(255), nullable=True)
    brewer = Column(String(255), nullable=True)
    asst_brewer = Column(String(255), nullable=True)
    batch_size = Column(Integer, nullable=True)
    boil_size = Column(Integer, nullable=True)
    boil_time = Column(Integer, nullable=True)
    efficiency = Column(Integer, nullable=True)
    # mash = Column(String(255), nullable=True)
    notes = Column(String(255), nullable=True)
    taste_notes = Column(String(255), nullable=True)
    taste_rating = Column(Integer, nullable=True)
    og = Column(Integer, nullable=True)
    fg = Column(Integer, nullable=True)
    fermentation_stages = Column(Integer, nullable=True)
    primary_age = Column(Integer, nullable=True)
    primary_temp = Column(Integer, nullable=True)
    secondary_age = Column(Integer, nullable=True)
    secondary_temp = Column(Integer, nullable=True)
    tertiary_age = Column(Integer, nullable=True)
    tertiary_temp = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)
    age_temp = Column(Integer, nullable=True)
    carbonation_used = Column(String(255), nullable=True)
    # carbonation_date = Column(Date, nullable=True)
    est_og = Column(Integer, nullable=True)
    est_fg = Column(Integer, nullable=True)
    est_color = Column(Integer, nullable=True)
    ibu = Column(Integer, nullable=True)
    ibu_method = Column(String(255), nullable=True)
    est_abv = Column(Integer, nullable=True)
    abv = Column(Integer, nullable=True)
    actual_efficiency = Column(Integer, nullable=True)
    calories = Column(Integer, nullable=True)
    display_batch_size = Column(String(255), nullable=True)
    display_boil_size = Column(String(255), nullable=True)
    display_og = Column(String(255), nullable=True)
    display_fg = Column(String(255), nullable=True)
    display_primary_temp = Column(String(255), nullable=True)
    display_secondary_temp = Column(String(255), nullable=True)
    display_tertiary_temp = Column(String(255), nullable=True)
    display_age_temp = Column(String(255), nullable=True)
