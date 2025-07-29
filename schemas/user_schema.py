from pydantic import BaseModel, ConfigDict

# Схема входящих данных — тут ничего не меняется, валидация по полям
class UserCreate(BaseModel):
    username: str
    email: str

# Схема исходящих данных: указываем, что модель может заполняться из атрибутов ORM-объекта
class UserOut(BaseModel):
    id: int
    username: str
    email: str

    # Вместо deprecated orm_mode ставим from_attributes
    model_config = ConfigDict(from_attributes=True)
