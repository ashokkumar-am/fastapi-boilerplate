from fastapi import APIRouter
from app.schemas.user import User
from app.services.user_service import get_user_info

router = APIRouter()

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    return await get_user_info(user_id)
