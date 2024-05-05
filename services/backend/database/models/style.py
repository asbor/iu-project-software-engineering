import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Style(Base):
    """
    Represents the style table in the database.

    Attributes:
        id (UUID): The unique identifier for the style.
        created_at (DateTime): The timestamp when the style was created.
        updated_at (DateTime): The timestamp when the style was last updated.
        name (str): The name of the style.
        version (int): The version number of the style.
        category (str): The category of the style.
        category_number (int): The category number of the style.
        style_letter (str): The letter of the style.
        style_guide (str): The guide of the style.
        type (str): The type of the style.
        og_min (int): The minimum original gravity of the style.
        og_max (int): The maximum original gravity of the style.
        fg_min (int): The minimum final gravity of the style.
        fg_max (int): The maximum final gravity of the style.
        ibu_min (int): The minimum IBU of the style.
        ibu_max (int): The maximum IBU of the style.
        color_min (int): The minimum color of the style.
        color_max (int): The maximum color of the style.
        carb_min (int): The minimum carbonation of the style.
        carb_max (int): The maximum carbonation of the style.
        abv_min (int): The minimum ABV of the style.
        abv_max (int): The maximum ABV of the style.
        notes (str): Additional notes about the style.
        profile (str): The profile of the style.
        ingredients (str): The ingredients of the style.
        examples (str): Examples of the style.
        display_og_min (str): Formatted minimum original gravity of the style.
        display_og_max (str): Formatted maximum original gravity of the style.
        display_fg_min (str): Formatted minimum final gravity of the style.
        display_fg_max (str): Formatted maximum final gravity of the style.
        display_color_min (str): Formatted minimum color of the style.
        display_color_max (str): Formatted maximum color of the style.
        og_range (str): The range of original gravity of the style.
        fg_range (str): The range of final gravity of the style.
        ibu_range (str): The range of IBU of the style.
        carb_range (str): The range of carbonation of the style.
        color_range (str): The range of color of the style.
        abv_range (str): The range of ABV of the style.
    """
    __tablename__ = "style"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    name = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    category = Column(String(255), nullable=False)
    category_number = Column(Integer, nullable=False)
    style_letter = Column(String(255), nullable=False)
    style_guide = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    og_min = Column(Integer, nullable=False)
    og_max = Column(Integer, nullable=False)
    fg_min = Column(Integer, nullable=False)
    fg_max = Column(Integer, nullable=False)
    ibu_min = Column(Integer, nullable=False)
    ibu_max = Column(Integer, nullable=False)
    color_min = Column(Integer, nullable=False)
    color_max = Column(Integer, nullable=False)
    carb_min = Column(Integer, nullable=False)
    carb_max = Column(Integer, nullable=False)
    abv_min = Column(Integer, nullable=False)
    abv_max = Column(Integer, nullable=False)
    notes = Column(String(255), nullable=False)
    profile = Column(String(255), nullable=False)
    ingredients = Column(String(255), nullable=False)
    examples = Column(String(255), nullable=False)
    display_og_min = Column(String(255), nullable=False)
    display_og_max = Column(String(255), nullable=False)
    display_fg_min = Column(String(255), nullable=False)
    display_fg_max = Column(String(255), nullable=False)
    display_color_min = Column(String(255), nullable=False)
    display_color_max = Column(String(255), nullable=False)
    og_range = Column(String(255), nullable=False)
    fg_range = Column(String(255), nullable=False)
    ibu_range = Column(String(255), nullable=False)
    carb_range = Column(String(255), nullable=False)
    color_range = Column(String(255), nullable=False)
    abv_range = Column(String(255), nullable=False)

    def __repr__(self):
        return f"Style(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                version={self.version}, \
                category={self.category}, \
                category_number={self.category_number}, \
                style_letter={self.style_letter}, \
                style_guide={self.style_guide}, \
                type={self.type}, \
                og_min={self.og_min}, \
                og_max={self.og_max}, \
                fg_min={self.fg_min}, \
                fg_max={self.fg_max}, \
                ibu_min={self.ibu_min}, \
                ibu_max={self.ibu_max}, \
                color_min={self.color_min}, \
                color_max={self.color_max}, \
                carb_min={self.carb_min}, \
                carb_max={self.carb_max}, \
                abv_min={self.abv_min}, \
                abv_max={self.abv_max}, \
                notes={self.notes}, \
                profile={self.profile}, \
                ingredients={self.ingredients}, \
                examples={self.examples}, \
                display_og_min={self.display_og_min}, \
                display_og_max={self.display_og_max}, \
                display_fg_min={self.display_fg_min}, \
                display_fg_max={self.display_fg_max}, \
                display_color_min={self.display_color_min}, \
                display_color_max={self.display_color_max}, \
                og_range={self.og_range}, \
                fg_range={self.fg_range}, \
                ibu_range={self.ibu_range}, \
                carb_range={self.carb_range}, \
                color_range={self.color_range}, \
                abv_range={self.abv_range})"
