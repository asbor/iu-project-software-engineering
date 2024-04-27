from fastapi import FastAPI
from setup import engine
from api.router import router
import database.models.models as models
from fastapi.middleware.cors import CORSMiddleware

# create the database tables if they do not exist already
models.Base.metadata.create_all(bind=engine)

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


@app.get("/")
def read_root():
    return {"Hello": "World"}
