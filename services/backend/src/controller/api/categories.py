from fastapi import APIRouter, HTTPException, status
import uuid
from src.model.database import SessionLocal
import src.model.db_models as models
import src.data.schemas as schemas

router = APIRouter()

db = SessionLocal()

# create a new category


@router.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.Category):
    if db.query(models.Category).filter(models.Category.name == category.name).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Category already exists")

    new_category = models.Category(
        id=category.id,
        name=category.name,
        created_at=category.created_at,
        updated_at=category.updated_at
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


# get all categories
@router.get("/categories", response_model=list[schemas.Category])
def get_all_categories():
    categories = db.query(models.Category).all()
    return categories

# get a category by id


@router.get("/categories/{categoryId}", response_model=schemas.Category)
def get_category(categoryId: uuid.UUID):
    category = db.query(models.Category).filter(
        models.Category.id == categoryId).first()
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category

# Update a category


@router.patch("/categories/{categoryId}", status_code=status.HTTP_200_OK)
async def patch_category(categoryId: uuid.UUID, category: schemas.Category):
    db_category = db.query(models.Category).filter(
        models.Category.id == categoryId).first()

    # The category id must exist in the database
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    if category.name is not None:
        db_category.name = category.name                # type: ignore
    if category.created_at is not None:
        db_category.created_at = category.created_at    # type: ignore
    if category.updated_at is not None:
        db_category.updated_at = category.updated_at    # type: ignore

    db.commit()
    db.refresh(db_category)

    return db_category

# Delete a category


@router.delete("/categories/{categoryId}", status_code=status.HTTP_200_OK)
async def delete_category(categoryId: uuid.UUID):
    db_category = db.query(models.Category).filter(
        models.Category.id == categoryId).first()

    # The category id must exist in the database
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    db.delete(db_category)
    db.commit()

    return db_category
