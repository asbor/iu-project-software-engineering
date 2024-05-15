from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID
from database import Base


class Hops(Base):
    """
    Description:
    This class represents the Hops table in the database.

    Relationships:
    - ONE hop can have only ONE recipe
    - ONE hop can have only ONE inventory
    """
    __tablename__ = "hops"

    # Metadata
    # id = Column(UUID(as_uuid=True), primary_key=True)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)

    # Specific attributes for hop
    origin = Column(String(255), nullable=False)
    alpha = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)

    # General attributes
    use = Column(String(255), nullable=False)
    time = Column(Integer, nullable=False)
    notes = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    form = Column(String(255), nullable=False)
    beta = Column(Integer, nullable=False)
    hsi = Column(Integer, nullable=False)
    display_amount = Column(String(255), nullable=False)
    inventory = Column(Integer, nullable=False)
    display_time = Column(String(255), nullable=False)

    # Relationships
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    # inventory = relationship("Inventory", back_populates="hop")
