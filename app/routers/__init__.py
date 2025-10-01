from fastapi import APIRouter
from .name import router as name_router

router = APIRouter(prefix="/api")

router.include_router(name_router)
