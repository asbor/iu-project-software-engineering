from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class BatchLogs(Base):
    __tablename__ = "batch_logs"
    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    timestamp = Column(DateTime, default=datetime.now)
    activity = Column(String, nullable=False)
    notes = Column(String, nullable=True)
# Relationship to Batches


    batch = relationship("Batches", back_populates="batch_log")
