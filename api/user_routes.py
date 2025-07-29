from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from schemas.user_schema import UserCreate, UserOut
from services.user_service import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    POST /users/ — регистрация нового пользователя
    """
    return await create_user(user, db)

@router.get("/", response_model=list[UserOut])
async def list_users(db: AsyncSession = Depends(get_db)):
    """
    GET /users/ — список всех пользователей
    """
    return await get_users(db)
