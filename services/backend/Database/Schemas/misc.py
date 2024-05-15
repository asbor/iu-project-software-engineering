from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Misc(BaseModel):
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

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    type: str
    use: str
    amount: int
    time: int
    amount_is_weight: bool
    use_for: str
    notes: str
    display_amount: str
    inventory: int
    display_time: str
    batch_size: int

    class Config:
        from_attributes = True
