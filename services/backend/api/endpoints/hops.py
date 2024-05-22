from fastapi import APIRouter, HTTPException, status
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()

# Recipe Hops Endpoints


@router.get("/recipes/hops")
async def get_all_recipe_hops(db: db_dependency):
    hops = db.query(models.RecipeHop).all()
    return hops

# Inventory Hops Endpoints


@router.get("/inventory/hops")
async def get_all_inventory_hops(db: db_dependency):
    hops = db.query(models.InventoryHop).all()
    return hops
