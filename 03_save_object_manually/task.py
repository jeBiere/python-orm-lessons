import sqlite3
from pathlib import Path


class Book:
    def __init__(self, id, title, pages):
        self.id = id
        self.title = title
        self.pages = pages


def get_book_by_id(connection, book_id):
    row = connection.execute(
        "SELECT id, title, pages FROM books WHERE id = ?", (book_id,)
    ).fetchone()
    if row is None:
        return None
    return Book(id=row[0], title=row[1], pages=row[2])


def add_pages(connection, book_id, extra_pages):
    book = get_book_by_id(connection, book_id)
    book.pages += extra_pages
    # TODO: сохрани изменённое pages в существующей строке по book.id.
    connection.commit()


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
connection = sqlite3.connect(database_path)

pages_before = get_book_by_id(connection, 1).pages
other_pages_before = get_book_by_id(connection, 2).pages
print("До исправления:", pages_before)
add_pages(connection, 1, 20)
saved_book = get_book_by_id(connection, 1)
print("После повторного чтения:", saved_book.pages)
assert saved_book.pages == pages_before + 20, "Исправление должно сохраниться в БД"
assert get_book_by_id(connection, 2).pages == other_pages_before, "Другая книга не менялась"
connection.close()
