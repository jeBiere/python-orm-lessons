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
    user = session.get(User, 2)
    user.name = user.name + "!"
    session.commit()

with Session(engine) as session:
    saved_user = session.get(User, 2)
    print("В базе после сохранения:", saved_user.name)
