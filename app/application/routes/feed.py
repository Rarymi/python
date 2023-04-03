from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def findAllFeed():
    return {"aqui é o feed"}