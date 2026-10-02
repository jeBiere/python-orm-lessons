from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)


def delete_user(session, user_id):
    # TODO: получи объект, удали его и сохрани изменение.
    # Верни True при успехе или False, если пользователя нет.
    raise NotImplementedError("Допиши delete_user")


engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(User(name="Аня"))
    session.add(User(name="Боря"))
    session.commit()

with Session(engine) as session:
    deleted = delete_user(session, 1)
    assert deleted is True
    missing_user_deleted = delete_user(session, 999)
    assert missing_user_deleted is False

with Session(engine) as session:
    deleted_user = session.get(User, 1)
    assert deleted_user is None, "Удалённого пользователя больше нет"
    remaining_user = session.get(User, 2)
    assert remaining_user is not None, "Второй пользователь должен остаться"
    assert remaining_user.name == "Боря"
    print(deleted_user)
    print(remaining_user.name)
    print("Готово!")
