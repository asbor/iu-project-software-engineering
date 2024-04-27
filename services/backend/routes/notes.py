from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from auth.jwthandler import get_current_user
from crud.sqlalchemy_notes import (
    get_notes,
    get_note,
    create_note,
    update_note,
    delete_note,
)
from schemas.notes import NoteOutSchema, NoteInSchema, UpdateNote
from schemas.token import Status
from schemas.users import UserOutSchema
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/notes", response_model=List[NoteOutSchema])
async def read_notes(db: Session = Depends(get_db), current_user: UserOutSchema = Depends(get_current_user)):
    return get_notes(db)


@router.get("/note/{note_id}", response_model=NoteOutSchema)
async def read_note(note_id: int, db: Session = Depends(get_db), current_user: UserOutSchema = Depends(get_current_user)):
    note = get_note(db, note_id)
    if note is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Note not found")
    return note


@router.post("/notes", response_model=NoteOutSchema)
async def create_note(note: NoteInSchema, db: Session = Depends(get_db), current_user: UserOutSchema = Depends(get_current_user)):
    return create_note(db, note, current_user)


@router.put("/note/{note_id}", response_model=NoteOutSchema)
async def update_note(note_id: int, note: UpdateNote, db: Session = Depends(get_db), current_user: UserOutSchema = Depends(get_current_user)):
    return update_note(db, note_id, note, current_user)


@router.delete("/note/{note_id}", response_model=Status)
async def delete_note(note_id: int, db: Session = Depends(get_db), current_user: UserOutSchema = Depends(get_current_user)):
    return delete_note(db, note_id, current_user)
