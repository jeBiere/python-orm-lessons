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


def get_all_books(session):
    # TODO 1: получи все книги по возрастанию id и верни список Book.
    pass


def get_book_by_id(session, book_id):
    # TODO 2, 3, 6: получи книгу по book_id.
    # Верни Book или None, если такой книги нет.
    pass


def find_books_by_pages(session, min_pages, max_pages):
    # TODO 4: получи книги с числом страниц от min_pages до max_pages включительно.
    # Верни список Book по возрастанию числа страниц; если совпадений нет — [].
    pass


def create_book(session, title, pages):
    # TODO 5: создай книгу с переданными названием и числом страниц.
    # Сохрани её в БД и верни выданный id.
    pass


def update_book(session, book_id, new_title, new_pages):
    # TODO 7: получи книгу по book_id и измени её название и число страниц.
    # Сохрани изменения и верни Book; если книги нет — верни None.
    pass


def delete_book(session, book_id):
    # TODO 8: получи книгу по book_id, удали её и сохрани изменение в БД.
    # Если книги нет, ничего не делай. Возвращать результат не нужно.
    pass


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
engine = create_engine(f"sqlite:///{database_path}", echo=True)


# Практика: каталог библиотеки.
# Заполни тела функций выше через SQLAlchemy ORM, без SQL-строк и sqlite3.
# Вместо pass в функциях напиши своё решение.
# Фильтрацию и сортировку задавай в запросах, а не в Python после получения книг.
# Код ниже уже вызывает функции и выводит результаты заданий по порядку.
# Запуск из корня проекта: python 09_orm_practice/task.py

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
