from datetime import datetime

import httpx
from fastapi import HTTPException

from ...models.schema.base import BaseSchema


async def quesition_request(question_num: int) -> list[BaseSchema]:
    url = f'https://jservice.io/api/random?count={question_num}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        data = response.json()
        questions = []
        for item in data:
            question_id = item['id']
            question_text = item['question']
            question_answer = item['answer']
            created_at = datetime.strptime(item['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
            question = BaseSchema(
                question_id=question_id,
                question_text=question_text,
                question_answer=question_answer,
                creation_date=created_at
            )
            questions.append(question)
        return questions
    else:
        raise HTTPException(status_code=response.status_code, detail='error occured on external api service')
