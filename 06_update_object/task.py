from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)


def rename_user(session, user_id, new_name):
    # TODO: получи объект, измени имя и сохрани изменение.
    # Верни True при успехе или False, если пользователя нет.
    raise NotImplementedError("Допиши rename_user")


engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(User(name="Аня"))
    session.commit()

with Session(engine) as session:
    renamed = rename_user(session, 1, "Анна")
    assert renamed is True
    missing_user_renamed = rename_user(session, 999, "Нина")
    assert missing_user_renamed is False

with Session(engine) as session:
    user = session.get(User, 1)
    assert user.name == "Анна", "Новое имя должно сохраниться в БД"
    print(user.name)
    print("Готово!")
