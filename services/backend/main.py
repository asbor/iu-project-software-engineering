from fastapi import FastAPI
from setup import engine
from api.router import router
from database.models.base import Base
from fastapi.middleware.cors import CORSMiddleware
from beer_styles_processing import main

# Connect to the database (bind the engine)
# Create the tables in the database (create_all)
Base.metadata.create_all(bind=engine)

# create the FastAPI app and include the router from the endpoints folder
app = FastAPI(title="PostgreSQL and FastAPI")
app.include_router(router)

# create a root endpoint

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# main()


@app.get("/")
def read_root():
    return {"Hello": "World"}
