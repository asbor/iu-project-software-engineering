"""
File:           main.py
Author:         Asbjorn Bordoy
Email:          asbjorn.bordoy@gmail.com
Description:    Main file for the FastAPI application
Date:           2024-apr-04
"""

from app.model import db_models
from app.model.database import engine
from fastapi import FastAPI
from app.controller.router import router

# create the database tables if they do not exist already
db_models.Base.metadata.create_all(bind=engine)

# create the FastAPI app and include the router from the endpoints folder
app = FastAPI(title="PostgreSQL and FastAPI")
app.include_router(router)

# create a root endpoint


@app.get("/")
def read_root():
    return {"Hello": "World"}
