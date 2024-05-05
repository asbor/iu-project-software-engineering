from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from setup import SessionLocal
import database.models as models
import database.schemas as schemas

router = APIRouter()

db = SessionLocal()


@router.post("/hop", response_model=schemas.Hop)
def create_hop(hop: schemas.Hop):
    """
    Create a new hop entry in the database.

    Args:
        hop (Hop): The hop data to be added to the database.

    Returns:
        Hop: The hop data that was added to the database.

    Raises:
        HTTPException: If an error occurs while trying to add the hop data to the database.
    """
    new_hop = models.Hop(**hop.dict())
    db.add(new_hop)
    db.commit()
    db.refresh(new_hop)
    return new_hop


@router.get("/hop/{hop_id}", response_model=schemas.Hop)
def read_hop(hop_id: UUID):
    """
    Retrieve a hop entry from the database.

    Args:
        hop_id (UUID): The unique identifier for the hop.

    Returns:
        Hop: The hop data retrieved from the database.

    Raises:
        HTTPException: If the hop data with the specified ID does not exist in the database.
    """
    hop = db.query(models.Hop).filter(models.Hop.id == hop_id).first()
    if hop is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hop not found")
    return hop


@router.put("/hop/{hop_id}", response_model=schemas.Hop)
def update_hop(hop_id: UUID, hop: schemas.Hop):
    """
    Update a hop entry in the database.

    Args:
        hop_id (UUID): The unique identifier for the hop.
        hop (Hop): The hop data to be added to the database.

    Returns:
        Hop: The updated hop data.

    Raises:
        HTTPException: If the hop data with the specified ID does not exist in the database.
    """
    hop_data = db.query(models.Hop).filter(models.Hop.id == hop_id).first()
    if hop_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hop not found")
    for key, value in hop.dict().items():
        setattr(hop_data, key, value)
    db.commit()
    db.refresh(hop_data)
    return hop_data


@router.delete("/hop/{hop_id}")
def delete_hop(hop_id: UUID):
    """
    Delete a hop entry from the database.

    Args:
        hop_id (UUID): The unique identifier for the hop.

    Returns:
        None

    Raises:
        HTTPException: If the hop data with the specified ID does not exist in the database.
    """
    hop = db.query(models.Hop).filter(models.Hop.id == hop_id).first()
    if hop is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hop not found")
    db.delete(hop)
    db.commit()
    return None
