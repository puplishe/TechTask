from pydantic import BaseModel
from datetime import datetime

class BaseSchema(BaseModel):
    question_id: int
    question_text: str
    question_answer: str
    creation_date: datetime