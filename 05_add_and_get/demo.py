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

# Главное в этом уроке: объект -> строка в БД -> объект.
with Session(engine) as session:
    user = User(name="Аня")
    print("id до сохранения:", user.id)
    session.add(user)
    session.commit()
    print("id после сохранения:", user.id)

with Session(engine) as session:
    saved_user = session.get(User, 1)
    print("Получили из БД:", saved_user.id, saved_user.name)
    print("Несуществующий пользователь:", session.get(User, 999))
