from pathlib import Path

from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
engine = create_engine(f"sqlite:///{database_path}", echo=True)


with Session(engine) as session:
    temporary_user = User(name="Временный читатель")
    session.add(temporary_user)
    session.commit()
    temporary_id = temporary_user.id


with Session(engine) as session:
    user = session.get(User, temporary_id)
    session.delete(user)
    session.commit()

with Session(engine) as session:
    print("После удаления:", session.get(User, temporary_id))
