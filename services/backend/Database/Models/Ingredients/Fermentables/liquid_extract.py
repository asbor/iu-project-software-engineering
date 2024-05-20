from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base


class LiquidExtract(Base):
    """
    Description:
    This class represents the LiquidExtract table in the database.

    Note:
    The LiquidExtract is a type of fermentable, which is why it is a subclass of fermentable.

    Relationships:
    - ONE LiquidExtract can have ZERO or MANY fermentables
    """

    __tablename__ = "liquid_extract"
    id = Column(Integer, primary_key=True, index=True)
    # Most fields are inherited from the fermentable table.

    # Relationships:
    fermentable_id = Column(Integer, ForeignKey('master_fermentables.id'))
