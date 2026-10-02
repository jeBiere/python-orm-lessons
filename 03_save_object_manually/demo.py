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


def save_user(connection, user):
    connection.execute(
        "UPDATE users SET name = ? WHERE id = ?", (user.name, user.id)
    )
    connection.commit()


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
connection = sqlite3.connect(database_path)


user = get_user_by_id(connection, 1)
user.name = user.name + "!"
print("В объекте:", user.name)
print("В базе до сохранения:", get_user_by_id(connection, 1).name)

save_user(connection, user)
print("В базе после сохранения:", get_user_by_id(connection, 1).name)
connection.close()
