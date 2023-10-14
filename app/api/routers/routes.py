from fastapi import FastAPI

from ..routers.router import router


def include_routers(app: FastAPI):
    prefix = '/api/v1'
    app.include_router(router, prefix=prefix)
