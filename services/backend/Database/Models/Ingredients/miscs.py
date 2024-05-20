from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from database import Base


class MasterMiscs(Base):
    """
    Description:
    This class represents the MasterMiscs table in the database.
    It stores detailed information about miscellaneous ingredients.

    Relationships:
    - ONE master misc can be used in ZERO or MANY recipes
    """

    __tablename__ = "master_miscs"

    # Metadata
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)

    # Details
    type = Column(String, nullable=True)
    use = Column(String, nullable=True)
    amount_is_weight = Column(Boolean, nullable=True)
    use_for = Column(String, nullable=True)


class RecipeMiscs(Base):
    """
    Description:
    This class represents the RecipeMiscs table in the database.
    It stores miscellaneous ingredients used in specific recipes.

    Relationships:
    - ONE recipe misc belongs to ONE recipe
    - ONE recipe misc is associated with ONE master misc
    """

    __tablename__ = "recipe_miscs"

    # Metadata
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key relationship
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    master_misc_id = Column(Integer, ForeignKey('master_miscs.id'))

    # Specific attributes for recipe misc
    amount = Column(Integer, nullable=True)
    time = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)
    display_amount = Column(String, nullable=True)
    inventory = Column(Integer, nullable=True)
    display_time = Column(String, nullable=True)
    batch_size = Column(Integer, nullable=True)
