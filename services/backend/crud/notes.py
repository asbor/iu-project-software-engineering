from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import Note
from schemas.notes import NoteOutSchema
from schemas.token import Status


async def get_notes(db: Session) -> list[NoteOutSchema]:
    return await db.query(NoteOutSchema).all()


async def get_note(db: Session, note_id: int) -> NoteOutSchema:
    note = db.query(NoteOutSchema).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Note {note_id} not found"
        )
    return note


async def create_note(db: Session, note, current_user) -> NoteOutSchema:
    new_note = Note(author_id=current_user.id, **note.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


async def update_note(db: Session, note_id: int, note, current_user) -> NoteOutSchema:
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if not db_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Note {note_id} not found"
        )
    if db_note.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this note"
        )
    for key, value in note.dict(exclude_unset=True).items():
        setattr(db_note, key, value)
    db.commit()
    db.refresh(db_note)
    return db_note


async def delete_note(db: Session, note_id: int, current_user) -> Status:
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if not db_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Note {note_id} not found"
        )
    if db_note.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this note"
        )
    db.delete(db_note)
    db.commit()
    return Status(message=f"Deleted note {note_id}")
