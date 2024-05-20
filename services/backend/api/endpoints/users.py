from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

from Database.Schemas.recipes import RecipeBase

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()
