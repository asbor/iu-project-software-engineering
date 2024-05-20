from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base


class Other(Base):
    """
    Description:
    This class represents the Sugar table in the database.

    Note:
    The other is a type of fermentable, which is why it is a subclass of fermentable.

    Relationships:
    - ONE other can have ZERO or MANY fermentables
    """

    __tablename__ = "other"
    id = Column(Integer, primary_key=True, index=True)
    # Most fields are inherited from the fermentable table.

    # Relationships:
    fermentable_id = Column(Integer, ForeignKey('fermentables.id'))
