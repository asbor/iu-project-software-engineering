from fastapi import APIRouter, HTTPException, status
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()


# Recipe Yeasts Endpoints
@router.get("/recipes/yeasts")
async def get_all_recipe_yeasts(db: db_dependency):
    yeasts = db.query(models.RecipeYeast).all()
    return yeasts

# Inventory Yeasts Endpoints


@router.get("/inventory/yeasts")
async def get_all_inventory_yeasts(db: db_dependency):
    yeasts = db.query(models.InventoryYeast).all()
    return yeasts
