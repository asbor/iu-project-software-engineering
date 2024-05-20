from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from database import Base


class MasterFermentables(Base):
    """
    Description:
    This class represents the MasterFermentables table in the database.
    It stores detailed information about fermentables.

    Relationships:
    - ONE master fermentable can be used in ZERO or MANY recipes
    """

    __tablename__ = "master_fermentables"

    # Metadata
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True, unique=True)

    # Details
    type = Column(String, nullable=True)
    color = Column(Integer, nullable=True)
    potential = Column(Integer, nullable=True)
    yield_ = Column(Float, nullable=True)
    manufacturing_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)
    lot_number = Column(String, nullable=True)
    supplier = Column(String, nullable=True)
    origin = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    description = Column(String, nullable=True)
    substitutes = Column(String, nullable=True)
    used_in = Column(String, nullable=True)


class RecipeFermentables(Base):
    """
    Description:
    This class represents the RecipeFermentables table in the database.
    It stores fermentables used in specific recipes.

    Relationships:
    - ONE recipe fermentable belongs to ONE recipe
    - ONE recipe fermentable is associated with ONE master fermentable
    """

    __tablename__ = "recipe_fermentables"

    # Metadata
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key relationship
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    master_fermentable_id = Column(
        Integer, ForeignKey('master_fermentables.id'))

    # Specific attributes for recipe fermentable
    amount = Column(Float, nullable=True)
    cost_per_unit = Column(Float, nullable=True)
    exclude_from_total = Column(Boolean, nullable=True)
    not_fermentable = Column(Boolean, nullable=True)
