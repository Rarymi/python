from fastapi import APIRouter

from utils.mocks.comment import generate_mock_comments, generate_comment

router = APIRouter()

@router.get("/")
def find_all_comments():
    return generate_mock_comments(3)


@router.get("/{comment_id}")
def findOnePost(comment_id: int):
    return generate_comment(comment_id)


@router.post("/new-comment")
def create_new_post():
    return {"novo post"}


@router.patch("/{comment_id}")
def edit_post(comment_id: int):
    return generate_comment(comment_id)
