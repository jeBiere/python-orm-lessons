import sqlite3


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def get_users(connection):
    rows = connection.execute("SELECT id, name FROM users ORDER BY id").fetchall()

    # Главное в этом уроке: превращаем каждую строку в объект.
    users = []
    for row in rows:
        user = User(id=row[0], name=row[1])
        users.append(user)

    return users


connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
connection.execute("INSERT INTO users (name) VALUES (?)", ("Аня",))
connection.execute("INSERT INTO users (name) VALUES (?)", ("Боря",))
connection.commit()

users = get_users(connection)
for user in users:
    print(user.id, user.name)

connection.close()
