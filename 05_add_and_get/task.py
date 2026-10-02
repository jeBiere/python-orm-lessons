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


def copy_book(session, book_id, new_title):
    # TODO: скопируй число страниц в новую книгу с new_title, сохрани и верни её id.
    # TODO: исходную книгу не меняй; если её нет, верни None.
    raise NotImplementedError("Допиши copy_book")


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
engine = create_engine(f"sqlite:///{database_path}", echo=True)

with Session(engine) as session:
    original = session.get(Book, 1)
    original_title = original.title
    original_pages = original.pages
    new_title = original_title + ". Новое издание"
    new_id = copy_book(session, 1, new_title)
    assert new_id is not None and new_id != 1, "Новому изданию нужна отдельная строка"
    missing_copy = copy_book(session, 999, "Несуществующая книга")
    assert missing_copy is None

with Session(engine) as session:
    original = session.get(Book, 1)
    copied = session.get(Book, new_id)
    assert original.title == original_title and original.pages == original_pages
    assert copied is not None, "Новое издание должно сохраниться в БД"
    assert copied.title == new_title and copied.pages == original_pages
    print(original.id, original.title)
    print(copied.id, copied.title)
