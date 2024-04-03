from fastapi import FastAPI
from app.model.database import engine
from app.controller.router import router
from app.model import db_models

# create the database tables if they do not exist already
db_models.Base.metadata.create_all(bind=engine)

# create the FastAPI app and include the router from the endpoints folder
app = FastAPI(title="PostgreSQL and FastAPI")
app.include_router(router)

# create a root endpoint


@app.get("/")
def read_root():
    return {"Hello": "World"}
