from app.controller.api import user
from app.controller.api import reservation
from app.controller.api import publications
from app.controller.api import instances
from app.controller.api import categories
from app.controller.api import cards
from app.controller.api import authors
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
