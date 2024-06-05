from fastapi import APIRouter
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db

db_dependency = Annotated[SessionLocal, Depends(get_db)]
router = APIRouter()
db = SessionLocal()
