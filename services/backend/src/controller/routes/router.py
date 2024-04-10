from controller.api import user
from controller.api import categories
from controller.api import authors
from fastapi import APIRouter


# create the router and include all the routers from the endpoints folder
router = APIRouter()
router.include_router(authors.router, tags=["authors"])
router.include_router(categories.router, tags=["categories"])
router.include_router(user.router, tags=["user"])
