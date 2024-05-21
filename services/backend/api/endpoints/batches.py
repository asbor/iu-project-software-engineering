# api/endpoints/batches.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import Database.Models as models
import Database.Schemas as schemas
from typing import List

router = APIRouter()


@router.post("/batches")
def create_batch(batch: schemas.BatchBase, db: Session = Depends(get_db)):
    db_recipe = db.query(models.Recipes).filter(
        models.Recipes.id == batch.recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    db_batch = models.Batches(recipe_id=batch.recipe_id,
                              batch_name=batch.batch_name,
                              batch_size=batch.batch_size)
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch


@router.get("/batches")
def get_batches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    batches = db.query(models.Batches).offset(skip).limit(limit).all()
    return batches


@router.get("/batches/{batch_id}")
def get_batch(batch_id: int, db: Session = Depends(get_db)):
    batch = db.query(models.Batches).filter(
        models.Batches.id == batch_id).first()
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch


@router.delete("/batches/{batch_id}")
def delete_batch(batch_id: int, db: Session = Depends(get_db)):
    batch = db.query(models.Batches).filter(
        models.Batches.id == batch_id).first()
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    db.delete(batch)
    db.commit()
    return batch
