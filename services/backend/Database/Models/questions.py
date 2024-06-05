# Database/Models/questions.py



from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship

from database import Base





class Questions(Base):

    __tablename__ = "questions"



    id = Column(Integer, primary_key=True, index=True)

    question_text = Column(String, index=True)

    choices = relationship("Choices", back_populates="question")
