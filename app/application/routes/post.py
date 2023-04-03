from fastapi import APIRouter

from utils.mocks.post import generate_mock_posts, generate_post

router = APIRouter()

@router.get("/")
def find_all_posts():
    return generate_mock_posts(3)


@router.get("/{post_id}")
def findOnePost(post_id: int):
    return generate_post(post_id)


@router.post("/new-post")
def create_new_post():
    return {"novo post"}


@router.patch("/{post_id}")
def edit_post(post_id: int):
    return generate_post(post_id)
