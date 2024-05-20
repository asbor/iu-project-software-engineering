from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from database import Base


class Grain(Base):
    """
    Description:
    This class represents the Grain table in the database.

    Note:
    The Grain is a type of fermentable, which is why it is a subclass of fermentable.

    Relationships:
    - ONE Grain can have ZERO or MANY fermentables (entries in the fermentable table)
    """

    __tablename__ = "grain"
    id = Column(Integer, primary_key=True, index=True)
    # Most fields are inherited from the fermentable table.
    diastatic_power = Column(Float, nullable=True)
    moisture = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    coarse_fine_diff = Column(Float, nullable=True)
    extract = Column(Float, nullable=True)
    acidity = Column(Float, nullable=True)
    friability = Column(Float, nullable=True)
    free_amino_nitrogen = Column(Float, nullable=True)
    max_in_batch = Column(Float, nullable=True)

    # Relationships for the fermentable types 1:1
    fermentable_id = Column(Integer, ForeignKey('fermentables.id'))
