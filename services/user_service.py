from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User
from schemas.user_schema import UserCreate

# Сервис для создания пользователя
async def create_user(user_data: UserCreate, db: AsyncSession):
    user = User(**user_data.dict())    # Распаковываем данные из Pydantic в SQLAlchemy объект
    db.add(user)                       # Добавляем в сессию
    await db.commit()                 # Коммитим транзакцию
    await db.refresh(user)           # Обновляем из БД (получаем ID)
    return user

# Сервис для получения всех пользователей
async def get_users(db: AsyncSession):
    result = await db.execute(select(User))  # Выполняем SELECT * FROM users
    return result.scalars().all()            # Возвращаем список пользователей
