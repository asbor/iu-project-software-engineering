# api/endpoints/recipes.py


from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from database import get_db
import Database.Models as models
import Database.Schemas as schemas

router = APIRouter()

# Get all recipes



@router.get("/recipes")
async def get_all_recipes(db: Session = Depends(get_db)):
    """
This endpoint returns all the recipes stored in the database.

    """
    recipes = (
        db.query(models.Recipes)
        .options(
            joinedload(models.Recipes.hops),
            joinedload(models.Recipes.fermentables),
            joinedload(models.Recipes.yeasts),
            joinedload(models.Recipes.miscs),
        )
        .all()
    )
    return recipes


# Get a recipe by ID



@router.get("/recipes/{recipe_id}")
async def get_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    """
This endpoint returns a recipe by its ID.

    """
    recipe = (
        db.query(models.Recipes)
        .options(
            joinedload(models.Recipes.hops),
            joinedload(models.Recipes.fermentables),
            joinedload(models.Recipes.yeasts),
            joinedload(models.Recipes.miscs),
        )
        .filter(models.Recipes.id == recipe_id)
        .first()
    )
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


# Create a new recipe



@router.post("/recipes")
async def create_recipe(
    recipe: schemas.RecipeBase, db: Session = Depends(get_db)
):
    """
This endpoint creates a new recipe in the database.

    """
# Check if the recipe already exists


    existing_recipe = (
        db.query(models.Recipes)
        .filter(models.Recipes.name == recipe.name)
        .first()
    )
    if existing_recipe:
        raise HTTPException(
            status_code=400, detail="Recipe with this name already exists"
        )
# Exclude the related fields when creating the Recipes instance


    db_recipe = models.Recipes(
        **recipe.dict(exclude={"hops", "fermentables", "yeasts", "miscs"})
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
# Add hops to the recipe


    for hop_data in recipe.hops:
        db_hop = models.RecipeHop(**hop_data.dict(), recipe_id=db_recipe.id)
        db.add(db_hop)
# Add fermentables to the recipe


    for fermentable_data in recipe.fermentables:
        db_fermentable = models.RecipeFermentable(
            **fermentable_data.dict(), recipe_id=db_recipe.id
        )
        db.add(db_fermentable)
# Add miscs to the recipe


    for misc_data in recipe.miscs:
        db_misc = models.RecipeMisc(**misc_data.dict(), recipe_id=db_recipe.id)
        db.add(db_misc)
# Add yeasts to the recipe


    for yeast_data in recipe.yeasts:
        db_yeast = models.RecipeYeast(
            **yeast_data.dict(), recipe_id=db_recipe.id
        )
        db.add(db_yeast)
    db.commit()
    return db_recipe


# Update a recipe by ID



@router.put("/recipes/{recipe_id}")
async def update_recipe(
    recipe_id: int, recipe: schemas.RecipeBase, db: Session = Depends(get_db)
):
    """
This endpoint updates a recipe by its ID.

    """
    db_recipe = (
        db.query(models.Recipes).filter(models.Recipes.id == recipe_id).first()
    )
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
# Update the recipe


    for key, value in recipe.dict(
        exclude={"hops", "fermentables", "yeasts", "miscs"}
    ).items():
        setattr(db_recipe, key, value)
# Update hops


    db.query(models.RecipeHop).filter(
        models.RecipeHop.recipe_id == recipe_id
    ).delete()
    for hop_data in recipe.hops:
        db_hop = models.RecipeHop(**hop_data.dict(), recipe_id=recipe_id)
        db.add(db_hop)
# Update fermentables


    db.query(models.RecipeFermentable).filter(
        models.RecipeFermentable.recipe_id == recipe_id
    ).delete()
    for fermentable_data in recipe.fermentables:
        db_fermentable = models.RecipeFermentable(
            **fermentable_data.dict(), recipe_id=recipe_id
        )
        db.add(db_fermentable)
# Update miscs


    db.query(models.RecipeMisc).filter(
        models.RecipeMisc.recipe_id == recipe_id
    ).delete()
    for misc_data in recipe.miscs:
        db_misc = models.RecipeMisc(**misc_data.dict(), recipe_id=recipe_id)
        db.add(db_misc)
# Update yeasts


    db.query(models.RecipeYeast).filter(
        models.RecipeYeast.recipe_id == recipe_id
    ).delete()
    for yeast_data in recipe.yeasts:
        db_yeast = models.RecipeYeast(**yeast_data.dict(), recipe_id=recipe_id)
        db.add(db_yeast)
    db.commit()
    return db_recipe


# Delete a recipe by ID



@router.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """
This endpoint deletes a recipe by its ID.

    """
    db_recipe = (
        db.query(models.Recipes).filter(models.Recipes.id == recipe_id).first()
    )
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.query(models.RecipeHop).filter(
        models.RecipeHop.recipe_id == recipe_id
    ).delete()
    db.query(models.RecipeFermentable).filter(
        models.RecipeFermentable.recipe_id == recipe_id
    ).delete()
    db.query(models.RecipeMisc).filter(
        models.RecipeMisc.recipe_id == recipe_id
    ).delete()
    db.query(models.RecipeYeast).filter(
        models.RecipeYeast.recipe_id == recipe_id
    ).delete()
    db.delete(db_recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}
