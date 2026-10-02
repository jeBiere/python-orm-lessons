from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)


engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    # TODO: создай User с именем «Боря», добавь и сохрани его.
    # id указывать не нужно: его назначит база.
    raise NotImplementedError("Добавь и сохрани пользователя")

with Session(engine) as session:
    user = session.get(User, 1)
    assert isinstance(user, User), "Пользователь должен сохраниться в БД"
    assert user.name == "Боря"
    print(user.id, user.name)
    missing_user = session.get(User, 999)
    assert missing_user is None
    print(missing_user)
    print("Готово!")
