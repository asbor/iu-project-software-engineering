from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from database import get_db
import Database.Models as models
import Database.Schemas as schemas

router = APIRouter()


@router.get("/recipes")
async def get_all_recipes(db: Session = Depends(get_db)):
    """
    This endpoint returns all the recipes stored in the database.
    """
    recipes = db.query(models.Recipes).options(
        joinedload(models.Recipes.hops),
        joinedload(models.Recipes.fermentables),
        joinedload(models.Recipes.yeasts),
        joinedload(models.Recipes.miscs)
    ).all()
    return recipes


@router.get("/recipes/{recipe_id}")
async def get_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    """
    This endpoint returns a recipe by its ID.
    """
    recipe = db.query(models.Recipes).options(
        joinedload(models.Recipes.hops),
        joinedload(models.Recipes.fermentables),
        joinedload(models.Recipes.yeasts),
        joinedload(models.Recipes.miscs)
    ).filter(models.Recipes.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.post("/recipes")
async def create_recipe(recipe: schemas.RecipeBase, db: Session = Depends(get_db)):
    """
    This endpoint creates a new recipe in the database.
    """
    # Check if the recipe already exists
    existing_recipe = db.query(models.Recipes).filter(
        models.Recipes.name == recipe.name).first()
    if existing_recipe:
        raise HTTPException(
            status_code=400, detail="Recipe with this name already exists")

    # Exclude the related fields when creating the Recipes instance
    db_recipe = models.Recipes(
        **recipe.dict(exclude={'hops', 'fermentables', 'yeasts', 'miscs'})
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # Add hops to the recipe
    for hop_data in recipe.hops:
        db_hop = models.Hops(**hop_data.dict(), recipe_id=db_recipe.id)
        db.add(db_hop)

    # Add fermentables to the recipe
    for fermentable_data in recipe.fermentables:
        db_fermentable = models.Fermentables(
            **fermentable_data.dict(), recipe_id=db_recipe.id)
        db.add(db_fermentable)

    # Add miscs to the recipe
    for misc_data in recipe.miscs:
        db_misc = models.Miscs(**misc_data.dict(), recipe_id=db_recipe.id)
        db.add(db_misc)

    # Add yeasts to the recipe
    for yeast_data in recipe.yeasts:
        db_yeast = models.Yeasts(**yeast_data.dict(), recipe_id=db_recipe.id)
        db.add(db_yeast)

    db.commit()

    return db_recipe


@router.put("/recipes/{recipe_id}")
async def update_recipe(recipe_id: int, recipe: schemas.RecipeBase, db: Session = Depends(get_db)):
    """
    This endpoint updates a recipe by its ID.
    """
    db_recipe = db.query(models.Recipes).filter(
        models.Recipes.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Update the recipe
    for key, value in recipe.dict(exclude={'hops', 'fermentables', 'yeasts', 'miscs'}).items():
        setattr(db_recipe, key, value)

    # Update hops
    db.query(models.Hops).filter(models.Hops.recipe_id == recipe_id).delete()
    for hop_data in recipe.hops:
        db_hop = models.Hops(**hop_data.dict(), recipe_id=recipe_id)
        db.add(db_hop)

    # Update fermentables
    db.query(models.Fermentables).filter(
        models.Fermentables.recipe_id == recipe_id).delete()
    for fermentable_data in recipe.fermentables:
        db_fermentable = models.Fermentables(
            **fermentable_data.dict(), recipe_id=recipe_id)
        db.add(db_fermentable)

    # Update miscs
    db.query(models.Miscs).filter(models.Miscs.recipe_id == recipe_id).delete()
    for misc_data in recipe.miscs:
        db_misc = models.Miscs(**misc_data.dict(), recipe_id=recipe_id)
        db.add(db_misc)

    # Update yeasts
    db.query(models.Yeasts).filter(
        models.Yeasts.recipe_id == recipe_id).delete()
    for yeast_data in recipe.yeasts:
        db_yeast = models.Yeasts(**yeast_data.dict(), recipe_id=recipe_id)
        db.add(db_yeast)

    db.commit()
    return db_recipe


@router.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """
    This endpoint deletes a recipe by its ID.
    """
    db_recipe = db.query(models.Recipes).filter(
        models.Recipes.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    db.query(models.Hops).filter(models.Hops.recipe_id == recipe_id).delete()
    db.query(models.Fermentables).filter(
        models.Fermentables.recipe_id == recipe_id).delete()
    db.query(models.Miscs).filter(models.Miscs.recipe_id == recipe_id).delete()
    db.query(models.Yeasts).filter(
        models.Yeasts.recipe_id == recipe_id).delete()
    db.delete(db_recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}
