from fastapi import FastAPI
from model.database import engine
from controller.router import router
import model.db_models as models

# create the database tables if they do not exist already
models.Base.metadata.create_all(bind=engine)

# create the FastAPI app and include the router from the endpoints folder
app = FastAPI(title="PostgreSQL and FastAPI")
app.include_router(router)

# create a root endpoint


@app.get("/")
def read_root():
    return {"Hello": "World"}
