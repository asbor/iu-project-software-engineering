from fastapi import APIRouter, HTTPException, status
from setup import SessionLocal
import database.models as models
import database.schemas as schemas
from typing import List

router = APIRouter()
db = SessionLocal()


@router.post("/style", response_model=schemas.Style)
def create_style(style: schemas.Style):
    """
    Create a new style entry in the database.

    Args:
        style (Style): The style data to be added to the database.

    Returns:
        Style: The style data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the style data to the database.
    """
    new_style = models.Style(**style.dict())
    db.add(new_style)
    db.commit()
    db.refresh(new_style)
    return new_style


@router.get("/style", response_model=List[schemas.Style])
def get_all_style():
    """
    Retrieve all style entries from the database.

    Returns:
        List[style]: The list of all style entries retrieved from the database.

    Raises:
        HTTPException: If an error occurs while trying to retrieve style data from the database.
    """
    style = db.query(models.Style).all()
    return style


@router.get("/style/{style_id}", response_model=schemas.Style)
def read_style(style_id: int):
    """
    Retrieve a style entry from the database.

    Args:
        style_id (int): The unique identifier for the style.

    Returns:
        Style: The style data retrieved from the database.

    Raises:
        HTTPException: If the style data with the specified ID does not exist in the database.
    """
    style = db.query(models.Style).filter(models.Style.id == style_id).first()
    if style is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Style not found")
    return style


@router.put("/style/{style_id}", response_model=schemas.Style)
def update_style(style_id: int, style: schemas.Style):
    """
    Update a style entry in the database.

    Args:
        style_id (int): The unique identifier for the style.
        style (Style): The style data to be added to the database.

    Returns:
        Style: The updated style data.

    Raises:
        HTTPException: If the style data with the specified ID does not exist in the database.
    """
    style_data = db.query(models.Style).filter(
        models.Style.id == style_id).first()
    if style_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Style not found")
    for key, value in style.dict().items():
        setattr(style_data, key, value)
    db.commit()
    db.refresh(style_data)
    return style_data


@router.delete("/style/{style_id}")
def delete_style(style_id: int):
    """
    Delete a style entry from the database.

    Args:
        style_id (int): The unique identifier for the style.

    Returns:
        None

    Raises:
        HTTPException: If the style data with the specified ID does not exist in the database.
    """
    style = db.query(models.Style).filter(models.Style.id == style_id).first()
    if style is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Style not found")
    db.delete(style)
    db.commit()
    return None
