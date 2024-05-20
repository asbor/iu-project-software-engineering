from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import Database.Models as models
from Database.Schemas.recipes import RecipeBase

router = APIRouter()


@router.get("/recipes", response_model=list[RecipeBase])
async def get_all_recipes(db: Session = Depends(get_db)):
    recipes = db.query(models.Recipes).all()
    return recipes


@router.post("/recipes")
async def create_recipe(recipe: RecipeBase, db: Session = Depends(get_db)):
    # Create the main recipe entry
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
        display_age_temp=recipe.display_age_temp
    )

    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # Handle hops
    for hop in recipe.hops:
        # Check if the master hop already exists
        master_hop = db.query(models.MasterHops).filter_by(
            name=hop.name).first()
        if not master_hop:
            # If not, create a new master hop entry
            master_hop = models.MasterHops(
                name=hop.name,
                origin=hop.origin,
                alpha=hop.alpha,
                type=hop.type,
                form=hop.form,
                beta=hop.beta,
                hsi=hop.hsi
            )
            db.add(master_hop)
            db.commit()
            db.refresh(master_hop)

        # Now use the master_hop_id for the recipe hop
        db_recipe_hop = models.RecipeHops(
            master_hop_id=master_hop.id,
            amount=hop.amount,
            use=hop.use,
            time=hop.time,
            notes=hop.notes,
            display_amount=hop.display_amount,
            inventory=hop.inventory,
            display_time=hop.display_time,
            recipe_id=db_recipe.id
        )
        db.add(db_recipe_hop)

    db.commit()

    return db_recipe
