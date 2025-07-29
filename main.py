from fastapi import FastAPI
from api import user_routes
from models.user import Base
from db.session import engine

app = FastAPI()

app.include_router(user_routes.router)

# При старте приложения создаём таблицы (если их ещё нет)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
