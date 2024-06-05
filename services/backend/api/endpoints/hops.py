# api/endpoints/hops.py



from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from database import get_db

import Database.Models as models

import Database.Schemas as schemas

from typing import List



router = APIRouter()



# Recipe Hops Endpoints





@router.get("/recipes/hops", response_model=List[schemas.RecipeHop])

async def get_all_recipe_hops(db: Session = Depends(get_db)):

    hops = db.query(models.RecipeHop).all()

    return hops





# Inventory Hops Endpoints





@router.get("/inventory/hops", response_model=List[schemas.InventoryHop])

async def get_all_inventory_hops(db: Session = Depends(get_db)):

    hops = db.query(models.InventoryHop).all()

    return hops





@router.get("/inventory/hops/{hop_id}", response_model=schemas.InventoryHop)

async def get_inventory_hop(hop_id: int, db: Session = Depends(get_db)):

    hop = (

        db.query(models.InventoryHop)

        .filter(models.InventoryHop.id == hop_id)

        .first()

    )

    if not hop:

        raise HTTPException(status_code=404, detail="Hop not found")

    return hop





@router.post("/inventory/hops", response_model=schemas.InventoryHop)

async def create_inventory_hop(

    hop: schemas.InventoryHopCreate, db: Session = Depends(get_db)

):

    try:

        db_hop = models.InventoryHop(**hop.dict())

        db.add(db_hop)

        db.commit()

        db.refresh(db_hop)

        return db_hop

    except Exception as e:

        raise HTTPException(status_code=400, detail=str(e))





@router.delete("/inventory/hops/{id}", response_model=schemas.InventoryHop)

async def delete_inventory_hop(id: int, db: Session = Depends(get_db)):

    hop = (

        db.query(models.InventoryHop)

        .filter(models.InventoryHop.id == id)

        .first()

    )

    if not hop:

        raise HTTPException(status_code=404, detail="Hop not found")

    db.delete(hop)

    db.commit()

    return hop





@router.put("/inventory/hops/{id}", response_model=schemas.InventoryHop)

async def update_inventory_hop(

    id: int, hop: schemas.InventoryHopCreate, db: Session = Depends(get_db)

):

    db_hop = (

        db.query(models.InventoryHop)

        .filter(models.InventoryHop.id == id)

        .first()

    )

    if not db_hop:

        raise HTTPException(status_code=404, detail="Hop not found")

    for key, value in hop.dict().items():

        setattr(db_hop, key, value)

    db.commit()

    db.refresh(db_hop)

    return db_hop
