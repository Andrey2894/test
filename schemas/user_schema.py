from pydantic import BaseModel

class UserCreate(BaseModel):
    """DTO для создания пользователя"""
    username: str
    email: str

class UserOut(BaseModel):
    """DTO пользователя в ответе"""
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True  # Позволяет маппить SQLAlchemy -> Pydantic
