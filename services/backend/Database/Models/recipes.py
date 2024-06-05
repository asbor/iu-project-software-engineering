# services/backend/Database/Models/recipes.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Recipes(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_batch = Column(Boolean, default=False)
    origin_recipe_id = Column(Integer,
                              ForeignKey("recipes.id"),
                              nullable=True)
    origin_recipe = relationship("Recipes", remote_side=[id])
    version = Column(Integer)
    type = Column(String)
    brewer = Column(String)
    asst_brewer = Column(String)
    batch_size = Column(Float)
    boil_size = Column(Float)
    boil_time = Column(Integer)
    efficiency = Column(Float)
    notes = Column(String)
    taste_notes = Column(String)
    taste_rating = Column(Integer)
    og = Column(Float)
    fg = Column(Float)
    fermentation_stages = Column(Integer)
    primary_age = Column(Integer)
    primary_temp = Column(Float)
    secondary_age = Column(Integer)
    secondary_temp = Column(Float)
    tertiary_age = Column(Integer)
    age = Column(Integer)
    age_temp = Column(Float)
    carbonation_used = Column(String)
    est_og = Column(Float)
    est_fg = Column(Float)
    est_color = Column(Float)
    ibu = Column(Float)
    ibu_method = Column(String)
    est_abv = Column(Float)
    abv = Column(Float)
    actual_efficiency = Column(Float)
    calories = Column(Float)
    display_batch_size = Column(String)
    display_boil_size = Column(String)
    display_og = Column(String)
    display_fg = Column(String)
    display_primary_temp = Column(String)
    display_secondary_temp = Column(String)
    display_tertiary_temp = Column(String)
    display_age_temp = Column(String)
    hops = relationship("RecipeHop", back_populates="recipe")
    fermentables = relationship("RecipeFermentable",
                                back_populates="recipe")
    yeasts = relationship("RecipeYeast", back_populates="recipe")
    miscs = relationship("RecipeMisc", back_populates="recipe")
    batches = relationship("Batches", back_populates="recipe")
