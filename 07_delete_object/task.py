from pathlib import Path

from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    pages = mapped_column(Integer, nullable=False)


def delete_drafts(session, books):
    # TODO: удали переданные книги с pages == 0, сохрани и верни число удалённых.
    raise NotImplementedError("Допиши delete_drafts")


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
engine = create_engine(f"sqlite:///{database_path}", echo=True)

with Session(engine) as session:
    books = []
    draft_ids = []
    for book_id in (1, 13, 14, 15):
        book = session.get(Book, book_id)
        if book is not None:
            books.append(book)
            if book.pages == 0:
                draft_ids.append(book.id)
    removed = delete_drafts(session, books)
    assert removed == len(draft_ids)
    print("Удалено черновиков:", removed)
    assert delete_drafts(session, []) == 0

with Session(engine) as session:
    for book_id in draft_ids:
        assert session.get(Book, book_id) is None
    remaining = session.get(Book, 1)
    assert remaining is not None and remaining.pages > 0
    print("Осталась книга:", remaining.title)
