from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from setup import SessionLocal
import database.models as models
import database.schemas as schemas

router = APIRouter()
db = SessionLocal()


@router.post("/recipe", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.Recipe):
    """
    Create a new recipe entry in the database.

    Args:
        recipe (RecipeCreate): The recipe data to be added to the database.

    Returns:
        Recipe: The recipe data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the recipe data to the database.
    """
    new_recipe = models.Recipe(**recipe.dict())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe


@router.get("/recipe/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(recipe_id: UUID):
    """
    Retrieve a recipe entry from the database.

    Args:
        recipe_id (UUID): The unique identifier for the recipe.

    Returns:
        Recipe: The recipe data retrieved from the database.

    Raises:
        HTTPException: If the recipe data with the specified ID does not exist in the database.
    """
    recipe = db.query(models.Recipe).filter(
        models.Recipe.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    return recipe


@router.put("/recipe/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(recipe_id: UUID, recipe: schemas.Recipe):
    """
    Update a recipe entry in the database.

    Args:
        recipe_id (UUID): The unique identifier for the recipe.
        recipe (Recipe): The recipe data to be added to the database.

    Returns:
        Recipe: The updated recipe data.

    Raises:
        HTTPException: If the recipe data with the specified ID does not exist in the database.
    """
    recipe_data = db.query(models.Recipe).filter(
        models.Recipe.id == recipe_id).first()
    if recipe_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    for key, value in recipe.dict().items():
        setattr(recipe_data, key, value)
    db.commit()
    db.refresh(recipe_data)
    return recipe_data


@router.delete("/recipe/{recipe_id}")
def delete_recipe(recipe_id: UUID):
    """
    Delete a recipe entry from the database.

    Args:
        recipe_id (UUID): The unique identifier for the recipe.

    Returns:
        None

    Raises:
        HTTPException: If the recipe data with the specified ID does not exist in the database.
    """
    recipe = db.query(models.Recipe).filter(
        models.Recipe.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    db.delete(recipe)
    db.commit()
    return None
