import sqlite3
from pathlib import Path


database_path = Path(__file__).resolve().parent.parent / "library.db"
if database_path.exists():
    print("База уже существует, данные сохранены:", database_path)
    raise SystemExit

connection = sqlite3.connect(database_path)
connection.execute("PRAGMA foreign_keys = ON")

connection.executescript("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        pages INTEGER NOT NULL CHECK (pages >= 0),
        author_id INTEGER REFERENCES authors(id)
    );

    CREATE TABLE loans (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES users(id),
        book_id INTEGER NOT NULL REFERENCES books(id),
        borrowed_at TEXT NOT NULL,
        returned_at TEXT
    );
""")


connection.executemany("INSERT INTO users (id, name) VALUES (?, ?)", [
    (1, "Аня"),
    (2, "Боря"),
    (3, "Аня"),
    (4, "Вера"),
    (5, "Глеб"),
    (6, "Даша"),
    (7, "Егор"),
    (8, "Женя"),
    (9, "Зоя"),
    (10, "Илья"),
    (11, "Катя"),
    (12, "Лена"),
])

connection.executemany("INSERT INTO authors (id, name) VALUES (?, ?)", [
    (1, "Мария Лесная"),
    (2, "Иван Учёный"),
    (3, "Анна Рассказова"),
    (4, "Павел Морской"),
    (5, "Ольга Северная"),
    (6, "Денис Звёздный"),
    (7, "Елена Садовая"),
    (8, "Михаил Горный"),
    (9, "Софья Городская"),
    (10, "Алексей Речной"),
    (11, "Нина Луговая"),
    (12, "Виктор Полевой"),
])


connection.executemany(
    "INSERT INTO books (id, title, pages, author_id) VALUES (?, ?, ?, ?)",
    [
        (1, "Учебник", 80, 1),
        (2, "Лесные истории", 300, 2),
        (3, "Рассказы", 120, 3),
        (4, "Морское путешествие", 40, 4),
        (5, "Северный ветер", 180, 5),
        (6, "Карта звёзд", 240, 6),
        (7, "Садовые сказки", 60, 7),
        (8, "Горная тропа", 100, 8),
        (9, "Городские тайны", 200, 9),
        (10, "Вдоль реки", 160, 10),
        (11, "Луговые заметки", 120, 11),
        (12, "Полевой дневник", 150, 12),
        (13, "План рассказа", 0, None),
        (14, "Идея романа", 0, None),
        (15, "Набросок сказки", 0, None),
    ],
)

connection.executemany(
    "INSERT INTO loans (id, user_id, book_id, borrowed_at, returned_at) VALUES (?, ?, ?, ?, ?)",
    [
        (1, 1, 1, "2026-09-01", "2026-09-05"),
        (2, 2, 2, "2026-09-02", None),
        (3, 3, 3, "2026-09-03", "2026-09-08"),
        (4, 4, 4, "2026-09-04", None),
        (5, 5, 5, "2026-09-05", "2026-09-10"),
        (6, 6, 6, "2026-09-06", None),
        (7, 7, 7, "2026-09-07", "2026-09-12"),
        (8, 8, 8, "2026-09-08", None),
        (9, 9, 9, "2026-09-09", "2026-09-14"),
        (10, 10, 10, "2026-09-10", None),
        (11, 11, 11, "2026-09-11", "2026-09-16"),
        (12, 12, 12, "2026-09-12", None),
    ],
)
connection.commit()

print("База создана:", database_path)
for table in ("users", "authors", "books", "loans"):
    count = connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"{table}: {count} строк")
connection.close()
