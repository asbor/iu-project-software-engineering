from uuid import uuid4
from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from database import SessionLocal
import Database.Models as models
import Database.Schemas as schemas


from typing import List
import logging

# Create a logger
logger = logging.getLogger(__name__)

router = APIRouter()

db = SessionLocal()


router = APIRouter()


@router.post("/equipment", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_equipment(equipment: schemas.Equipment):
    # Check if equipment name already exists
    existing_equipment = db.query(models.Equipment).filter(
        models.Equipment.name == equipment.name).first()
    if existing_equipment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Equipment name already exists")

    # Generate unique ID
    equipment_id = str(uuid4())

    # Create new equipment
    new_equipment = models.Equipment(
        id=equipment_id,
        name=equipment.name,
        version=equipment.version if equipment.version else 0,
        boil_size=equipment.boil_size if equipment.boil_size else 0,
        batch_size=equipment.batch_size if equipment.batch_size else 0,
        tun_volume=equipment.tun_volume if equipment.tun_volume else 0,
        tun_weight=equipment.tun_weight if equipment.tun_weight else 0,
        tun_specific_heat=equipment.tun_specific_heat if equipment.tun_specific_heat else 0,
        top_up_water=equipment.top_up_water if equipment.top_up_water else 0,
        trub_chiller_loss=equipment.trub_chiller_loss if equipment.trub_chiller_loss else 0,
        evap_rate=equipment.evap_rate if equipment.evap_rate else 0,
        boil_time=equipment.boil_time if equipment.boil_time else 0,
        calc_boil_volume=equipment.calc_boil_volume if equipment.calc_boil_volume is not None else False,
        lauter_deadspace=equipment.lauter_deadspace if equipment.lauter_deadspace else 0,
        top_up_kettle=equipment.top_up_kettle if equipment.top_up_kettle else 0,
        hop_utilization=equipment.hop_utilization if equipment.hop_utilization else 0,
        notes=equipment.notes if equipment.notes else "",
        display_boil_size=equipment.display_boil_size if equipment.display_boil_size else "",
        display_batch_size=equipment.display_batch_size if equipment.display_batch_size else "",
        display_tun_volume=equipment.display_tun_volume if equipment.display_tun_volume else "",
        display_tun_weight=equipment.display_tun_weight if equipment.display_tun_weight else "",
        display_top_up_water=equipment.display_top_up_water if equipment.display_top_up_water else "",
        display_trub_chiller_loss=equipment.display_trub_chiller_loss if equipment.display_trub_chiller_loss else "",
        display_lauter_deadspace=equipment.display_lauter_deadspace if equipment.display_lauter_deadspace else "",
        display_top_up_kettle=equipment.display_top_up_kettle if equipment.display_top_up_kettle else "",
    )

    # Add equipment to the database
    db.add(new_equipment)
    db.commit()
    db.refresh(new_equipment)

    return {"message": "Equipment created successfully", "equipment_id": equipment_id}


@router.get("/equipment/{equipment_id}", response_model=schemas.Equipment)
def read_equipment(equipment_id: UUID):
    """
    Retrieve an equipment entry from the database.

    Args:
        equipment_id (UUID): The unique identifier for the equipment.

    Returns:
        Equipment: The equipment data retrieved from the database.

    Raises:
        HTTPException: If the equipment data with the specified ID does not exist in the database.
    """
    try:
        equipment = db.query(models.Equipment).filter(
            models.Equipment.id == equipment_id).first()
        if equipment is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
        logger.info("Equipment retrieved successfully")
        return equipment
    except Exception as e:
        logger.error(f"Failed to retrieve equipment: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Failed to retrieve equipment")


@router.put("/equipment/{equipment_id}", response_model=schemas.Equipment)
def update_equipment(equipment_id: UUID, equipment: schemas.Equipment):
    """
    Update an equipment entry in the database.

    Args:
        equipment_id (UUID): The unique identifier for the equipment.
        equipment (Equipment): The equipment data to be added to the database.

    Returns:
        Equipment: The updated equipment data.

    Raises:
        HTTPException: If the equipment data with the specified ID does not exist in the database.
    """
    try:
        equipment_data = db.query(models.Equipment).filter(
            models.Equipment.id == equipment_id).first()
        if equipment_data is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
        for key, value in equipment.dict().items():
            setattr(equipment_data, key, value)
        db.commit()
        db.refresh(equipment_data)
        logger.info("Equipment updated successfully")
        return equipment_data
    except Exception as e:
        logger.error(f"Failed to update equipment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update equipment")


@router.delete("/equipment/{equipment_id}")
async def delete_equipment(equipment_id: UUID):
    """
    Delete an equipment entry from the database.

    Args:
        equipment_id (UUID): The unique identifier for the equipment.

    Returns:
        dict: A dictionary containing a confirmation message.

    Raises:
        HTTPException: If the equipment data with the specified ID does not exist in the database.
    """
    # Retrieve the equipment by ID
    equipment = db.query(models.Equipment).filter(
        models.Equipment.id == equipment_id).first()

    # Check if equipment exists
    if equipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Equipment not found"
        )

    # Delete the equipment
    db.delete(equipment)
    db.commit()

    return {"message": "Equipment deleted successfully"}


@router.get("/equipment", response_model=List[schemas.Equipment])
def get_all_equipment():
    """
    Retrieve all equipment entries from the database.

    Returns:
        List[Equipment]: The list of all equipment entries retrieved from the database.

    Raises:
        HTTPException: If an error occurs while trying to retrieve equipment data from the database.
    """
    equipment = db.query(models.Equipment).all()
    return equipment
