from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

from Database.Schemas.recipes import RecipeBase

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()


@router.post("/recipes")
async def create_recipes(recipe: RecipeBase, db: db_dependency):
    db_recipe = models.Recipes(
        name=recipe.name,
        version=recipe.version,
        type=recipe.type,
        brewer=recipe.brewer,
        asst_brewer=recipe.asst_brewer,
        batch_size=recipe.batch_size,
        boil_size=recipe.boil_size,
        boil_time=recipe.boil_time,
        efficiency=recipe.efficiency,
        notes=recipe.notes,
        taste_notes=recipe.taste_notes,
        taste_rating=recipe.taste_rating,
        og=recipe.og,
        fg=recipe.fg,
        fermentation_stages=recipe.fermentation_stages,
        primary_age=recipe.primary_age,
        primary_temp=recipe.primary_temp,
        secondary_age=recipe.secondary_age,
        secondary_temp=recipe.secondary_temp,
        tertiary_age=recipe.tertiary_age,
        tertiary_temp=recipe.tertiary_temp,
        age=recipe.age,
        age_temp=recipe.age_temp,
        carbonation_used=recipe.carbonation_used,
        est_og=recipe.est_og,
        est_fg=recipe.est_fg,
        est_color=recipe.est_color,
        ibu=recipe.ibu,
        ibu_method=recipe.ibu_method,
        est_abv=recipe.est_abv,
        abv=recipe.abv,
        actual_efficiency=recipe.actual_efficiency,
        calories=recipe.calories,
        display_batch_size=recipe.display_batch_size,
        display_boil_size=recipe.display_boil_size,
        display_og=recipe.display_og,
        display_fg=recipe.display_fg,
        display_primary_temp=recipe.display_primary_temp,
        display_secondary_temp=recipe.display_secondary_temp,
        display_tertiary_temp=recipe.display_tertiary_temp,
    )

    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    for hop in recipe.hops:
        db_hop = models.Hops(
            recipe_id=db_recipe.id,
            name=hop.name,
            version=hop.version,
            origin=hop.origin,
            alpha=hop.alpha,
            amount=hop.amount,
            use=hop.use,
            time=hop.time,
            notes=hop.notes,
            type=hop.type,
            form=hop.form,
            beta=hop.beta,
            hsi=hop.hsi,
            display_amount=hop.display_amount,
            inventory=hop.inventory,
            display_time=hop.display_time,
        )

        db.add(db_hop)
        db.commit()
        db.refresh(db_hop)
