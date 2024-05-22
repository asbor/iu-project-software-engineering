from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import Database.Models as models
import Database.Schemas as schemas
from datetime import datetime

router = APIRouter()


@router.post("/batches", response_model=schemas.Batch)
async def create_batch(batch: schemas.BatchCreate, db: Session = Depends(get_db)):
    # Fetch the recipe to copy
    recipe = db.query(models.Recipes).filter(
        models.Recipes.id == batch.recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Create a new batch
    db_batch = models.Batches(
        recipe_id=batch.recipe_id,
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
            display_amount=hop.display_amount,
            inventory=hop.inventory,
            display_time=hop.display_time,
            batch_id=db_batch.id
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
            batch_id=db_batch.id
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
            display_amount=misc.display_amount,
            inventory=misc.inventory,
            display_time=misc.display_time,
            batch_size=misc.batch_size,
            batch_id=db_batch.id
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
            inventory=yeast.inventory,
            display_amount=yeast.display_amount,
            batch_id=db_batch.id
        )
        db.add(db_inventory_yeast)

    db.commit()
    return db_batch
