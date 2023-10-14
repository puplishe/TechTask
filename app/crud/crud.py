from typing import Any

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.db_conn import get_db
from ..models.models import QuestionModel
from ..models.schema.base import BaseSchema


class QuestionsCrud:
    def __init__(self, db: AsyncSession = Depends(get_db)) -> None:
        self.db = db
        self._model = QuestionModel

    async def create_question(self, data: BaseSchema) -> dict[str, Any]:
        new_question = self._model(**data.dict())
        self.db.add(new_question)
        await self.db.commit()
        return new_question.as_dict()

    async def get_questions(self) -> list[QuestionModel]:
        stmt = select(self._model)
        questions = (await self.db.execute(stmt)).scalars().all()
        return questions

    async def get_question(self, question_id: int) -> QuestionModel:
        stmt = select(self._model).where(self._model.question_id == question_id)
        question = (await self.db.execute(stmt)).scalars().first()
        if question is None:
            return 'question not in db'
        else:
            return question
