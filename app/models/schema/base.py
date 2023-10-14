from datetime import datetime

from pydantic import BaseModel


class BaseSchema(BaseModel):
    question_id: int
    question_text: str
    question_answer: str
    creation_date: datetime
