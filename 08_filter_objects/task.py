from pathlib import Path

from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    pages = mapped_column(Integer, nullable=False)


def find_books_for_weekend(session, max_pages):
    # TODO: через ORM получи книги с 0 < pages <= max_pages по возрастанию pages.
    # TODO: верни список Book; если совпадений нет — [].
    raise NotImplementedError("Допиши find_books_for_weekend")


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
engine = create_engine(f"sqlite:///{database_path}", echo=True)

with Session(engine) as session:
    books = find_books_for_weekend(session, 120)
    assert books, "В учебной базе есть подходящие книги"
    previous_pages = 0
    for book in books:
        assert 0 < book.pages <= 120, "Нужна готовая книга не длиннее 120 страниц"
        assert book.pages >= previous_pages, "Сначала самая короткая книга"
        print(book.title, book.pages)
        previous_pages = book.pages
    assert find_books_for_weekend(session, 0) == [], "Черновик не подходит читателю"
