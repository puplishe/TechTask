from typing import Any

from fastapi import Depends

from ..api.external_api.questions_requests import quesition_request
from ..crud.crud import QuestionsCrud
from ..models.models import QuestionModel
from ..models.schema.base import BaseSchema


class QuestionService:
    def __init__(self, question_crud: QuestionsCrud = Depends()) -> None:
        self._question_crud = question_crud

    async def questions(self, question_num: int) -> dict[str, Any | None]:
        unique_questions: list[QuestionModel] = []

        db_questions: list[QuestionModel] = await self._question_crud.get_questions()

        while len(unique_questions) < question_num:
            data: list[BaseSchema] = await quesition_request(question_num - len(unique_questions))

            for question in data:
                if not any(db_question.question_text == question.question_text for db_question in db_questions):
                    last_question = await self._question_crud.create_question(question)
                    unique_questions.append(question)
                    db_questions.append(question)

        if unique_questions:
            return last_question
        else:
            return {}
