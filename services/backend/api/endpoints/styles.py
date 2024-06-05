from fastapi import APIRouter

from database import SessionLocal

from typing import Annotated

from fastapi import Depends

from database import get_db

import Database.Models as models


db_dependency = Annotated[SessionLocal, Depends(get_db)]


router = APIRouter()

db = SessionLocal()


@router.get("/styles")
async def get_all_styles(db: db_dependency):

    styles = db.query(models.Styles).all()

    return styles
