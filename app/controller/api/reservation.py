from fastapi import APIRouter, status, HTTPException
from app.model.database import SessionLocal
from typing import List
import uuid
import app.data.schemas as schemas
import app.data.models as models

router = APIRouter()

db = SessionLocal()

# post a new reservation


@router.post("/reservations", response_model=schemas.Reservation, status_code=status.HTTP_201_CREATED)
def create_reservation(reservation: schemas.Reservation):

    # check if user exists
    user = db.query(models.User).filter(
        models.User.id == reservation.user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # check if publication exists
    publication = db.query(models.Publication).filter(
        models.Publication.id == reservation.publication_id).first()
    if publication is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")

    # check if reservation already exists
    reservation_exists = db.query(models.Reservation).filter(models.Reservation.user_id == reservation.user_id).filter(
        models.Reservation.publication_id == reservation.publication_id).first()
    if reservation_exists is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Reservation already exists")

    new_reservation = models.Reservation(
        id=reservation.id,
        user_id=reservation.user_id,
        publication_id=reservation.publication_id,
        created_at=reservation.created_at
    )

    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation


# get all reservations
@router.get("/reservations", status_code=status.HTTP_200_OK)
def get_all_reservations():
    reservations = db.query(models.Reservation).all()
    return reservations


# get reservations by id
@router.get("/reservations/{reservationId}", status_code=status.HTTP_200_OK)
def get_reservation(reservationId: uuid.UUID):
    reservation = db.query(models.Reservation).filter(
        models.Reservation.id == reservationId).first()
    return reservation


# update a reservation
@router.patch("/reservations/{reservationId}", status_code=status.HTTP_202_ACCEPTED)
def update_reservation(reservationId: uuid.UUID, reservation: schemas.Reservation):
    reservation_exists = db.query(models.Reservation).filter(
        models.Reservation.id == reservationId).first()

    # The reservation id must exist in the database
    if reservation_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")

    # The user id must exist in the database
    user = db.query(models.User).filter(
        models.User.id == reservation.user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # The publication id must exist in the database
    publication = db.query(models.Publication).filter(
        models.Publication.id == reservation.publication_id).first()
    if publication is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")

    # the reservation id can not be changed
    if reservation.id != reservation_exists.id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Reservation id can not be changed")

    # the created_at date can not be changed
    if reservation.created_at != reservation_exists.created_at:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Created at date can not be changed")

    reservation_exists.user_id = reservation.user_id                  # type: ignore
    reservation_exists.publication_id = reservation.publication_id    # type: ignore
    reservation_exists.created_at = reservation.created_at            # type: ignore
    reservation_exists.updated_at = reservation.updated_at            # type: ignore

    db.commit()
    db.refresh(reservation_exists)
    return reservation_exists


# delete a reservation
@router.delete("/reservations/{reservationId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation(reservationId: uuid.UUID):
    reservation = db.query(models.Reservation).filter(
        models.Reservation.id == reservationId).first()
    if reservation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")

    db.delete(reservation)
    db.commit()

    return "Reservation deleted"
