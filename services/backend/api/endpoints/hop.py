from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from database import SessionLocal
from typing import Annotated
from fastapi import Depends
from database import get_db
import Database.Models as models

from Database.Schemas.hops import HopBase

db_dependency = Annotated[SessionLocal, Depends(get_db)]

router = APIRouter()
db = SessionLocal()


@router.post("/hops")
async def create_hops(question: HopBase, db: db_dependency):
    db_question = models.hops(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = models.Choices(
            choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choice)
        db.commit()
        db.refresh(db_choice)
