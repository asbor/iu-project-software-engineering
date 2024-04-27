from fastapi import APIRouter

from api.endpoints import authors
from api.endpoints import user

# create the router and include all the routers from the endpoints folder
router = APIRouter()
router.include_router(authors.router, tags=["authors"])
router.include_router(user.router, tags=["user"])
