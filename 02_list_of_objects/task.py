import sqlite3
from pathlib import Path


class Book:
    def __init__(self, id, title, pages):
        self.id = id
        self.title = title
        self.pages = pages


def pick_books(books, max_pages):
    # TODO: верни объекты с pages <= max_pages в исходном порядке; если их нет — [].
    raise NotImplementedError("Допиши pick_books")


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
connection = sqlite3.connect(database_path)

books = []
for row in connection.execute(
    "SELECT id, title, pages FROM books WHERE pages > 0 ORDER BY id"
).fetchall():
    books.append(Book(id=row[0], title=row[1], pages=row[2]))
connection.close()

selected = pick_books(books, 120)
assert selected, "В учебной базе есть книги не длиннее 120 страниц"
for book in selected:
    assert book in books and book.pages <= 120
    print(book.title)
assert pick_books([], 120) == []
