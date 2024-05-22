from fastapi import APIRouter, HTTPException, status
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()


# Recipe Miscs Endpoints
@router.get("/recipes/miscs")
async def get_all_recipe_miscs(db: db_dependency):
    miscs = db.query(models.RecipeMisc).all()
    return miscs

# Inventory Miscs Endpoints


@router.get("/inventory/miscs")
async def get_all_inventory_miscs(db: db_dependency):
    miscs = db.query(models.InventoryMisc).all()
    return miscs
