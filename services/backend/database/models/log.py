# Define the log model

from .base import Base
from sqlalchemy import Column, Integer, String, DateTime


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    level = Column(String)
    message = Column(String)
    timestamp = Column(DateTime)
