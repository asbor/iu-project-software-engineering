from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from database import SessionLocal
import Database.Models as models
import Database.Schemas as schemas

router = APIRouter()
db = SessionLocal()


@router.post("/water", response_model=schemas.Water)
def create_water(water: schemas.Water):
    """
    Create a new water entry in the database.

    Args:
        water (Water): The water data to be added to the database.

    Returns:
        Water: The water data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the water data to the database.
    """
    new_water = models.Water(**water.dict())
    db.add(new_water)
    db.commit()
    db.refresh(new_water)
    return new_water


@router.get("/water/{water_id}", response_model=schemas.Water)
def read_water(water_id: UUID):
    """
    Retrieve a water entry from the database.

    Args:
        water_id (UUID): The unique identifier for the water.

    Returns:
        Water: The water data retrieved from the database.

    Raises:
        HTTPException: If the water data with the specified ID does not exist in the database.
    """
    water = db.query(models.Water).filter(models.Water.id == water_id).first()
    if water is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Water not found")
    return water


@router.put("/water/{water_id}", response_model=schemas.Water)
def update_water(water_id: UUID, water: schemas.Water):
    """
    Update a water entry in the database.

    Args:
        water_id (UUID): The unique identifier for the water.
        water (Water): The water data to be added to the database.

    Returns:
        Water: The updated water data.

    Raises:
        HTTPException: If the water data with the specified ID does not exist in the database.
    """
    water_data = db.query(models.Water).filter(
        models.Water.id == water_id).first()
    if water_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Water not found")
    for key, value in water.dict().items():
        setattr(water_data, key, value)
    db.commit()
    db.refresh(water_data)
    return water_data


@router.delete("/water/{water_id}")
def delete_water(water_id: UUID):
    """
    Delete a water entry from the database.

    Args:
        water_id (UUID): The unique identifier for the water.

    Returns:
        None

    Raises:
        HTTPException: If the water data with the specified ID does not exist in the database.
    """
    water = db.query(models.Water).filter(models.Water.id == water_id).first()
    if water is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Water not found")
    db.delete(water)
    db.commit()
    return None
