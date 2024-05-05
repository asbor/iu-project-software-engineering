from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from setup import SessionLocal
import database.models as models
import database.schemas as schemas

router = APIRouter()
db = SessionLocal()


@router.post("/misc", response_model=schemas.Misc)
def create_misc(misc: schemas.Misc):
    """
    Create a new misc entry in the database.

    Args:
        misc (Misc): The misc data to be added to the database.

    Returns:
        Misc: The misc data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the misc data to the database.
    """
    new_misc = models.Misc(**misc.dict())
    db.add(new_misc)
    db.commit()
    db.refresh(new_misc)
    return new_misc


@router.get("/misc/{misc_id}", response_model=schemas.Misc)
def read_misc(misc_id: UUID):
    """
    Retrieve a misc entry from the database.

    Args:
        misc_id (UUID): The unique identifier for the misc.

    Returns:
        Misc: The misc data retrieved from the database.

    Raises:
        HTTPException: If the misc data with the specified ID does not exist in the database.
    """
    misc = db.query(models.Misc).filter(models.Misc.id == misc_id).first()
    if misc is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Misc not found")
    return misc


@router.put("/misc/{misc_id}", response_model=schemas.Misc)
def update_misc(misc_id: UUID, misc: schemas.Misc):
    """
    Update a misc entry in the database.

    Args:
        misc_id (UUID): The unique identifier for the misc.
        misc (Misc): The misc data to be added to the database.

    Returns:
        Misc: The updated misc data.

    Raises:
        HTTPException: If the misc data with the specified ID does not exist in the database.
    """
    misc_data = db.query(models.Misc).filter(models.Misc.id == misc_id).first()
    if misc_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Misc not found")
    for key, value in misc.dict().items():
        setattr(misc_data, key, value)
    db.commit()
    db.refresh(misc_data)
    return misc_data


@router.delete("/misc/{misc_id}")
def delete_misc(misc_id: UUID):
    """
    Delete a misc entry from the database.

    Args:
        misc_id (UUID): The unique identifier for the misc.

    Returns:
        None

    Raises:
        HTTPException: If the misc data with the specified ID does not exist in the database.
    """
    misc = db.query(models.Misc).filter(models.Misc.id == misc_id).first()
    if misc is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Misc not found")
    db.delete(misc)
    db.commit()
    return None
