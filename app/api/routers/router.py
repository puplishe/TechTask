from typing import Any

from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from ...services.service import QuestionService

router = APIRouter()


@cbv(router)
class QestionRouter:

    def __init__(self, question_service: QuestionService = Depends()) -> None:
        self._question_service = question_service

    @router.post('/questions/{questions_num}')
    async def questions(self, question_num: int) -> dict[str, Any | None]:

        return await self._question_service.questions(question_num)
