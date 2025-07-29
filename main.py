from fastapi import FastAPI                           # Импортируем FastAPI для создания приложения
from contextlib import asynccontextmanager             # Для объединённого управления lifespan (startup/shutdown)
from api import user_routes                        # Наши роуты (контроллеры) для работы с пользователями
from models.user import Base                       # Метаинформация о моделях SQLAlchemy (таблицы)
from db.session import engine                      # Асинхронный движок SQLAlchemy для подключения к БД

# Создаём менеджер жизненного цикла приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    # === Startup ===
    # Открываем соединение и создаём таблицы (если их нет)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # После этого FastAPI начинает принимать запросы
    # === Shutdown ===
    # Здесь можно закрыть соединения, выгрузить логи и т.п.
    # Например:
    # await engine.dispose()

# Инициализация FastAPI с нашим lifespan
app = FastAPI(lifespan=lifespan)

# Подключаем все маршруты из user_routes под префиксом, заданным внутри router
app.include_router(user_routes.router)

# Блок ниже позволяет запускать сервер командой "python main.py"
if __name__ == "__main__":
    import uvicorn
    # Запускаем Uvicorn на localhost:8000 с перезагрузкой при изменениях
    uvicorn.run(
        "main:app",      # точка входа — модуль main, объект app
        host="127.0.0.1",
        port=8000,
        reload=True      # авто-reload при правках кода (только для разработки)
    )
