from fastapi import FastAPI
from api import user_routes
from models.user import Base
from db.session import engine
import uvicorn

app = FastAPI()

app.include_router(user_routes.router)

# Простой корневой endpoint
@app.get("/")
async def read_root():
    return {"status": "ok"}

# При старте приложения создаём таблицы (если их ещё нет)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
