from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base


class Inventory(Base):
    """
    Description:
    This class represents the Inventory table in the database.

    Relationships:
    TODO: - ONE inventory "entry" can have ZERO or MANY Hops
    TODO: - ONE inventory "entry" can have ZERO or MANY Fermentables
    TODO: - ONE inventory "entry" can have ZERO or MANY Miscs
    TODO: - ONE inventory "entry" can have ZERO or MANY Yeasts
    """

    __tablename__ = "inventory"

    # Attributes
    id = Column(Integer, primary_key=True, index=True)
    stock = Column(Integer, nullable=True)
    cost_per_unit = Column(Integer, nullable=True)
    eng_units = Column(String, nullable=True)
