from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import Database.Models as models
import Database.Schemas as schemas

router = APIRouter()


@router.post("/recipes")
async def create_recipe(recipe: schemas.RecipeBase, db: Session = Depends(get_db)):
    # Exclude the related fields when creating the Recipes instance
    db_recipe = models.Recipes(
        **recipe.dict(exclude={'hops', 'fermentables', 'yeasts', 'miscs'}))
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # Add hops to the recipe
    for hop_data in recipe.hops:
        db_hop = models.Hops(**hop_data.dict(), recipe_id=db_recipe.id)
        db.add(db_hop)
        db.commit()
        db.refresh(db_hop)

    # Add fermentables to the recipe
    for fermentable_data in recipe.fermentables:
        db_fermentable = models.Fermentables(
            **fermentable_data.dict(), recipe_id=db_recipe.id)
        db.add(db_fermentable)
        db.commit()
        db.refresh(db_fermentable)

    # Add miscs to the recipe
    for misc_data in recipe.miscs:
        db_misc = models.Miscs(**misc_data.dict(), recipe_id=db_recipe.id)
        db.add(db_misc)
        db.commit()
        db.refresh(db_misc)

    # Add yeasts to the recipe
    for yeast_data in recipe.yeasts:
        db_yeast = models.Yeasts(**yeast_data.dict(), recipe_id=db_recipe.id)
        db.add(db_yeast)
        db.commit()
        db.refresh(db_yeast)

    return db_recipe
