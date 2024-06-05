# api/endpoints/batches.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from database import get_db
import Database.Models as models
import Database.Schemas as schemas
from datetime import datetime
from typing import List
import re
import logging

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_numeric_value(value):
    match = re.match(r"(\d+(\.\d+)?)", value)
    if match:
        return float(match.group(1))
    return 0.0

# Create a new batch


@router.post("/batches", response_model=schemas.Batch)
async def create_batch(
    batch: schemas.BatchCreate, db: Session = Depends(get_db)
):
    try:
        # Fetch the recipe to copy
        recipe = (
            db.query(models.Recipes)
            .options(
                joinedload(models.Recipes.hops),
                joinedload(models.Recipes.fermentables),
                joinedload(models.Recipes.yeasts),
                joinedload(models.Recipes.miscs),
            )
            .filter(models.Recipes.id == batch.recipe_id)
            .first()
        )
        if not recipe:
            logger.error(f"Recipe with id {batch.recipe_id} not found")
            raise HTTPException(status_code=404, detail="Recipe not found")

        # Create a copy of the recipe with the is_batch flag set to true
        batch_recipe = models.Recipes(
            name=recipe.name,
            is_batch=True,
            origin_recipe_id=recipe.id,
            version=recipe.version,
            type=recipe.type,
            brewer=recipe.brewer,
            asst_brewer=recipe.asst_brewer,
            batch_size=recipe.batch_size,
            boil_size=recipe.boil_size,
            boil_time=recipe.boil_time,
            efficiency=recipe.efficiency,
            notes=recipe.notes,
            taste_notes=recipe.taste_notes,
            taste_rating=recipe.taste_rating,
            og=recipe.og,
            fg=recipe.fg,
            fermentation_stages=recipe.fermentation_stages,
            primary_age=recipe.primary_age,
            primary_temp=recipe.primary_temp,
            secondary_age=recipe.secondary_age,
            secondary_temp=recipe.secondary_temp,
            tertiary_age=recipe.tertiary_age,
            age=recipe.age,
            age_temp=recipe.age_temp,
            carbonation_used=recipe.carbonation_used,
            est_og=recipe.est_og,
            est_fg=recipe.est_fg,
            est_color=recipe.est_color,
            ibu=recipe.ibu,
            ibu_method=recipe.ibu_method,
            est_abv=recipe.est_abv,
            abv=recipe.abv,
            actual_efficiency=recipe.actual_efficiency,
            calories=recipe.calories,
            display_batch_size=recipe.display_batch_size,
            display_boil_size=recipe.display_boil_size,
            display_og=recipe.display_og,
            display_fg=recipe.display_fg,
            display_primary_temp=recipe.display_primary_temp,
            display_secondary_temp=recipe.display_secondary_temp,
            display_tertiary_temp=recipe.display_tertiary_temp,
            display_age_temp=recipe.display_age_temp,
        )
        db.add(batch_recipe)
        db.commit()
        db.refresh(batch_recipe)

        # Create a new batch
        db_batch = models.Batches(
            recipe_id=batch_recipe.id,
            batch_name=batch.batch_name,
            batch_number=batch.batch_number,
            batch_size=batch.batch_size,
            brewer=batch.brewer,
            brew_date=batch.brew_date,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        db.add(db_batch)
        db.commit()
        db.refresh(db_batch)

        # Copy ingredients to inventory tables
        for hop in recipe.hops:
            db_inventory_hop = models.InventoryHop(
                name=hop.name,
                origin=hop.origin,
                alpha=hop.alpha,
                type=hop.type,
                form=hop.form,
                beta=hop.beta,
                hsi=hop.hsi,
                amount=hop.amount,
                use=hop.use,
                time=hop.time,
                notes=hop.notes,
                display_amount=(
                    hop.display_amount if hop.display_amount else ""
                ),
                inventory=(
                    parse_numeric_value(hop.inventory)
                    if hop.inventory
                    else 0.0
                ),
                display_time=hop.display_time if hop.display_time else "",
                batch_id=db_batch.id,
            )
            db.add(db_inventory_hop)
        for fermentable in recipe.fermentables:
            db_inventory_fermentable = models.InventoryFermentable(
                name=fermentable.name,
                type=fermentable.type,
                yield_=fermentable.yield_,
                color=fermentable.color,
                origin=fermentable.origin,
                supplier=fermentable.supplier,
                notes=fermentable.notes,
                potential=fermentable.potential,
                amount=fermentable.amount,
                cost_per_unit=fermentable.cost_per_unit,
                manufacturing_date=fermentable.manufacturing_date,
                expiry_date=fermentable.expiry_date,
                lot_number=fermentable.lot_number,
                exclude_from_total=fermentable.exclude_from_total,
                not_fermentable=fermentable.not_fermentable,
                description=fermentable.description,
                substitutes=fermentable.substitutes,
                used_in=fermentable.used_in,
                batch_id=db_batch.id,
            )
            db.add(db_inventory_fermentable)
        for misc in recipe.miscs:
            db_inventory_misc = models.InventoryMisc(
                name=misc.name,
                type=misc.type,
                use=misc.use,
                amount_is_weight=misc.amount_is_weight,
                use_for=misc.use_for,
                notes=misc.notes,
                amount=misc.amount,
                time=misc.time,
                display_amount=(
                    misc.display_amount if misc.display_amount else ""
                ),
                inventory=(
                    parse_numeric_value(misc.inventory)
                    if misc.inventory
                    else 0.0
                ),
                display_time=misc.display_time if misc.display_time else "",
                batch_size=misc.batch_size,
                batch_id=db_batch.id,
            )
            db.add(db_inventory_misc)
        for yeast in recipe.yeasts:
            db_inventory_yeast = models.InventoryYeast(
                name=yeast.name,
                type=yeast.type,
                form=yeast.form,
                laboratory=yeast.laboratory,
                product_id=yeast.product_id,
                min_temperature=yeast.min_temperature,
                max_temperature=yeast.max_temperature,
                flocculation=yeast.flocculation,
                attenuation=yeast.attenuation,
                notes=yeast.notes,
                best_for=yeast.best_for,
                max_reuse=yeast.max_reuse,
                amount=yeast.amount,
                amount_is_weight=yeast.amount_is_weight,
                batch_id=db_batch.id,
            )
            db.add(db_inventory_yeast)
        db.commit()
        return db_batch
    except Exception as e:
        logger.error(f"Error creating batch: {e}", exc_info=True)
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Get all batches


@router.get("/batches", response_model=List[schemas.Batch])
async def get_all_batches(db: Session = Depends(get_db)):
    batches = (
        db.query(models.Batches)
        .options(joinedload(models.Batches.recipe))
        .all()
    )
    return batches

# Get a batch by ID


@router.get("/batches/{batch_id}", response_model=schemas.Batch)
async def get_batch_by_id(batch_id: int, db: Session = Depends(get_db)):
    batch = (
        db.query(models.Batches)
        .options(
            joinedload(models.Batches.recipe),
            joinedload(models.Batches.fermentables),
            joinedload(models.Batches.hops),
            joinedload(models.Batches.miscs),
            joinedload(models.Batches.yeasts),
        )
        .filter(models.Batches.id == batch_id)
        .first()
    )
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch

# Update a batch by ID


@router.put("/batches/{batch_id}", response_model=schemas.Batch)
async def update_batch(
    batch_id: int, batch: schemas.BatchBase, db: Session = Depends(get_db)
):
    db_batch = (
        db.query(models.Batches).filter(models.Batches.id == batch_id).first()
    )
    if not db_batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    # Update the batch
    for key, value in batch.dict().items():
        setattr(db_batch, key, value)
    db.commit()
    db.refresh(db_batch)
    return db_batch

# Delete a batch by ID


@router.delete("/batches/{batch_id}")
async def delete_batch(batch_id: int, db: Session = Depends(get_db)):
    db_batch = (
        db.query(models.Batches).filter(models.Batches.id == batch_id).first()
    )
    if not db_batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    # Delete related inventory items
    db.query(models.InventoryHop).filter(
        models.InventoryHop.batch_id == batch_id
    ).delete()
    db.query(models.InventoryFermentable).filter(
        models.InventoryFermentable.batch_id == batch_id
    ).delete()
    db.query(models.InventoryMisc).filter(
        models.InventoryMisc.batch_id == batch_id
    ).delete()
    db.query(models.InventoryYeast).filter(
        models.InventoryYeast.batch_id == batch_id
    ).delete()
    # Delete the batch
    db.delete(db_batch)
    db.commit()
    return {"message": "Batch deleted successfully"}
