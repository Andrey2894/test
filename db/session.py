from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# URL подключения к PostgreSQL через async драйвер (asyncpg)
DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost/test"

# Создаём async движок (в отличие от обычного create_engine)
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаём сессию для работы с БД — это как EntityManager в Java
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Зависимость, которая будет автоматически передавать сессию в endpoint
async def get_db():
    async with async_session() as session:
        yield session
