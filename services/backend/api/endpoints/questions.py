from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import Database.Models.questions as question_models
import Database.Models.choices as choice_models
import Database.Schemas.questions as question_schemas
from typing import List

router = APIRouter()


@router.post("/questions", response_model=question_schemas.QuestionWithID)
async def create_questions(
    question: question_schemas.QuestionBase, db: Session = Depends(get_db)
):
    try:
        # Create the main question entry
        db_question = question_models.Questions(
            question_text=question.question_text
        )
        db.add(db_question)
        db.commit()
        db.refresh(db_question)

        # Create associated choices
        for choice in question.choices:
            db_choice = choice_models.Choices(
                choice_text=choice.choice_text,
                is_correct=choice.is_correct,
                question_id=db_question.id,
            )
            db.add(db_choice)
            db.commit()
            db.refresh(db_choice)

        db_question.choices = (
            db.query(choice_models.Choices)
            .filter(choice_models.Choices.question_id == db_question.id)
            .all()
        )

        return db_question
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/questions", response_model=List[question_schemas.QuestionWithID])
async def get_all_questions(db: Session = Depends(get_db)):
    questions = db.query(question_models.Questions).all()
    for question in questions:
        question.choices = (
            db.query(choice_models.Choices)
            .filter(choice_models.Choices.question_id == question.id)
            .all()
        )
    return questions


@router.delete(
    "/questions/{question_id}", response_model=question_schemas.QuestionWithID
)
async def delete_question(question_id: int, db: Session = Depends(get_db)):
    question = (
        db.query(question_models.Questions)
        .filter(question_models.Questions.id == question_id)
        .first()
    )
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(question)
    db.commit()
    return question
