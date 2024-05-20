from fastapi import APIRouter, HTTPException, status
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

from Database.Schemas.recipes import RecipeBase

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()


@router.get("/style_guidelines")
async def get_all_style_guidelines(db: db_dependency):
    style_guidelines = db.query(models.StyleGuidelines).all()
    return style_guidelines
