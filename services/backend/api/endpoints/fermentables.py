from fastapi import APIRouter, HTTPException, status
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()

# Recipe Fermentables Endpoints


@router.get("/recipes/fermentables")
async def get_all_recipe_fermentables(db: db_dependency):
    fermentables = db.query(models.RecipeFermentable).all()
    return fermentables

# Inventory Fermentables Endpoints


@router.get("/inventory/fermentables")
async def get_all_inventory_fermentables(db: db_dependency):
    fermentables = db.query(models.InventoryFermentable).all()
    return fermentables
