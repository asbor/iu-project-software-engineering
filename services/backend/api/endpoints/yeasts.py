# api/endpoints/yeasts.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import Database.Models as models
import Database.Schemas as schemas
from typing import List

router = APIRouter()

# Recipe Yeasts Endpoints


@router.get("/recipes/yeasts", response_model=List[schemas.RecipeYeast])
async def get_all_recipe_yeasts(db: Session = Depends(get_db)):
    yeasts = db.query(models.RecipeYeast).all()
    return yeasts


# Inventory Yeasts Endpoints


@router.get("/inventory/yeasts", response_model=List[schemas.InventoryYeast])
async def get_all_inventory_yeasts(db: Session = Depends(get_db)):
    yeasts = db.query(models.InventoryYeast).all()
    return yeasts


@router.get(
    "/inventory/yeasts/{yeast_id}", response_model=schemas.InventoryYeast
)
async def get_inventory_yeast(yeast_id: int, db: Session = Depends(get_db)):
    yeast = (
        db.query(models.InventoryYeast)
        .filter(models.InventoryYeast.id == yeast_id)
        .first()
    )
    if not yeast:
        raise HTTPException(status_code=404, detail="Yeast not found")
    return yeast


@router.post("/inventory/yeasts", response_model=schemas.InventoryYeast)
async def create_inventory_yeast(
    yeast: schemas.InventoryYeastCreate, db: Session = Depends(get_db)
):
    try:
        db_yeast = models.InventoryYeast(**yeast.dict())
        db.add(db_yeast)
        db.commit()
        db.refresh(db_yeast)
        return db_yeast
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/inventory/yeasts/{id}", response_model=schemas.InventoryYeast)
async def delete_inventory_yeast(id: int, db: Session = Depends(get_db)):
    yeast = (
        db.query(models.InventoryYeast)
        .filter(models.InventoryYeast.id == id)
        .first()
    )
    if not yeast:
        raise HTTPException(status_code=404, detail="Yeast not found")
    db.delete(yeast)
    db.commit()
    return yeast


@router.put("/inventory/yeasts/{id}", response_model=schemas.InventoryYeast)
async def update_inventory_yeast(
    id: int, yeast: schemas.InventoryYeastCreate, db: Session = Depends(get_db)
):
    db_yeast = (
        db.query(models.InventoryYeast)
        .filter(models.InventoryYeast.id == id)
        .first()
    )
    if not db_yeast:
        raise HTTPException(status_code=404, detail="Yeast not found")
    for key, value in yeast.dict().items():
        setattr(db_yeast, key, value)
    db.commit()
    db.refresh(db_yeast)
    return db_yeast
