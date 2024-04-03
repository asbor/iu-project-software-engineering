from app.controller.endpoints import user
from app.controller.endpoints import reservation
from app.controller.endpoints import publications
from app.controller.endpoints import instances
from app.controller.endpoints import categories
from app.controller.endpoints import cards
from app.controller.endpoints import authors
from fastapi import APIRouter


# create the router and include all the routers from the endpoints folder
router = APIRouter()
router.include_router(authors.router, tags=["authors"])
router.include_router(cards.router, tags=["cards"])
router.include_router(categories.router, tags=["categories"])
router.include_router(instances.router, tags=["instances"])
router.include_router(publications.router, tags=["publications"])
router.include_router(reservation.router, tags=["reservation"])
router.include_router(user.router, tags=["user"])
