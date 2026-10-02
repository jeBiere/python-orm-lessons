import sqlite3
from pathlib import Path

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id = mapped_column(Integer, primary_key=True)
    # TODO: опиши title (текст) и pages (целое число); оба поля не допускают NULL.


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")


# TODO: удали следующую строку после выполнения задания.
raise NotImplementedError("Допиши модель Book")

connection = sqlite3.connect(database_path)
row = connection.execute("SELECT id, title, pages FROM books WHERE id = 1").fetchone()
connection.close()

book = Book(id=row[0], title=row[1], pages=row[2])
print(book.title, book.pages)
