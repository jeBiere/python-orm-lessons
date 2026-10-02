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


def swap_titles(session, first_id, second_id):
    # TODO: обменяй только названия, сохрани и верни True.
    # TODO: если любой книги нет, ничего не меняй и верни False.
    raise NotImplementedError("Допиши swap_titles")


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
engine = create_engine(f"sqlite:///{database_path}", echo=True)

with Session(engine) as session:
    first = session.get(Book, 1)
    second = session.get(Book, 2)
    first_title, first_pages = first.title, first.pages
    second_title, second_pages = second.title, second.pages
    swapped = swap_titles(session, 1, 2)
    assert swapped is True
    failed_swap = swap_titles(session, 1, 999)
    assert failed_swap is False

with Session(engine) as session:
    first = session.get(Book, 1)
    second = session.get(Book, 2)
    assert first.title == second_title and first.pages == first_pages
    assert second.title == first_title and second.pages == second_pages
    print(first.id, first.title, first.pages)
    print(second.id, second.title, second.pages)
