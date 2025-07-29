from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.user import User
from schemas.user_schema import UserCreate

async def create_user(user_data: UserCreate, db: AsyncSession) -> User:
    """Создание пользователя"""
    user = User(**user_data.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_users(db: AsyncSession) -> list[User]:
    """Получить всех пользователей"""
    result = await db.execute(select(User))
    return result.scalars().all()
