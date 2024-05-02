import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Hops(Base):
    """
    A class representing the Hops table in the database.

    This table stores information about hops used in brewing recipes, including details about
    the origin, alpha acid content, and usage.

    Attributes:
        id (UUID): The unique identifier for the hops.
        created_at (DateTime): The timestamp when the hops were created.
        updated_at (DateTime): The timestamp when the hops were last updated.
        name (str): The name of the hops.
        version (int): The version number of the hops.
        origin (str): The origin of the hops.
        alpha (int): The alpha acid content of the hops.
        amount (int): The amount of hops used.
        use (str): The usage of the hops.
        time (int): The time the hops are added.
        notes (str): Additional notes about the hops.
        type (str): The type of hops.
        form (str): The form of the hops.
        beta (int): The beta acid content of the hops.
        hsi (int): The hop stability index of the hops.
        display_amount (str): Formatted amount of hops.
        inventory (int): The amount of hops in inventory.
        display_time (str): Formatted time the hops are added.
        recipes (relationship): Relationship to the Recipes table.
    """
    __tablename__ = "hops"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    origin = Column(String(255), nullable=False)
    alpha = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
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

    recipes_id = Column(UUID(as_uuid=True), ForeignKey("recipes.id"))
    recipes = relationship("Recipes", back_populates="hops")

    def __repr__(self):
        return f"Hops(id={self.id}, \
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
