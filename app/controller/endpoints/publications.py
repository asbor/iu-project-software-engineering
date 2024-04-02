from datetime import datetime
from fastapi import APIRouter, HTTPException, status
import uuid
from model.database import SessionLocal
import model.db_models as models
import data.schemas as schemas

router = APIRouter()

db = SessionLocal()


# create a publication
"""
{
  "id": "{{$guid}}",
  "title": "The sound of music",
  "authors": [
    {
      "name": "Asbjorn",
      "surname": "Bordoy",
      "created_at": "{{$timestamp}}",
      "updated_at": "{{$timestamp}}"
    }
  ],
  "categories": [
    {
        "name": "Romance",
        "created_at": "{{$timestamp}}",
        "updated_at": "{{$timestamp}}"
    }
  ],
  "created_at": "{{$timestamp}}",
  "updated_at": "{{$timestamp}}"
}
"""


@router.post("/publications", response_model=schemas.Publication, status_code=status.HTTP_201_CREATED)
def create_publication(publication: schemas.Publication):
    # check if publication exists
    if db.query(models.Publication).filter(models.Publication.id == publication.id).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Publication already exists")

    # create or get authors
    authors = []
    for author in publication.authors:
        author_obj = get_or_create_author(author)
        authors.append(author_obj)

    # create or get categories
    categories = []
    for category in publication.categories:
        category_obj = get_or_create_category(category)
        categories.append(category_obj)

    # create publication
    new_publication = models.Publication(
        id=publication.id,
        title=publication.title,
        authors=authors,
        categories=categories
    )
    db.add(new_publication)
    db.commit()
    db.refresh(new_publication)
    return new_publication


def get_or_create_author(author: schemas.Author) -> models.Author:
    # check if author exists
    author_obj = db.query(models.Author).filter(
        models.Author.name == author.name, models.Author.surname == author.surname).first()
    if author_obj is None:
        # create new author
        author_obj = models.Author(
            id=uuid.uuid4(),
            name=author.name,
            surname=author.surname,
            created_at=author.created_at,
            updated_at=author.updated_at
        )
        db.add(author_obj)
        db.commit()
        db.refresh(author_obj)
    else:
        # merge existing author into session
        author_obj = db.merge(author_obj)
    return author_obj


def get_or_create_category(category: schemas.Category) -> models.Category:
    # check if category exists
    category_obj = db.query(models.Category).filter(
        models.Category.name == category.name).first()
    if category_obj is None:
        # create new category
        category_obj = models.Category(
            id=uuid.uuid4(),
            name=category.name,
            created_at=category.created_at,
            updated_at=category.updated_at
        )
        db.add(category_obj)
        db.commit()
        db.refresh(category_obj)
    return category_obj

# get all publications


@router.get("/publications", status_code=status.HTTP_200_OK)
async def get_all_publications():
    publications = db.query(models.Publication).all()
    return publications

# get a publication by id


@router.get("/publications/{id}", status_code=status.HTTP_200_OK)
async def get_publication_by_id(id: str):
    publication = db.query(models.Publication).filter(
        models.Publication.id == id).first()
    if publication is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")
    return publication

# update a publication by id


@router.put("/publications/{id}", status_code=status.HTTP_200_OK)
async def update_publication_by_id(id: str, publication: schemas.Publication):
    publication_exists = db.query(models.Publication).filter(
        models.Publication.id == id).first()
    if publication_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")

    # check if author exists in Author table, by comparing name and surname, if not then create it, else add it to the publication
    for author in publication.authors:
        author_exists = db.query(models.Author).filter(
            models.Author.name == author.name, models.Author.surname == author.surname).first()
        if author_exists is None:
            new_author = models.Author(
                # create a new id for the author
                id=uuid.uuid4(),
                name=author.name,
                surname=author.surname,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.add(new_author)
            db.commit()
            db.refresh(new_author)
        else:
            author = author_exists

    # check if category exists in Category table by comparing name, if not then create it, else add it to the publication
    for category in publication.categories:
        category_exists = db.query(models.Category).filter(
            models.Category.name == category.name).first()
        if category_exists is None:
            new_category = models.Category(
                # create a new id for the category
                id=uuid.uuid4(),
                name=category.name,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.add(new_category)
            db.commit()
            db.refresh(new_category)
        else:
            category = category_exists

    publication_exists.title = publication.title
    publication_exists.authors = publication.authors
    publication_exists.categories = publication.categories
    publication_exists.updated_at = datetime.now()
    db.commit()
    db.refresh(publication_exists)
    return publication_exists

# delete a publication by id


@router.delete("/publications/{id}", status_code=status.HTTP_200_OK)
async def delete_publication_by_id(id: str):
    publication = db.query(models.Publication).filter(
        models.Publication.id == id).first()
    if publication is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")
    db.delete(publication)
    db.commit()
    return {"message": "Publication deleted successfully"}
