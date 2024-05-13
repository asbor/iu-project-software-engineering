from datetime import datetime, timezone, date
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Recipe(Base):
    """
    A class representing the Recipe table in the database.

    This table stores information about brewing recipe, including details about
    ingredients, process, and measurements.

    Attributes:
        id (UUID): The unique identifier for the recipe.
        created_at (DateTime): The timestamp when the recipe was created.
        updated_at (DateTime): The timestamp when the recipe was last updated.
        name (str): The name of the recipe.
        type (str): The type or style of the recipe.
        brewer (str): The name of the primary brewer.
        asst_brewer (str): The name of the assistant brewer.
        batch_size (int): The size of the batch in liters.
        boil_size (int): The size of the boil in liters.
        boil_time (int): The duration of the boil in minutes.
        efficiency (int): The brewing efficiency as a percentage.
        hop (relationship): Relationship to the Hop table.
        fermentable (relationship): Relationship to the fermentable table.
        # misc (relationship): Relationship to the Misc table.
        yeast (relationship): Relationship to the Yeast table.
        #water (relationship): Relationship to the Water table.
        style (relationship): Relationship to the Style table.
        equipment (relationship): Relationship to the Equipment table.
        mash (str): Details about the mashing process.
        notes (str): General notes about the recipe.
        taste_notes (str): Notes about the taste of the final product.
        taste_rating (int): A rating for the taste of the final product.
        og (int): Original gravity of the beer.
        fg (int): Final gravity of the beer.
        carbonation (int): Level of carbonation.
        fermentation_stages (int): Number of fermentation stages.
        primary_age (int): Age of the beer during primary fermentation.
        primary_temp (int): Temperature during primary fermentation.
        secondary_age (int): Age of the beer during secondary fermentation.
        secondary_temp (int): Temperature during secondary fermentation.
        tertiary_age (int): Age of the beer during tertiary fermentation.
        age (int): Age of the beer in days.
        age_temp (int): Temperature during aging.
        carbonation_used (str): Details about carbonation used.
        date (Date): The date when the recipe was created.
        est_og (int): Estimated original gravity.
        est_fg (int): Estimated final gravity.
        est_color (int): Estimated color of the beer.
        ibu (int): International Bitterness Units.
        ibu_method (str): Method used to calculate IBU.
        est_abv (int): Estimated alcohol by volume.
        abv (int): Actual alcohol by volume.
        actual_efficiency (int): Actual brewing efficiency.
        calories (int): Estimated calories per serving.
        display_batch_size (str): Formatted batch size.
        display_boil_size (str): Formatted boil size.
        display_og (str): Formatted original gravity.
        display_fg (str): Formatted final gravity.
        display_primary_temp (str): Formatted primary fermentation temperature.
        display_secondary_temp (str): Formatted secondary fermentation temperature.
        display_tertiary_temp (str): Formatted tertiary fermentation temperature.
    """

    __tablename__ = "recipe"

    id = Column(UUID, primary_key=True, unique=True)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=True)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=True)
    name = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    brewer = Column(String(255), nullable=True)
    asst_brewer = Column(String(255), nullable=True)
    batch_size = Column(Integer, nullable=True)
    boil_size = Column(Integer, nullable=True)
    boil_time = Column(Integer, nullable=True)
    efficiency = Column(Integer, nullable=True)

    mash = Column(String(255), nullable=True)
    notes = Column(String(255), nullable=True)
    taste_notes = Column(String(255), nullable=True)
    taste_rating = Column(Integer, nullable=True)
    og = Column(Integer, nullable=True)
    fg = Column(Integer, nullable=True)
    carbonation = Column(Integer, nullable=True)
    fermentation_stages = Column(Integer, nullable=True)
    primary_age = Column(Integer, nullable=True)
    primary_temp = Column(Integer, nullable=True)
    secondary_age = Column(Integer, nullable=True)
    secondary_temp = Column(Integer, nullable=True)
    tertiary_age = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)
    age_temp = Column(Integer, nullable=True)
    carbonation_used = Column(String(255), nullable=True)
    date = Column(Date, default=date.today, nullable=True)
    est_og = Column(Integer, nullable=True)
    est_fg = Column(Integer, nullable=True)
    est_color = Column(Integer, nullable=True)
    ibu = Column(Integer, nullable=True)
    ibu_method = Column(String(255), nullable=True)
    est_abv = Column(Integer, nullable=True)
    abv = Column(Integer, nullable=True)
    actual_efficiency = Column(Integer, nullable=True)
    calories = Column(Integer, nullable=True)
    display_batch_size = Column(String(255), nullable=True)
    display_boil_size = Column(String(255), nullable=True)
    display_og = Column(String(255), nullable=True)
    display_fg = Column(String(255), nullable=True)
    display_primary_temp = Column(String(255), nullable=True)
    display_secondary_temp = Column(String(255), nullable=True)
    display_tertiary_temp = Column(String(255), nullable=True)
    display_age_temp = Column(String(255), nullable=True)

    # Relationships
    # hop = relationship("Hop", back_populates="recipe")
    # fermentable = relationship("Fermentable", back_populates="recipe")
    # yeast = relationship("Yeast", back_populates="recipe")
    # misc = relationship("Misc", back_populates="recipe")
    # water = relationship("Water", back_populates="recipe")
    # style = relationship("Style", back_populates="recipe")
    # equipment = relationship("Equipment", back_populates="recipe")

    def __repr__(self):
        return f"Recipe(id={self.id}, \
                created_at={self.created_at}, \
                updated_at={self.updated_at}, \
                name={self.name}, \
                type={self.type}, \
                brewer={self.brewer}, \
                asst_brewer={self.asst_brewer}, \
                batch_size={self.batch_size}, \
                boil_size={self.boil_size}, \
                boil_time={self.boil_time}, \
                efficiency={self.efficiency}, \
                mash={self.mash}, \
                notes={self.notes}, \
                taste_notes={self.taste_notes}, \
                taste_rating={self.taste_rating}, \
                og={self.og}, \
                fg={self.fg}, \
                carbonation={self.carbonation}, \
                fermentation_stages={self.fermentation_stages}, \
                primary_age={self.primary_age}, \
                primary_temp={self.primary_temp}, \
                secondary_age={self.secondary_age}, \
                secondary_temp={self.secondary_temp}, \
                tertiary_age={self.tertiary_age}, \
                age={self.age}, \
                age_temp={self.age_temp}, \
                carbonation_used={self.carbonation_used}, \
                date={self.date}, \
                est_og={self.est_og}, \
                est_fg={self.est_fg}, \
                est_color={self.est_color}, \
                ibu={self.ibu}, \
                ibu_method={self.ibu_method}, \
                est_abv={self.est_abv}, \
                abv={self.abv}, \
                actual_efficiency={self.actual_efficiency}, \
                calories={self.calories}, \
                display_batch_size={self.display_batch_size}, \
                display_boil_size={self.display_boil_size}, \
                display_og={self.display_og}, \
                display_fg={self.display_fg}, \
                display_primary_temp={self.display_primary_temp}, \
                display_secondary_temp={self.display_secondary_temp}, \
                display_tertiary_temp={self.display_tertiary_temp}, \
                display_age_temp={self.display_age_temp}"
