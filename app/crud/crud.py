from typing import Any

from fastapi import Depends
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from db.db_conn import get_db
from models.models import *
from models.schema.base import BaseSchema

class QuestionsCrud:
    def __init__(self, db: AsyncSession = Depends(get_db)) -> None:
        self.db = db
        self._model = QuestionModel
    
    async def create_question(self, data: BaseSchema):
        pass