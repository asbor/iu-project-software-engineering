from fastapi import APIRouter, status, HTTPException
from dbs_assignment.database import SessionLocal
from typing import List
import uuid
import dbs_assignment.schemas as schemas
import dbs_assignment.models as models

router = APIRouter()

db=SessionLocal()


# create an instance
@router.post("/instances", response_model=schemas.Instance, status_code=status.HTTP_201_CREATED)
def create_instance(instance: schemas.Instance):
    
    # allowed status
    if instance.status != "available" and instance.status != "reserved":
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Status can only be changed to available or reserved")

    # check if publication exists
    publication = db.query(models.Publication).filter(models.Publication.id == instance.publication_id).first()
    if publication is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")


    new_instance = models.Instance(
        id=instance.id,
        type=instance.type,
        publisher=instance.publisher,
        year=instance.year,
        status=instance.status,
        publication_id=instance.publication_id
    )

    db.add(new_instance)
    db.commit()
    db.refresh(new_instance)
    return new_instance

# get all instances
@router.get("/instances", status_code=status.HTTP_200_OK)
def get_all_instances():
    instances = db.query(models.Instance).all()
    return instances

# get instance by id
@router.get("/instances/{instanceId}", status_code=status.HTTP_200_OK)
def get_instance(instanceId: uuid.UUID):
    instance = db.query(models.Instance).filter(models.Instance.id == instanceId).first()
    return instance

# get instances by publication id
@router.get("/instances/publications/{publicationId}", status_code=status.HTTP_200_OK)
def get_instance_by_publication(publicationId: uuid.UUID):
    instances = db.query(models.Instance).filter(models.Instance.publication_id == publicationId).all()
    return instances

# get instances by status
@router.get("/instances/status/{status}", status_code=status.HTTP_200_OK)
def get_instance_by_status(status: str):
    instances = db.query(models.Instance).filter(models.Instance.status == status).all()
    return instances

# update instance status
@router.patch("/instances/{instanceId}", status_code=status.HTTP_202_ACCEPTED)
def update_instance(instanceId: uuid.UUID, instance: schemas.Instance):
    instance_exists = db.query(models.Instance).filter(models.Instance.id == instanceId).first()
    if instance_exists is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instance not found")
    
    # allowed status
    if instance.status != "available" and instance.status != "reserved":
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Status can only be changed to available or reserved")
    
    # The instance id must exist in the database
    if instance_exists.id != instance.id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Instance id can not be changed")
    
    # The publication id must exist in the database
    publication = db.query(models.Publication).filter(models.Publication.id == instance.publication_id).first()
    if publication is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")
    
    # the created_at fields must not be changed
    if instance_exists.created_at != instance.created_at:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Created at can not be changed {instance_exists.created_at} != {instance.created_at}")
    
    # the updated_at fields must be updated
    if instance_exists.updated_at == instance.updated_at:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Updated at must be updated {instance_exists.updated_at} == {instance.updated_at}")


    instance_exists.type=instance.type                      # type: ignore
    instance_exists.publisher=instance.publisher            # type: ignore
    instance_exists.year=instance.year                      # type: ignore
    instance_exists.status=instance.status                  # type: ignore
    instance_exists.publication_id=instance.publication_id  # type: ignore
    instance_exists.updated_at=instance.updated_at          # type: ignore
    instance_exists.created_at=instance.created_at          # type: ignore

    db.commit()
    db.refresh(instance_exists)
    return instance_exists


# delete instance
@router.delete("/instances/{instanceId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_instance(instanceId: uuid.UUID):
    instance = db.query(models.Instance).filter(models.Instance.id == instanceId).first()
    if instance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instance not found")
    db.delete(instance)
    db.commit()
    return "Instance deleted"



