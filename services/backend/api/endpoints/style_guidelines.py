# api/endpoints/style_guidelines.py


from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import Database.Models as models
import Database.Schemas as schemas
from typing import List

router = APIRouter()

# Style Guidelines Endpoints



@router.get(
    "/style_guidelines", response_model=List[schemas.StyleGuidelineBase]
)
async def get_all_style_guidelines(db: Session = Depends(get_db)):
    style_guidelines = db.query(models.StyleGuidelines).all()
    return style_guidelines


@router.get(
    "/style_guidelines/{guideline_id}",
    response_model=schemas.StyleGuidelineBase,
)
async def get_style_guideline(
    guideline_id: int, db: Session = Depends(get_db)
):
    guideline = (
        db.query(models.StyleGuidelines)
        .filter(models.StyleGuidelines.id == guideline_id)
        .first()
    )
    if not guideline:
        raise HTTPException(
            status_code=404, detail="Style Guideline not found"
        )
    return guideline


@router.post("/style_guidelines", response_model=schemas.StyleGuidelineBase)
async def create_style_guideline(
    guideline: schemas.StyleGuidelineBaseCreate, db: Session = Depends(get_db)
):
    try:
        db_guideline = models.StyleGuidelines(**guideline.dict())
        db.add(db_guideline)
        db.commit()
        db.refresh(db_guideline)
        return db_guideline
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(
    "/style_guidelines/{id}", response_model=schemas.StyleGuidelineBase
)
async def delete_style_guideline(id: int, db: Session = Depends(get_db)):
    guideline = (
        db.query(models.StyleGuidelines)
        .filter(models.StyleGuidelines.id == id)
        .first()
    )
    if not guideline:
        raise HTTPException(
            status_code=404, detail="Style Guideline not found"
        )
    db.delete(guideline)
    db.commit()
    return guideline


@router.put(
    "/style_guidelines/{id}", response_model=schemas.StyleGuidelineBase
)
async def update_style_guideline(
    id: int,
    guideline: schemas.StyleGuidelineBaseCreate,
    db: Session = Depends(get_db),
):
    db_guideline = (
        db.query(models.StyleGuidelines)
        .filter(models.StyleGuidelines.id == id)
        .first()
    )
    if not db_guideline:
        raise HTTPException(
            status_code=404, detail="Style Guideline not found"
        )
    for key, value in guideline.dict().items():
        setattr(db_guideline, key, value)
    db.commit()
    db.refresh(db_guideline)
    return db_guideline
