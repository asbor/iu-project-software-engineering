from fastapi import APIRouter, HTTPException, status
import uuid
from app.model.database import SessionLocal
import app.model.db_models as models
import app.data.schemas as schemas

router = APIRouter()
db = SessionLocal()


# Get all card
@router.get("/card", response_model=list[schemas.Card])
def get_all_card():
    return db.query(models.Card).all()


# Get a card by id
@router.get("/card/{cardId}", response_model=schemas.Card)
def get_card(cardId: uuid.UUID):
    db_card = db.query(models.Card).filter(models.Card.id == cardId).first()
    if db_card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
    return db_card


# Update a card
@router.patch("/card/{cardId}", status_code=status.HTTP_200_OK)
def update_card(cardId: uuid.UUID, card: schemas.Card):
    db_card = db.query(models.Card).filter(models.Card.id == cardId).first()

    # card must exist
    if db_card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")

    # card id must not be changed
    if card.id is not None:
        if db_card.id != card.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Card id must not be changed")

    # card magstripe must not be changed
    if card.magstripe is not None:
        if db_card.magstripe != card.magstripe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Magstripe must not be changed")

    # card status must be either active, inactive or expired
    if card.status not in ["active", "inactive", "expired"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Status must be either active, inactive or expired")

    # card user_id must be present in table "user"
    if db.query(models.User).filter(models.User.id == card.user_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user_id not found")

    # card created_at must not be changed
    if card.created_at is not None:
        if db_card.created_at != card.created_at:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Card created_at must not be changed")

    if card.user_id is not None:
        db_card.user_id = card.user_id              # type: ignore

    if card.magstripe is not None:
        db_card.magstripe = card.magstripe          # type: ignore

    if card.status is not None:
        db_card.status = card.status                # type: ignore

    if card.updated_at is not None:
        db_card.updated_at = card.updated_at        # type: ignore

    db.commit()
    db.refresh(db_card)
    return db_card


# Create a card
@router.post("/card", response_model=schemas.Card)
def create_card(card: schemas.Card):

    # user_id must be present in table "user"
    if db.query(models.User).filter(models.User.id == card.user_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user_id not found")

    if db.query(models.Card).filter(models.Card.id == card.id).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Card already exists")

    # card id must be unique
    if db.query(models.Card).filter(models.Card.id == card.id).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Card id must be unique")

    # card magstripe must be unique
    if db.query(models.Card).filter(models.Card.magstripe == card.magstripe).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Card magstripe must be unique")

    # card magstripe must be like "stringstringstringst"
    if len(card.magstripe) != 20:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Card magstripe must be like 'stringstringstringst'")

    # status must be either active, inactive or expired
    if card.status not in ["active", "inactive", "expired"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Status must be either active, inactive or expired")

    new_card = models.Card(
        id=card.id,
        user_id=card.user_id,
        magstripe=card.magstripe,
        status=card.status,
        created_at=card.created_at,
        updated_at=card.updated_at
    )

    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card


# Delete a card
@router.delete("/card/{cardId}", response_model=schemas.Card)
def delete_card(cardId: uuid.UUID):
    db_card = db.query(models.Card).filter(models.Card.id == cardId).first()
    if db_card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")

    db.delete(db_card)
    db.commit()
    return db_card
