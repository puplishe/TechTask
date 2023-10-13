from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

router = APIRouter()

@cbv(router)
class QestionRouter:


    @router.post('/questions/{questions_num}')
    async def questions(self, questions_num: int):
        pass