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


# Знакомая подготовка: таблица и одна строка.
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
connection.execute("INSERT INTO users (name) VALUES (?)", ("Аня",))
connection.commit()

# Главное в этом уроке: одни данные, два способа представления.
row = connection.execute("SELECT id, name FROM users WHERE id = 1").fetchone()
print("Кортеж:", row)
print("Имя через индекс:", row[1])

user = get_user_by_id(connection, 1)
print("Объект:", type(user).__name__)
print("Имя через атрибут:", user.name)
print("Несуществующий пользователь:", get_user_by_id(connection, 999))

connection.close()
