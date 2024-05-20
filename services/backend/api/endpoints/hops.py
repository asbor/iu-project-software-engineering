from fastapi import APIRouter, HTTPException, status
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()


@router.get("/hops")
async def get_all_hops(db: db_dependency):
    hops = db.query(models.Hops).all()
    return hops
