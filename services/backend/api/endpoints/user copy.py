from datetime import datetime
from fastapi import APIRouter, HTTPException, status
from database import SessionLocal
from pydantic import validate_email
from uuid import UUID
import Database.Models as models
import Database.Schemas as schemas
import re

router = APIRouter()

db = SessionLocal()


def email_validation(email):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\\.[a-z]{1,3}$"
    if re.match(pat, email):
        return True
    return False


@router.get("/user", status_code=status.HTTP_200_OK)
async def get_user():
    users = db.query(models.User).all()
    return users


# Return a user by id


@router.get("/user/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: UUID):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


# Update a user


@router.patch("/user/{user_id}", status_code=status.HTTP_200_OK)
async def patch_user(user_id: UUID, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    # The user id must exist in the database
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    # The user id cannot be changed
    if user.id is not None:
        if db_user.id != user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User id cannot be changed",
            )

    # FUNCTION TO VALIDATE EMAIL ADDRESS
    if email_validation(user.email) == False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email address is not valid",
        )

    # the email address must be unique, so if it is changed, it must be unique
    # in the database, if it is not changed, then it can be ignored, and the
    # email address can be the same as the one in the database
    if user.email is not None:
        if db_user.email != user.email:
            if (
                db.query(models.User)
                .filter(models.User.email == user.email)
                .first()
                is not None
            ):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email address already exists",
                )

    # if the personal identificator is changed, it must be unique. If it is not changed, then it can be ignored.
    # numbers only, 10 digits long
    if user.personal_identificator is not None:
        if db_user.personal_identificator != user.personal_identificator:
            if (
                db.query(models.User)
                .filter(
                    models.User.personal_identificator
                    == user.personal_identificator
                )
                .first()
                is not None
            ):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Personal identificator already exists",
                )

            if len(user.personal_identificator) != 10:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Personal identificator must be 10 digits long",
                )

            if not user.personal_identificator.isdigit():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Personal identificator must be numbers only",
                )

    if user.name is not None:
        db_user.name = user.name  # type: ignore
    if user.surname is not None:
        db_user.surname = user.surname  # type: ignore
    if user.email is not None:
        db_user.email = user.email  # type: ignore
    if user.birth_date is not None:
        db_user.birth_date = user.birth_date  # type: ignore
    if user.personal_identificator is not None:
        db_user.personal_identificator = user.personal_identificator  # type: ignore
    if user.reservations is not None:
        db_user.reservations = user.reservations
    if user.rentals is not None:
        db_user.rentals = user.rentals

    # updating the updated_at field
    db_user.updated_at = user.updated_at  # type: ignore

    db.commit()
    db.refresh(db_user)

    return db_user


# delete a user


@router.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: UUID):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    db.delete(db_user)
    db.commit()

    return "User deleted"


# Create a new user


@router.post(
    "/user", response_model=schemas.User, status_code=status.HTTP_201_CREATED
)
async def create_user(user: schemas.User):
    # user id must be unique
    if (
        db.query(models.User).filter(models.User.id == user.id).first()
        is not None
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User id already exists",
        )

    # FUNCTION TO VALIDATE EMAIL ADDRESS
    if validate_email(user.email) is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email address is not valid",
        )

    # email address must be unique
    if (
        db.query(models.User).filter(models.User.email == user.email).first()
        is not None
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    # personal identificator must be unique
    if (
        db.query(models.User)
        .filter(
            models.User.personal_identificator == user.personal_identificator
        )
        .first()
        is not None
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Personal identificator already exists",
        )

    # Personal identificator must be 10 digits long
    if len(user.personal_identificator) != 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Personal identificator must be 10 digits long",
        )

    # Personal identificator must be numbers only
    if not user.personal_identificator.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Personal identificator must be numbers only",
        )

    # birth_date must be in a valid format
    try:
        datetime.strptime(user.birth_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Birth date must be in a valid format like 1999-12-31",
        )

    # generate user id if it is not provided
    if user.id is None:
        user.id = UUID.generate()

    new_user = models.User(
        id=user.id,
        name=user.name,
        surname=user.surname,
        email=user.email,
        birth_date=user.birth_date,
        personal_identificator=user.personal_identificator,
        reservations=user.reservations,
        rentals=user.rentals,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
