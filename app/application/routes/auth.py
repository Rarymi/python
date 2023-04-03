from fastapi import APIRouter

from DTO.login_dto import LoginDTO

router = APIRouter()

@router.post("/login")
def login(user: LoginDTO):
    return {"user": user}