from fastapi import APIRouter, status, HTTPException
from typing import List
import uuid
from model.database import SessionLocal
import model.db_models as models
import data.schemas as schemas

router = APIRouter()

db = SessionLocal()


# create a rental
@router.post("/rentals", response_model=schemas.Rental, status_code=status.HTTP_201_CREATED)
def create_rental(rental: schemas.Rental):
    # check if user exists
    user = db.query(models.User).filter(
        models.User.id == rental.user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # check if publication exists
    publication = db.query(models.Publication).filter(
        models.Publication.id == rental.publication_id).first()
    if publication is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")

    # check if rental already exists
    rental_exists = db.query(models.Rental).filter(models.Rental.user_id == rental.user_id).filter(
        models.Rental.publication_id == rental.publication_id).first()
    if rental_exists is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Rental already exists")

    new_rental = models.Rental(
        id=uuid.uuid4(),
        user_id=rental.user_id,
        publication_id=rental.publication_id,
        start_date=rental.start_date,
        end_date=rental.end_date
    )

    db.add(new_rental)
    db.commit()
    db.refresh(new_rental)
    return new_rental

# get all rentals


@router.get("/rentals", status_code=status.HTTP_200_OK)
def get_all_rentals():
    rentals = db.query(models.Rental).all()
    return rentals

# get rentals by id


@router.get("/rentals/{rentalId}", status_code=status.HTTP_200_OK)
def get_rental(rentalId: uuid.UUID):
    rental = db.query(models.Rental).filter(
        models.Rental.id == rentalId).first()
    return rental

# get rentals by user id


@router.get("/rentals/users/{userId}", status_code=status.HTTP_200_OK)
def get_rental_by_user(userId: uuid.UUID):
    rentals = db.query(models.Rental).filter(
        models.Rental.user_id == userId).all()
    return rentals

# get rentals by publication id


@router.get("/rentals/publications/{publicationId}", status_code=status.HTTP_200_OK)
def get_rental_by_publication(publicationId: uuid.UUID):
    rentals = db.query(models.Rental).filter(
        models.Rental.publication_id == publicationId).all()
    return rentals

# delete a rental


@router.delete("/rentals/{rentalId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rental(rentalId: uuid.UUID):
    rental = db.query(models.Rental).filter(
        models.Rental.id == rentalId).first()
    if rental is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rental not found")
    db.delete(rental)
    db.commit()
    return rental

# update a rental


@router.put("/rentals/{rentalId}", status_code=status.HTTP_202_ACCEPTED)
def update_rental(rentalId: uuid.UUID, rental: schemas.Rental):
    rental_exists = db.query(models.Rental).filter(
        models.Rental.id == rentalId).first()
    if rental_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rental not found")
    rental_exists.user_id = rental.user_id
    rental_exists.publication_id = rental.publication_id
    rental_exists.created_at = rental.created_at
    db.commit()
    db.refresh(rental_exists)
    return rental_exists
