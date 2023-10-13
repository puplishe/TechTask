from sqlalchemy import ForeignKey, Column, String, Integer, DateTime
from datetime import datetime

from models.models import Base

class QuestionModel(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer)
    question_text = Column(String, unique=True, nullable=False)
    question_answer = Column(String, nullable=False)
    creation_date = Column(DateTime, nullable=False)