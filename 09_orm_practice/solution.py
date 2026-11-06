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


def get_all_books(session):
    return session.query(Book).order_by(Book.id).all()


def get_book_by_id(session, book_id):
    return session.get(Book, book_id)


def find_books_by_pages(session, min_pages, max_pages):
    return (
        session.query(Book)
        .filter(Book.pages >= min_pages, Book.pages <= max_pages)
        .order_by(Book.pages)
        .all()
    )


def create_book(session, title, pages):
    book = Book(title=title, pages=pages)
    session.add(book)
    session.commit()
    return book.id


def update_book(session, book_id, new_title, new_pages):
    book = session.get(Book, book_id)
    if book is None:
        return None

    book.title = new_title
    book.pages = new_pages
    session.commit()
    return book


def delete_book(session, book_id):
    book = session.get(Book, book_id)
    if book is None:
        return

    session.delete(book)
    session.commit()


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
engine = create_engine(f"sqlite:///{database_path}", echo=True)


# Практика: каталог библиотеки. Решение для преподавателя.
# Для заданий 1 и 4 используется session.query(Book): запрос объектов Book.
# filter задаёт условия, order_by — сортировку, all возвращает список объектов.
# Это другой способ выборки; если его ещё не проходили, сначала разбери его.
# Запуск из корня проекта: python 09_orm_practice/solution.py

if __name__ == "__main__":
    with Session(engine) as session:
        print("1. Все книги")
        for book in get_all_books(session):
            print(book.id, book.title, book.pages)

        print("2. Книга с id=1")
        book = get_book_by_id(session, 1)
        if book is None:
            print("Книга не найдена")
        else:
            print(book.title, book.pages)

        print("3. Книга с id=999")
        book = get_book_by_id(session, 999)
        if book is None:
            print("Книга не найдена")
        else:
            print(book.title, book.pages)

        print("4. Книги от 100 до 200 страниц")
        for book in find_books_by_pages(session, 100, 200):
            print(book.title, book.pages)

        print("5. Создание книги")
        new_book_id = create_book(session, "Заметки читателя", 150)
        print("id новой книги:", new_book_id)

        # Дальше изменяем и удаляем только созданную книгу.
        print("6. Чтение созданной книги")
        book = get_book_by_id(session, new_book_id)
        if book is not None:
            print(book.title, book.pages)

        print("7. Изменение книги")
        update_book(session, new_book_id, "Заметки читателя. Дополненное издание", 180)
        book = get_book_by_id(session, new_book_id)
        if book is not None:
            print(book.title, book.pages)

        print("8. Удаление книги")
        delete_book(session, new_book_id)
        print("После удаления (ожидается None):", get_book_by_id(session, new_book_id))
