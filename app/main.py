"""
File:           main.py
Author:         Asbjorn Bordoy
Email:          asbjorn.bordoy@gmail.com
Description:    Main file for the FastAPI application
Date:           2024-apr-04
"""

from model import db_models
from model.database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
from app.controller.routes.router import router

# create the database tables if they do not exist already
db_models.Base.metadata.create_all(bind=engine)

# create the FastAPI app and include the router from the endpoints folder
app = FastAPI(title="PostgreSQL and FastAPI")
app.include_router(router)

# create a root endpoint

# NEW
# CORSMiddleware is required to make cross-origin requests -- i.e., requests that originate from a different protocol, IP address, domain name, or port. This is necessary since the frontend will run at http://localhost:8080.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
