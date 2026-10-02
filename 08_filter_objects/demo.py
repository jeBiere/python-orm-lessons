from sqlalchemy import Integer, String, create_engine, select
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
    session.add(User(name="Боря"))
    session.add(User(name="Аня"))
    session.commit()

# Главное в этом уроке: SQL-условие описываем через модель.
with Session(engine) as session:
    query = select(User).where(User.name == "Аня").order_by(User.id)
    users = session.scalars(query).all()

    for user in users:
        print(user.id, user.name)
