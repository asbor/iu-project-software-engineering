from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from setup import SessionLocal
import database.models as models
import database.schemas as schemas

router = APIRouter()
db = SessionLocal()


@router.post("/mash", response_model=schemas.Mash)
def create_mash(mash: schemas.Mash):
    """
    Create a new mash entry in the database.

    Args:
        mash (Mash): The mash data to be added to the database.

    Returns:
        Mash: The mash data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the mash data to the database.
    """
    new_mash = models.Mash(**mash.dict())
    db.add(new_mash)
    db.commit()
    db.refresh(new_mash)
    return new_mash


@router.get("/mash/{mash_id}", response_model=schemas.Mash)
def read_mash(mash_id: UUID):
    """
    Retrieve a mash entry from the database.

    Args:
        mash_id (UUID): The unique identifier for the mash.

    Returns:
        Mash: The mash data retrieved from the database.

    Raises:
        HTTPException: If the mash data with the specified ID does not exist in the database.
    """
    mash = db.query(models.Mash).filter(models.Mash.id == mash_id).first()
    if mash is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Mash not found")
    return mash


@router.put("/mash/{mash_id}", response_model=schemas.Mash)
def update_mash(mash_id: UUID, mash: schemas.Mash):
    """
    Update a mash entry in the database.

    Args:
        mash_id (UUID): The unique identifier for the mash.
        mash (Mash): The mash data to be added to the database.

    Returns:
        Mash: The updated mash data.

    Raises:
        HTTPException: If the mash data with the specified ID does not exist in the database.
    """
    mash_data = db.query(models.Mash).filter(models.Mash.id == mash_id).first()
    if mash_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Mash not found")
    for key, value in mash.dict().items():
        setattr(mash_data, key, value)
    db.commit()
    db.refresh(mash_data)
    return mash_data


@router.delete("/mash/{mash_id}")
def delete_mash(mash_id: UUID):
    """
    Delete a mash entry from the database.

    Args:
        mash_id (UUID): The unique identifier for the mash.

    Returns:
        None

    Raises:
        HTTPException: If the mash data with the specified ID does not exist in the database.
    """
    mash = db.query(models.Mash).filter(models.Mash.id == mash_id).first()
    if mash is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Mash not found")
    db.delete(mash)
    db.commit()
    return None
