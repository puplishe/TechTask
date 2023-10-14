from sqlalchemy import Column, DateTime, Integer, String

from ..db.db_conn import Base


class QuestionModel(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer)
    question_text = Column(String, unique=True, nullable=False)
    question_answer = Column(String, nullable=False)
    creation_date = Column(DateTime, nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'question_text': self.question_text,
            'question_answer': self.question_answer,
            'creation_date': self.creation_date,
        }
