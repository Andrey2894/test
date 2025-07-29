from pydantic import BaseModel

# DTO для создания пользователя (входной формат)
class UserCreate(BaseModel):
    username: str
    email: str

# DTO для ответа клиенту (выходной формат)
class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True  # Позволяет автоматически маппить SQLAlchemy-объекты на Pydantic-модель
