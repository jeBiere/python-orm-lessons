import sqlite3
from pathlib import Path

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
connection = sqlite3.connect(database_path)
row = connection.execute("SELECT id, name FROM users WHERE id = 1").fetchone()
connection.close()

user = User(id=row[0], name=row[1])
print(user.id, user.name)
print("Модель соответствует таблице:", User.__tablename__)
