# api/endpoints/miscs.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import Database.Models as models
import Database.Schemas as schemas
from typing import List

router = APIRouter()

# Recipe Miscs Endpoints

@router.get("/recipes/miscs", response_model=List[schemas.RecipeMisc])
async def get_all_recipe_miscs(db: Session = Depends(get_db)):
    miscs = db.query(models.RecipeMisc).all()
    return miscs

# Inventory Miscs Endpoints

@router.get("/inventory/miscs", response_model=List[schemas.InventoryMisc])
async def get_all_inventory_miscs(db: Session = Depends(get_db)):
    miscs = db.query(models.InventoryMisc).all()
    return miscs

@router.get("/inventory/miscs/{misc_id}", response_model=schemas.InventoryMisc)
async def get_inventory_misc(misc_id: int, db: Session = Depends(get_db)):
    misc = (
        db.query(models.InventoryMisc)
        .filter(models.InventoryMisc.id == misc_id)
        .first()
    )
    if not misc:
        raise HTTPException(status_code=404, detail="Misc not found")
    return misc

@router.post("/inventory/miscs", response_model=schemas.InventoryMisc)
async def create_inventory_misc(
    misc: schemas.InventoryMiscCreate, db: Session = Depends(get_db)
):
    try:
        db_misc = models.InventoryMisc(**misc.dict())
        db.add(db_misc)
        db.commit()
        db.refresh(db_misc)
        return db_misc
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/inventory/miscs/{id}", response_model=schemas.InventoryMisc)
async def delete_inventory_misc(id: int, db: Session = Depends(get_db)):
    misc = (
        db.query(models.InventoryMisc)
        .filter(models.InventoryMisc.id == id)
        .first()
    )
    if not misc:
        raise HTTPException(status_code=404, detail="Misc not found")
    db.delete(misc)
    db.commit()
    return misc

@router.put("/inventory/miscs/{id}", response_model=schemas.InventoryMisc)
async def update_inventory_misc(
    id: int, misc: schemas.InventoryMiscCreate, db: Session = Depends(get_db)
):
    db_misc = (
        db.query(models.InventoryMisc)
        .filter(models.InventoryMisc.id == id)
        .first()
    )
    if not db_misc:
        raise HTTPException(status_code=404, detail="Misc not found")
    for key, value in misc.dict().items():
        setattr(db_misc, key, value)
    db.commit()
    db.refresh(db_misc)
    return db_misc
