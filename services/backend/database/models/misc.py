import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Misc(Base):
    """
    A class representing the Misc table in the database.

    This table stores information about miscellaneous ingredients used in brewing recipe,
    including details about the type, amount, and usage.

    Attributes:
        id (UUID): The unique identifier for the misc ingredient.
        created_at (DateTime): The timestamp when the misc ingredient was created.
        updated_at (DateTime): The timestamp when the misc ingredient was last updated.
        name (str): The name of the misc ingredient.
        version (int): The version number of the misc ingredient.
        type (str): The type of the misc ingredient.
        use (str): The usage of the misc ingredient.
        amount (int): The amount of the misc ingredient used.
        time (int): The time the misc ingredient is added.
        amount_is_weight (bool): Whether the amount is a weight or volume.
        use_for (str): The purpose of the misc ingredient.
        notes (str): Additional notes about the misc ingredient.
        display_amount (str): Formatted amount of the misc ingredient.
        inventory (int): The amount of the misc ingredient in inventory.
        display_time (str): Formatted time the misc ingredient is added.
        batch_size (int): The batch size the misc ingredient is used for.
    """
    __tablename__ = "misc"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    type = Column(String(255), nullable=False)
    use = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
    amount_is_weight = Column(Boolean, nullable=False)
    use_for = Column(String(255), nullable=False)
    notes = Column(String(255), nullable=False)
    display_amount = Column(String(255), nullable=False)
    inventory = Column(Integer, nullable=False)
    display_time = Column(String(255), nullable=False)
    batch_size = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Misc(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                version={self.version}, \
                type={self.type}, \
                use={self.use}, \
                amount={self.amount}, \
                time={self.time}, \
                amount_is_weight={self.amount_is_weight}, \
                use_for={self.use_for}, \
                notes={self.notes}, \
                display_amount={self.display_amount}, \
                inventory={self.inventory}, \
                display_time={self.display_time}, \
                batch_size={self.batch_size}"
