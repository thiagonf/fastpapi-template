from fastapi import APIRouter

from . import bills
from app.auth import user

api_router = APIRouter()
api_router.include_router(bills.router, tags=["bills"])
api_router.include_router(user.router, tags=["users"])
