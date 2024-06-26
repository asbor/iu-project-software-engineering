from fastapi import FastAPI
from database import engine, Base
from api.router import router
from fastapi.middleware.cors import CORSMiddleware
from logger_config import get_logger

# Get logger instance

logger = get_logger("Main")

# Connect to the database (bind the engine)
# Create the tables in the database (create_all)
logger.info("Connecting to the database and creating tables")
Base.metadata.create_all(bind=engine)

# Create the FastAPI app and include the router from the endpoints folder

logger.info("Creating FastAPI app and including the router")
app = FastAPI(title="PostgreSQL and FastAPI")
app.include_router(router)

# Add CORS middleware to allow requests from the frontend

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
