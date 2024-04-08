from fastapi import APIRouter, HTTPException, status
import uuid
from src.model.database import SessionLocal
import src.model.db_models as models
import src.data.schemas as schemas

router = APIRouter()

db = SessionLocal()

# create a new author


@router.post("/authors", response_model=schemas.Author)
def create_author(author: schemas.Author):
    # The author id must not exist in the database
    if db.query(models.Author).filter(models.Author.id == author.id).first() is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Author id already exists")

    # Length of the author name must be between 1 and 20 characters
    if len(author.name) < 1 or len(author.name) > 20:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Author name must be between 1 and 20 characters")

    # Length of the author surname must be between 1 and 20 characters
    if len(author.surname) < 1 or len(author.surname) > 20:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Author surname must be between 1 and 20 characters")

    # The auther name + surname must be unique
    if db.query(models.Author).filter(models.Author.name == author.name).filter(models.Author.surname == author.surname).first() is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Author name + surname already exists")

    new_author = models.Author(
        id=author.id,
        name=author.name,
        surname=author.surname,
        created_at=author.created_at,
        updated_at=author.updated_at
    )

    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


# get all authors
@router.get("/authors", response_model=list[schemas.Author])
def get_all_authors():
    authors = db.query(models.Author).all()
    return authors

# get an author by id


@router.get("/authors/{authorId}", response_model=schemas.Author)
def get_author(authorId: uuid.UUID):
    author = db.query(models.Author).filter(
        models.Author.id == authorId).first()
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author


# Update an author
@router.patch("/authors/{authorId}", status_code=status.HTTP_200_OK)
async def patch_author(authorId: uuid.UUID, author: schemas.Author):
    db_author = db.query(models.Author).filter(
        models.Author.id == authorId).first()

    # The author id must exist in the database
    if db_author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")

    # The author id cannot be changed
    if author.id is not None:
        if db_author.id != author.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Author id cannot be changed")

    # The author created_at cannot be changed
    if author.created_at is not None:
        if db_author.created_at != author.created_at:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Author created_at cannot be changed")

    # updating the updated_at field
    db_author.updated_at = author.name          # type: ignore
    db_author.name = author.name                # type: ignore
    db_author.surname = author.surname          # type: ignore

    db.commit()
    db.refresh(db_author)
    return db_author


# Delete an author
@router.delete("/authors/{authorId}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(authorId: uuid.UUID):
    db_author = db.query(models.Author).filter(
        models.Author.id == authorId).first()
    if db_author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")

    db.delete(db_author)
    db.commit()

    return "Author deleted"
