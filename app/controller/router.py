from fastapi import APIRouter

from dbs_assignment.endpoints import authors
from dbs_assignment.endpoints import cards
from dbs_assignment.endpoints import categories
from dbs_assignment.endpoints import instances
from dbs_assignment.endpoints import publications
from dbs_assignment.endpoints import rentals
from dbs_assignment.endpoints import reservation
from dbs_assignment.endpoints import user

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
