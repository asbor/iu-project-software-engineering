from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base


class Questions(Base):
    """
    Description:
    This class represents the Question table in the database.

    Relationships:
    - ONE question can have ONE or MANY choices
    """
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
