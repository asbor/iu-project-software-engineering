from fastapi import APIRouter

from api.endpoints import authors
from services.backend.api.endpoints import users

# create the router and include all the routers from the endpoints folder
router = APIRouter()
router.include_router(authors.router, tags=["authors"])
router.include_router(users.router, tags=["user"])
