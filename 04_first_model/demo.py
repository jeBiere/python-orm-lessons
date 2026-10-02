from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


# Главное в этом уроке: класс описывает таблицу и её колонки.
class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)


engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

user = User(id=1, name="Аня")
print(user.id, user.name)
print("Объект создан в Python. Строку в БД мы ещё не добавляли.")
