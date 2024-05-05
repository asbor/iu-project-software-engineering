from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from setup import SessionLocal
import database.models as models
import database.schemas as schemas

router = APIRouter()

db = SessionLocal()


@router.post("/fermentable", response_model=schemas.Fermentable)
def create_fermentable(fermentable: schemas.Fermentable):
    """
    Create a new fermentable entry in the database.

    Args:
        fermentable (Fermentable): The fermentable data to be added to the database.

    Returns:
        Fermentable: The fermentable data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the fermentable data to the database.
    """
    new_fermentable = models.Fermentable(**fermentable.dict())
    db.add(new_fermentable)
    db.commit()
    db.refresh(new_fermentable)
    return new_fermentable


@router.get("/fermentable/{fermentable_id}", response_model=schemas.Fermentable)
def read_fermentable(fermentable_id: UUID):
    """
    Retrieve a fermentable entry from the database.

    Args:
        fermentable_id (UUID): The unique identifier for the fermentable.

    Returns:
        Fermentable: The fermentable data retrieved from the database.

    Raises:
        HTTPException: If the fermentable data with the specified ID does not exist in the database.
    """
    fermentable = db.query(models.Fermentable).filter(
        models.Fermentable.id == fermentable_id).first()
    if fermentable is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Fermentable not found")
    return fermentable


@router.put("/fermentable/{fermentable_id}", response_model=schemas.Fermentable)
def update_fermentable(fermentable_id: UUID, fermentable: schemas.Fermentable):
    """
    Update a fermentable entry in the database.

    Args:
        fermentable_id (UUID): The unique identifier for the fermentable.
        fermentable (Fermentable): The fermentable data to be added to the database.

    Returns:
        Fermentable: The updated fermentable data.

    Raises:
        HTTPException: If the fermentable data with the specified ID does not exist in the database.
    """
    fermentable_data = db.query(models.Fermentable).filter(
        models.Fermentable.id == fermentable_id).first()
    if fermentable_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Fermentable not found")
    for key, value in fermentable.dict().items():
        setattr(fermentable_data, key, value)
    db.commit()
    db.refresh(fermentable_data)
    return fermentable_data


@router.delete("/fermentable/{fermentable_id}")
def delete_fermentable(fermentable_id: UUID):
    """
    Delete a fermentable entry from the database.

    Args:
        fermentable_id (UUID): The unique identifier for the fermentable.

    Returns:
        None

    Raises:
        HTTPException: If the fermentable data with the specified ID does not exist in the database.
    """
    fermentable = db.query(models.Fermentable).filter(
        models.Fermentable.id == fermentable_id).first()
    if fermentable is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Fermentable not found")
    db.delete(fermentable)
    db.commit()
    return None
