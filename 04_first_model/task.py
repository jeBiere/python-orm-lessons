from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id = mapped_column(Integer, primary_key=True)
    # TODO: добавь колонку title — текст, который не может быть NULL.


# Удали эту строку после добавления колонки.
raise NotImplementedError("Добавь колонку title в модель Book")

engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

book = Book(id=1, title="Путешествие к центру Земли")
print(book.id, book.title)
print("Готово!")
