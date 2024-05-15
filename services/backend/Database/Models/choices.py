from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base


class Choices(Base):
    """
    Description:
    This class represents the Choice table in the database.

    Relationships:
    - ONE choice can have only ONE question
    """

    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)

    # Relationships
    question_id = Column(Integer, ForeignKey('questions.id'))
