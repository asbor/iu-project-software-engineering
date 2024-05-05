from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from setup import SessionLocal
import database.models as models
import database.schemas as schemas
from api.validation.mash_validation import MashCreate
from typing import List
from uuid import uuid4

router = APIRouter()
db = SessionLocal()


@router.post("/mash", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_mash(mash: MashCreate):
    # Check if mash name already exists
    existing_mash = db.query(models.Mash).filter(
        models.Mash.name == mash.name).first()
    if existing_mash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Mash name already exists")

    # Generate unique ID
    mash_id = str(uuid4())

    # Create new mash profile
    new_mash = models.Mash(
        id=mash_id,
        name=mash.name,
        version=mash.version,
        grain_temp=mash.grain_temp,
        tun_temp=mash.tun_temp,
        sparge_temp=mash.sparge_temp,
        ph=mash.ph,
        tun_weight=mash.tun_weight,
        tun_specific_heat=mash.tun_specific_heat,
        # equip_adjust=mash.equip_adjust,
        notes=mash.notes if mash.notes else "",
        display_grain_temp=mash.display_grain_temp if mash.display_grain_temp else "",
        display_tun_temp=mash.display_tun_temp if mash.display_tun_temp else "",
        display_sparge_temp=mash.display_sparge_temp if mash.display_sparge_temp else "",
        display_tun_weight=mash.display_tun_weight if mash.display_tun_weight else "",
        # recipe_id=mash.recipe_id,
        # recipe=mash.recipe
    )

    # Add mash profile to the database
    db.add(new_mash)
    db.commit()
    db.refresh(new_mash)

    return {"message": "Mash profile created successfully", "mash_id": mash_id}


@router.get("/mash", response_model=List[schemas.Mash])
def get_all_mash():
    """
    Retrieve all mash entries from the database.

    Returns:
        List[mash]: The list of all mash entries retrieved from the database.

    Raises:
        HTTPException: If an error occurs while trying to retrieve mash data from the database.
    """
    mash = db.query(models.Mash).all()
    return mash


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
