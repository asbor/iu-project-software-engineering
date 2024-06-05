# backend/api/router.py

from fastapi import APIRouter
from .endpoints import (
    recipes,
    batches,
    hops,
    miscs,
    yeasts,
    fermentables,
    health,
    logs,
    questions,
    style_guidelines,
    references,
    mash_profiles,
    water_profiles,
    equipment_profiles,
    users,
    trigger_beer_styles_processing,
)

# create the router and include all the routers from the endpoints folder

router = APIRouter()
router.include_router(recipes.router, tags=["recipes"])
router.include_router(batches.router, tags=["batches"])
router.include_router(hops.router, tags=["hops"])
router.include_router(miscs.router, tags=["miscs"])
router.include_router(yeasts.router, tags=["yeasts"])
router.include_router(fermentables.router, tags=["fermentables"])
router.include_router(health.router, tags=["health"])
router.include_router(logs.router, tags=["logs"])
router.include_router(questions.router, tags=["questions"])
router.include_router(style_guidelines.router, tags=["style_guidelines"])
router.include_router(references.router, tags=["references"])

# Profile routers

router.include_router(mash_profiles.router, tags=["mash_profiles"])
router.include_router(water_profiles.router, tags=["water_profiles"])
router.include_router(equipment_profiles.router, tags=["equipment_profiles"])
router.include_router(users.router, tags=["user"])

# Include the script router

router.include_router(
    trigger_beer_styles_processing.router, tags=["refresh-beer-styles"]
)
