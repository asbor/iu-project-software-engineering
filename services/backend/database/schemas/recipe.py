from .base import BaseModel
from typing import List
import uuid
from datetime import datetime, date


class Recipe(BaseModel):
    """
    A class representing the Recipe table in the database.

    This table stores information about brewing recipe, including details about
    ingredients, process, and measurements.

    Attributes:
        id (UUID): The unique identifier for the recipe.
        created_at (DateTime): The timestamp when the recipe was created.
        updated_at (DateTime): The timestamp when the recipe was last updated.
        name (str): The name of the recipe.
        version (int): The version number of the recipe.
        type (str): The type or style of the recipe.
        brewer (str): The name of the primary brewer.
        asst_brewer (str): The name of the assistant brewer.
        batch_size (int): The size of the batch in liters.
        boil_size (int): The size of the boil in liters.
        boil_time (int): The duration of the boil in minutes.
        efficiency (int): The brewing efficiency as a percentage.
        hop (relationship): Relationship to the Hop table.
        fermentable (relationship): Relationship to the Fermentable table.
        misc (relationship): Relationship to the Misc table.
        yeast (relationship): Relationship to the Yeast table.
        water (relationship): Relationship to the Water table.
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

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    name: str
    version: int
    type: str
    brewer: str
    asst_brewer: str
    batch_size: int
    boil_size: int
    boil_time: int
    efficiency: int
    hop: List[uuid.UUID]
    fermentable: List[uuid.UUID]
    misc: List[uuid.UUID]
    yeast: List[uuid.UUID]
    water: List[uuid.UUID]
    style: List[uuid.UUID]
    equipment: List[uuid.UUID]
    mash: str
    notes: str
    taste_notes: str
    taste_rating: int
    og: int
    fg: int
    carbonation: int
    fermentation_stages: int
    primary_age: int
    primary_temp: int
    secondary_age: int
    secondary_temp: int
    tertiary_age: int
    age: int
    age_temp: int
    carbonation_used: str
    date: date
    est_og: int
    est_fg: int
    est_color: int
    ibu: int
    ibu_method: str
    est_abv: int
    abv: int
    actual_efficiency: int
    calories: int
    display_batch_size: str
    display_boil_size: str
    display_og: str
    display_fg: str
    display_primary_temp: str
    display_secondary_temp: str
    display_tertiary_temp: str

    class Config:
        orm_mode = True
