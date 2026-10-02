from pathlib import Path

from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
engine = create_engine(f"sqlite:///{database_path}", echo=True)


with Session(engine) as session:
    user = User(name="Новый читатель")
    print("id до сохранения:", user.id)
    session.add(user)
    session.commit()
    new_user_id = user.id
    print("id после сохранения:", new_user_id)

with Session(engine) as session:
    saved_user = session.get(User, new_user_id)
    print("Получили из БД:", saved_user.id, saved_user.name)
    print("Несуществующий пользователь:", session.get(User, 999))
