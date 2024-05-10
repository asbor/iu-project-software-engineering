import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..base import Base


class Hop(Base):
    """
    A class representing the Hop table in the database.

    This table stores information about hop used in brewing recipe, including details about
    the origin, alpha acid content, and usage.

    Attributes:
        id (UUID): The unique identifier for the hop.
        created_at (DateTime): The timestamp when the hop was created.
        updated_at (DateTime): The timestamp when the hop was last updated.
        name (str): The name of the hop.
        version (int): The version number of the hop.
        origin (str): The origin of the hop.
        alpha (int): The alpha acid content of the hop.
        amount (int): The amount of hop used.
        use (str): The usage of the hop.
        time (int): The time the hop is added.
        notes (str): Additional notes about the hop.
        type (str): The type of hop.
        form (str): The form of the hop.
        beta (int): The beta acid content of the hop.
        hsi (int): The hop stability index of the hop.
        display_amount (str): Formatted amount of hop.
        inventory (int): The amount of hop in inventory.
        display_time (str): Formatted time the hop is added.
        recipe (relationship): Relationship to the Recipe table.
    """
    __tablename__ = "hop"

    # Metadata
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)

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
    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id"))
    recipe = relationship("Recipe", back_populates="hop")
    inventory = relationship("Inventory", back_populates="hop")

    def __repr__(self):
        return f"Hop(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                version={self.version}, \
                origin={self.origin}, \
                alpha={self.alpha}, \
                amount={self.amount}, \
                use={self.use}, \
                time={self.time}, \
                notes={self.notes}, \
                type={self.type}, \
                form={self.form}, \
                beta={self.beta}, \
                hsi={self.hsi}, \
                display_amount={self.display_amount}, \
                inventory={self.inventory}, \
                display_time={self.display_time}"
