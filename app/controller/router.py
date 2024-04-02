from fastapi import APIRouter

from controller.endpoints import authors
from controller.endpoints import cards
from controller.endpoints import categories
from controller.endpoints import instances
from controller.endpoints import publications
from controller.endpoints import rentals
from controller.endpoints import reservation
from controller.endpoints import user

# create the router and include all the routers from the endpoints folder
router = APIRouter()
router.include_router(authors.router, tags=["authors"])
router.include_router(cards.router, tags=["cards"])
router.include_router(categories.router, tags=["categories"])
router.include_router(instances.router, tags=["instances"])
router.include_router(publications.router, tags=["publications"])
router.include_router(rentals.router, tags=["rentals"])
router.include_router(reservation.router, tags=["reservation"])
router.include_router(user.router, tags=["user"])
