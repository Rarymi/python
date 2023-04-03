from fastapi import APIRouter

router = APIRouter()

@router.post("/user")
def createUser():
    return {"novo usuario"}

@router.patch("/user/{user_id}")
def editUser():
    return {"editar usuario"}