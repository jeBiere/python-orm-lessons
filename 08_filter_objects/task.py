from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)


def get_users_by_name(session, name):
    # TODO: опиши запрос с условием по имени и сортировкой по id.
    # Выполни его через session и верни список объектов User.
    raise NotImplementedError("Допиши get_users_by_name")


engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(User(name="Аня"))
    session.add(User(name="Боря"))
    session.add(User(name="Аня"))
    session.commit()

with Session(engine) as session:
    users = get_users_by_name(session, "Аня")
    assert isinstance(users, list), "Нужен список объектов"
    assert len(users) == 2, "В базе две Ани"
    assert users[0].id == 1 and users[0].name == "Аня"
    assert users[1].id == 3 and users[1].name == "Аня"
    for user in users:
        assert isinstance(user, User), "Элемент списка должен быть объектом User"
        print(user.id, user.name)

    missing_users = get_users_by_name(session, "Нина")
    assert missing_users == [], "Нет совпадений — пустой список"
    print(missing_users)
    print("Готово!")
