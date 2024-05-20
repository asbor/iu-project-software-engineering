from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class Recipes(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    version = Column(Integer)
    type = Column(String, nullable=True)
    brewer = Column(String, nullable=True)
    asst_brewer = Column(String, nullable=True)
    batch_size = Column(Float, nullable=True)
    boil_size = Column(Float, nullable=True)
    boil_time = Column(Integer, nullable=True)
    efficiency = Column(Float, nullable=True)
    notes = Column(String, nullable=True)
    taste_notes = Column(String, nullable=True)
    taste_rating = Column(Integer, nullable=True)
    og = Column(Float, nullable=True)
    fg = Column(Float, nullable=True)
    fermentation_stages = Column(Integer, nullable=True)
    primary_age = Column(Integer, nullable=True)
    primary_temp = Column(Float, nullable=True)
    secondary_age = Column(Integer, nullable=True)
    secondary_temp = Column(Float, nullable=True)
    tertiary_age = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)
    age_temp = Column(Float, nullable=True)
    carbonation_used = Column(String, nullable=True)
    est_og = Column(Float, nullable=True)
    est_fg = Column(Float, nullable=True)
    est_color = Column(Float, nullable=True)
    ibu = Column(Float, nullable=True)
    ibu_method = Column(String, nullable=True)
    est_abv = Column(Float, nullable=True)
    abv = Column(Float, nullable=True)
    actual_efficiency = Column(Float, nullable=True)
    calories = Column(Float, nullable=True)
    display_batch_size = Column(String, nullable=True)
    display_boil_size = Column(String, nullable=True)
    display_og = Column(String, nullable=True)
    display_fg = Column(String, nullable=True)
    display_primary_temp = Column(String, nullable=True)
    display_secondary_temp = Column(String, nullable=True)
    display_tertiary_temp = Column(String, nullable=True)
    display_age_temp = Column(String, nullable=True)

    hops = relationship("RecipeHops", back_populates="recipe")
