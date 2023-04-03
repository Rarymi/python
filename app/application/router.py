from fastapi import APIRouter

from app.application.routes.auth import router as  auth_router
from app.application.routes.feed import router as  feed_router
from app.application.routes.post import router as  post_router
from app.application.routes.comment import router as  comment_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth")
router.include_router(feed_router, prefix="/feed")
router.include_router(post_router, prefix="/post")
router.include_router(comment_router, prefix="/comment")
