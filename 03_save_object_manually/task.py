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
    # TODO: обнови существующую строку по user.id и вызови commit().
    raise NotImplementedError("Допиши save_user")


connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
connection.execute("INSERT INTO users (name) VALUES (?)", ("Аня",))
connection.execute("INSERT INTO users (name) VALUES (?)", ("Боря",))
connection.commit()

user = get_user_by_id(connection, 1)
user.name = "Анна"
print("В объекте:", user.name)
print("В базе до сохранения:", get_user_by_id(connection, 1).name)

save_user(connection, user)
saved_user = get_user_by_id(connection, 1)
assert saved_user.name == "Анна", "Перечитай строку: имя должно сохраниться"
assert get_user_by_id(connection, 2).name == "Боря", "Измениться должна только Аня"
print("В базе после сохранения:", saved_user.name)
print("Готово!")
connection.close()
