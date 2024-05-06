from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from setup import SessionLocal
import database.models as models
import database.schemas as schemas
from api.validation.fermentable_validation import FermentableCreate

from typing import List
from uuid import uuid4
from datetime import datetime, timezone

router = APIRouter()
db = SessionLocal()

"""
Fermentable creation schema

Attributes:
    id (UUID): The unique identifier for the fermentable.
    created_at (datetime): The date and time the fermentable was created.
    updated_at (datetime): The date and time the fermentable was last updated.
    name (str): The name of the fermentable.
    amount (int): The amount of the fermentable in kilograms.
    cost_per_unit (float): The cost per unit in Euros.
    supplier (str): The supplier of the fermentable.
    origin (str): The origin of the fermentable.
    type (str): The type of the fermentable.
    color (int): The color of the fermentable in EBC.
    potential (int): The potential of the fermentable in PPG (Points Per Gallon).
    yield_ (float): The yield of the fermentable as a percentage.
    manufacturing_date (str): The manufacturing date of the fermentable.
    expiry_date (str): The expiry date of the fermentable.
    lot_number (str): The lot number of the fermentable.
    exclude_from_total (bool): Indicates whether to exclude the fermentable from the total.
    not_fermentable (bool): Indicates whether the fermentable is not fermentable.
    notes (str): Additional notes about the fermentable.
    description (str): Description of the fermentable.
    substitutes (str): Substitutes for the fermentable.
    used_in (str): Where the fermentable is used.
"""


@router.post("/fermentable", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_fermentable(fermentable: FermentableCreate):
    """
    Create a new fermentable entry in the database.

    Args:
        fermentable (FermentableCreate): The fermentable data to be created.

    Returns:
        dict: A message indicating the fermentable was created successfully and the unique identifier for the fermentable.

    Raises:
        HTTPException: If the fermentable name already exists in the database.
    """
    # Check if fermentable name already exists
    existing_fermentable = db.query(models.Fermentable).filter(
        models.Fermentable.name == fermentable.name).first()
    if existing_fermentable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Fermentable name already exists")

    # Generate unique ID
    fermentable_id = str(uuid4())

    # Create new fermentable profile
    new_fermentable = models.Fermentable(
        id=fermentable_id,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        name=fermentable.name,
        amount=fermentable.amount,
        cost_per_unit=fermentable.cost_per_unit,
        supplier=fermentable.supplier,
        origin=fermentable.origin,
        type=fermentable.type,
        color=fermentable.color,
        potential=fermentable.potential,
        yield_=fermentable.yield_,
        manufacturing_date=fermentable.manufacturing_date,
        expiry_date=fermentable.expiry_date,
        lot_number=fermentable.lot_number,
        exclude_from_total=fermentable.exclude_from_total,
        not_fermentable=fermentable.not_fermentable,
        notes=fermentable.notes if fermentable.notes else "",
        description=fermentable.description,
        substitutes=fermentable.substitutes,
        used_in=fermentable.used_in
    )

    # Add fermentable profile to the database
    db.add(new_fermentable)
    db.commit()
    db.refresh(new_fermentable)

    return {"message": "Fermentable profile created successfully", "fermentable_id": fermentable_id}


@router.get("/fermentable", response_model=List[schemas.Fermentable])
def get_all_fermentable():
    """
    Retrieve all fermentable entries from the database.

    Returns:
        List[fermentable]: The list of all fermentable entries retrieved from the database.

    Raises:
        HTTPException: If an error occurs while trying to retrieve fermentable data from the database.
    """
    fermentable = db.query(models.Fermentable).all()
    return fermentable


@router.get("/fermentable/{fermentable_id}", response_model=schemas.Fermentable)
def read_fermentable(fermentable_id: UUID):
    """
    Retrieve a fermentable entry from the database.

    Args:
        fermentable_id (UUID): The unique identifier for the fermentable.

    Returns:
        fermentable: The fermentable data retrieved from the database.

    Raises:
        HTTPException: If the fermentable data with the specified ID does not exist in the database.
    """
    fermentable = db.query(models.Fermentable).filter(
        models.Fermentable.id == fermentable_id).first()
    if fermentable is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="fermentable not found")
    return fermentable


@router.put("/fermentable/{fermentable_id}", response_model=dict)
async def update_fermentable(fermentable_id: UUID, fermentable: FermentableCreate):
    # Check if fermentable exists
    existing_fermentable = db.query(models.Fermentable).filter(
        models.Fermentable.id == fermentable_id).first()
    if not existing_fermentable:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="fermentable not found")

    # Update fermentable profile
    existing_fermentable.id = fermentable_id
    existing_fermentable.updated_at = datetime.now(timezone.utc)
    existing_fermentable.name = fermentable.name
    existing_fermentable.amount = fermentable.amount
    existing_fermentable.cost_per_unit = fermentable.cost_per_unit
    existing_fermentable.supplier = fermentable.supplier
    existing_fermentable.origin = fermentable.origin
    existing_fermentable.type = fermentable.type
    existing_fermentable.color = fermentable.color
    existing_fermentable.potential = fermentable.potential
    existing_fermentable.yield_ = fermentable.yield_
    existing_fermentable.manufacturing_date = fermentable.manufacturing_date
    existing_fermentable.expiry_date = fermentable.expiry_date
    existing_fermentable.lot_number = fermentable.lot_number
    existing_fermentable.exclude_from_total = fermentable.exclude_from_total
    existing_fermentable.not_fermentable = fermentable.not_fermentable
    existing_fermentable.notes = fermentable.notes
    existing_fermentable.description = fermentable.description
    existing_fermentable.substitutes = fermentable.substitutes
    existing_fermentable.used_in = fermentable.used_in

    db.commit()

    return {"message": "fermentable profile updated successfully", "fermentable_id": fermentable_id}


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
            status_code=status.HTTP_404_NOT_FOUND, detail="fermentable not found")
    db.delete(fermentable)
    db.commit()
    return None
