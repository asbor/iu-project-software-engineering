import uuid
from datetime import datetime, timezone, date
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class Yeast(Base):
    """
    Represents the yeast table in the database.

    Attributes:
        id (UUID): The unique identifier for the yeast.
        created_at (DateTime): The timestamp when the yeast was created.
        updated_at (DateTime): The timestamp when the yeast was last updated.
        name (str): The name of the yeast.
        version (int): The version number of the yeast.
        type (str): The type of the yeast.
        form (str): The form of the yeast.
        amount (int): The amount of the yeast.
        amount_is_weight (bool): Whether the amount is weight.
        laboratory (str): The laboratory of the yeast.
        product_id (str): The product ID of the yeast.
        min_temperature (int): The minimum temperature of the yeast.
        max_temperature (int): The maximum temperature of the yeast.
        flocculation (str): The flocculation of the yeast.
        attenuation (int): The attenuation of the yeast.
        notes (str): Additional notes about the yeast.
        best_for (str): The best for of the yeast.
        max_reuse (int): The maximum reuse of the yeast.
        times_cultured (int): The times cultured of the yeast.
        add_to_secondary (bool): Whether to add to secondary.
        display_amount (str): Formatted amount of the yeast.
        display_min_temp (str): Formatted minimum temperature of the yeast.
        display_max_temp (str): Formatted maximum temperature of the yeast.
        inventory (int): The inventory of the yeast.
        culture_date (Date): The culture date of the yeast.
        recipe_id (UUID): The unique identifier for the recipe.
        recipe (relationship): Relationship to the Recipe table.
    """
    __tablename__ = "yeast"
    id = Column(UUID(as_uuid=True), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    type = Column(String(255), nullable=False)
    form = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)
    amount_is_weight = Column(Boolean, nullable=False)
    laboratory = Column(String(255), nullable=False)
    product_id = Column(String(255), nullable=False)
    min_temperature = Column(Integer, nullable=False)
    max_temperature = Column(Integer, nullable=False)
    flocculation = Column(String(255), nullable=False)
    attenuation = Column(Integer, nullable=False)
    notes = Column(String(255), nullable=False)
    best_for = Column(String(255), nullable=False)
    max_reuse = Column(Integer, nullable=False)
    times_cultured = Column(Integer, nullable=False)
    add_to_secondary = Column(Boolean, nullable=False)
    display_amount = Column(String(255), nullable=False)
    display_min_temp = Column(String(255), nullable=False)
    display_max_temp = Column(String(255), nullable=False)
    inventory = Column(Integer, nullable=False)
    culture_date = Column(Date, default=date.today, nullable=False)

    # Relationships
    # recipe_id = Column(UUID(as_uuid=True), ForeignKey('recipe.id'))
    # recipe = relationship("Recipe", back_populates="yeast")
    inventory = relationship("Inventory", back_populates="yeast")

    def __repr__(self):
        return f"Yeast(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                version={self.version}, \
                type={self.type}, \
                form={self.form}, \
                amount={self.amount}, \
                amount_is_weight={self.amount_is_weight}, \
                laboratory={self.laboratory}, \
                product_id={self.product_id}, \
                min_temperature={self.min_temperature}, \
                max_temperature={self.max_temperature}, \
                flocculation={self.flocculation}, \
                attenuation={self.attenuation}, \
                notes={self.notes}, \
                best_for={self.best_for}, \
                max_reuse={self.max_reuse}, \
                times_cultured={self.times_cultured}, \
                add_to_secondary={self.add_to_secondary}, \
                display_amount={self.display_amount}, \
                display_min_temp={self.display_min_temp}, \
                display_max_temp={self.display_max_temp}, \
                inventory={self.inventory}, \
                culture_date={self.culture_date}"
