import sqlite3


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def get_user_by_name(connection, name):
    # TODO: SELECT с условием по имени, затем строка -> User.
    # Если строки нет, верни None. Используй параметр ?, как раньше.
    raise NotImplementedError("Допиши get_user_by_name")


connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
connection.execute("INSERT INTO users (name) VALUES (?)", ("Аня",))
connection.execute("INSERT INTO users (name) VALUES (?)", ("Боря",))
connection.commit()

user = get_user_by_name(connection, "Боря")
assert isinstance(user, User), "Функция должна вернуть объект User"
assert user.id == 2 and user.name == "Боря"
print(user.id, user.name)

missing_user = get_user_by_name(connection, "Нина")
assert missing_user is None, "Если строки нет, нужно вернуть None"
print(missing_user)
print("Готово!")
connection.close()
