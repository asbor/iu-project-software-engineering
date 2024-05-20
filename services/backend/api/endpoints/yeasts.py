from fastapi import APIRouter, HTTPException, status
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()


@router.get("/yeasts")
async def get_all_yeasts(db: db_dependency):
    yeasts = db.query(models.Yeasts).all()
    return yeasts
