from fastapi import APIRouter
from .endpoints import *

# create the router and include all the routers from the endpoints folder
router = APIRouter()
router.include_router(recipes.router, tags=["recipes"])
router.include_router(hops.router, tags=["hops"])
router.include_router(miscs.router, tags=["miscs"])
router.include_router(yeasts.router, tags=["yeasts"])
router.include_router(fermentables.router, tags=["fermentables"])

router.include_router(logs.router, tags=["logs"])
router.include_router(questions.router, tags=["questions"])
router.include_router(style_guidelines.router, tags=["style_guidelines"])


# Profile routers
router.include_router(mash_profiles.router, tags=["mash_profiles"])
router.include_router(water_profiles.router, tags=["water_profiles"])
router.include_router(equipment_profiles.router, tags=["equipment_profiles"])

# TODO: The following routers will be built at a later time
router.include_router(users.router, tags=["user"])
