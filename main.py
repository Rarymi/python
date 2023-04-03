from typing import Union
from DTO.login_dto import LoginDTO

from fastapi import FastAPI

from app.application.router import router

app = FastAPI()


app.include_router(router)