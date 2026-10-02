import sqlite3
from pathlib import Path


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def get_user_by_id(connection, user_id):
    row = connection.execute(
        "SELECT id, name FROM users WHERE id = ?", (user_id,)
    ).fetchone()

    if row is None:
        return None

    return User(id=row[0], name=row[1])


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
connection = sqlite3.connect(database_path)


row = connection.execute("SELECT id, name FROM users WHERE id = 1").fetchone()
print("Кортеж:", row)
print("Имя через индекс:", row[1])

user = get_user_by_id(connection, 1)
print("Имя через атрибут:", user.name)
print("Несуществующий пользователь:", get_user_by_id(connection, 999))

connection.close()
