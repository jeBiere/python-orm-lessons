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
    session.add(User(name="Аня"))
    session.commit()

# Главное в этом уроке: загруженный объект можно удалить.
with Session(engine) as session:
    user = session.get(User, 1)
    session.delete(user)
    session.commit()

with Session(engine) as session:
    print("После удаления:", session.get(User, 1))
