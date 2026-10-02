import sqlite3


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def get_users_by_name(connection, name):
    # TODO: получи все строки с нужным именем в порядке id.
    # Преврати их в список объектов User и верни этот список.
    raise NotImplementedError("Допиши get_users_by_name")


connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
connection.execute("INSERT INTO users (name) VALUES (?)", ("Аня",))
connection.execute("INSERT INTO users (name) VALUES (?)", ("Боря",))
connection.execute("INSERT INTO users (name) VALUES (?)", ("Аня",))
connection.commit()

users = get_users_by_name(connection, "Аня")
assert isinstance(users, list), "Нужен список объектов"
assert len(users) == 2, "В базе две Ани"
assert users[0].id == 1 and users[0].name == "Аня"
assert users[1].id == 3 and users[1].name == "Аня"
for user in users:
    assert isinstance(user, User), "Элемент списка должен быть объектом User"
    print(user.id, user.name)

missing_users = get_users_by_name(connection, "Нина")
assert missing_users == [], "Нет совпадений — пустой список"
print(missing_users)
print("Готово!")
connection.close()
