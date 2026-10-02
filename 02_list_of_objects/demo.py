import sqlite3
from pathlib import Path


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def get_users(connection):
    rows = connection.execute("SELECT id, name FROM users ORDER BY id").fetchall()


    users = []
    for row in rows:
        user = User(id=row[0], name=row[1])
        users.append(user)

    return users


database_path = Path(__file__).resolve().parent.parent / "library.db"
if not database_path.is_file():
    raise SystemExit("Сначала запусти: python 00_create_database/setup.py")
connection = sqlite3.connect(database_path)

users = get_users(connection)
for user in users:
    print(user.id, user.name)

connection.close()
