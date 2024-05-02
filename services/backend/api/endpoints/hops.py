from fastapi import APIRouter, HTTPException, status
import uuid
from setup import SessionLocal
import database.models as models
import database.schemas.schemas as schemas

router = APIRouter()

db = SessionLocal()


@router.post("/hops", response_model=schemas.hops)
def create_hops(hops: schemas.HopsCreate):
    """
    Create a new hops entry in the database.

    Args:
        hops (HopsCreate): The hops data to be added to the database.

    Returns:
        Hops: The hops data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the hops data to the database.
    """
    new_hops = models.Hops(**hops.dict())
    db.add(new_hops)
    db.commit()
    db.refresh(new_hops)
    return new_hops


@router.get("/hops/{hops_id}", response_model=schemas.Hops)
def read_hops(hops_id: uuid.UUID):
    """
    Retrieve a hops entry from the database.

    Args:
        hops_id (UUID): The unique identifier for the hops.

    Returns:
        Hops: The hops data retrieved from the database.

    Raises:
        HTTPException: If the hops data with the specified ID does not exist in the database.
    """
    hops = db.query(models.Hops).filter(models.Hops.id == hops_id).first()
    if hops is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hops not found")
    return hops


@router.put("/hops/{hops_id}", response_model=schemas.Hops)
def update_hops(hops_id: uuid.UUID, hops: schemas.HopsCreate):
    """
    Update a hops entry in the database.

    Args:
        hops_id (UUID): The unique identifier for the hops.
        hops (HopsCreate): The updated hops data.

    Returns:
        Hops: The updated hops data.

    Raises:
        HTTPException: If the hops data with the specified ID does not exist in the database.
    """
    hops_data = db.query(models.Hops).filter(models.Hops.id == hops_id).first()
    if hops_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hops not found")
    for key, value in hops.dict().items():
        setattr(hops_data, key, value)
    db.commit()
    db.refresh(hops_data)
    return hops_data


@router.delete("/hops/{hops_id}")
def delete_hops(hops_id: uuid.UUID):
    """
    Delete a hops entry from the database.

    Args:
        hops_id (UUID): The unique identifier for the hops.

    Returns:
        None

    Raises:
        HTTPException: If the hops data with the specified ID does not exist in the database.
    """
    hops = db.query(models.Hops).filter(models.Hops.id == hops_id).first()
    if hops is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hops not found")
    db.delete(hops)
    db.commit()
    return None
