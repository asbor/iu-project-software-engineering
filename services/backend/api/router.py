from fastapi import APIRouter
from .endpoints import *

# create the router and include all the routers from the endpoints folder
router = APIRouter()
router.include_router(equipment.router, tags=["equipment"])
router.include_router(fermentable.router, tags=["fermentable"])
router.include_router(hop.router, tags=["hop"])
router.include_router(mash.router, tags=["mash"])
router.include_router(misc.router, tags=["misc"])
router.include_router(style.router, tags=["style"])
router.include_router(user.router, tags=["user"])
router.include_router(logs.router, tags=["logs"])
router.include_router(questions.router, tags=["questions"])

router.include_router(recipes.router, tags=["recipes"])
# router.include_router(water.router, tags=["water"])
# router.include_router(yeast.router, tags=["yeast"])
