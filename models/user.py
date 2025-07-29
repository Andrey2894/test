from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Создаём базу для всех моделей
Base = declarative_base()

# Модель таблицы users — аналог @Entity в Spring
class User(Base):
    __tablename__ = 'users'                        # Название таблицы

    id = Column(Integer, primary_key=True, index=True)        # ID с автоинкрементом
    username = Column(String, unique=True, index=True)        # Уникальное имя
    email = Column(String, unique=True, index=True)           # Уникальный email
