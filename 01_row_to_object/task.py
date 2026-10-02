import sqlite3
from pathlib import Path


class Book:
    # TODO: создай конструктор Book с атрибутами id, title и pages.
    pass


def get_book_by_id(connection, book_id):
    row = connection.execute(
        "SELECT title, pages, id FROM books WHERE id = ?", (book_id,)
    ).fetchone()
    return row  # TODO: верни Book из строки (title, pages, id) или None, если строки нет.


def book_card(book):
    return f"«{book.title}» — {book.pages} стр."


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
connection = sqlite3.connect(database_path)

book = get_book_by_id(connection, 1)
assert isinstance(book, Book), "Карточке нужен объект Book, а не кортеж"
assert book.id == 1
assert isinstance(book.title, str) and isinstance(book.pages, int)
print(book_card(book))
assert get_book_by_id(connection, 999) is None
connection.close()
