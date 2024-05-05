from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from setup import SessionLocal
import database.models as models
import database.schemas as schemas

router = APIRouter()
db = SessionLocal()


@router.post("/yeast", response_model=schemas.Yeast)
def create_yeast(yeast: schemas.Yeast):
    """
    Create a new yeast entry in the database.

    Args:
        yeast (Yeast): The yeast data to be added to the database.

    Returns:
        Yeast: The yeast data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the yeast data to the database.
    """
    new_yeast = models.Yeast(**yeast.dict())
    db.add(new_yeast)
    db.commit()
    db.refresh(new_yeast)
    return new_yeast


@router.get("/yeast/{yeast_id}", response_model=schemas.Yeast)
def read_yeast(yeast_id: UUID):
    """
    Retrieve a yeast entry from the database.

    Args:
        yeast_id (UUID): The unique identifier for the yeast.

    Returns:
        Yeast: The yeast data retrieved from the database.

    Raises:
        HTTPException: If the yeast data with the specified ID does not exist in the database.
    """
    yeast = db.query(models.Yeast).filter(models.Yeast.id == yeast_id).first()
    if yeast is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Yeast not found")
    return yeast


@router.put("/yeast/{yeast_id}", response_model=schemas.Yeast)
def update_yeast(yeast_id: UUID, yeast: schemas.Yeast):
    """
    Update a yeast entry in the database.

    Args:
        yeast_id (UUID): The unique identifier for the yeast.
        yeast (Yeast): The yeast data to be added to the database.

    Returns:
        Yeast: The updated yeast data.

    Raises:
        HTTPException: If the yeast data with the specified ID does not exist in the database.
    """
    yeast_data = db.query(models.Yeast).filter(
        models.Yeast.id == yeast_id).first()
    if yeast_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Yeast not found")
    for key, value in yeast.dict().items():
        setattr(yeast_data, key, value)
    db.commit()
    db.refresh(yeast_data)
    return yeast_data


@router.delete("/yeast/{yeast_id}")
def delete_yeast(yeast_id: UUID):
    """
    Delete a yeast entry from the database.

    Args:
        yeast_id (UUID): The unique identifier for the yeast.

    Returns:
        None

    Raises:
        HTTPException: If the yeast data with the specified ID does not exist in the database.
    """
    yeast = db.query(models.Yeast).filter(models.Yeast.id == yeast_id).first()
    if yeast is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Yeast not found")
    db.delete(yeast)
    db.commit()
    return None
