import sqlite3


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


connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
connection.execute("INSERT INTO users (name) VALUES (?)", ("Аня",))
connection.commit()

# Главное в этом уроке: изменение объекта и сохранение — два шага.
user = get_user_by_id(connection, 1)
user.name = "Анна"
print("В объекте:", user.name)
print("В базе до сохранения:", get_user_by_id(connection, 1).name)

save_user(connection, user)
print("В базе после сохранения:", get_user_by_id(connection, 1).name)
connection.close()
