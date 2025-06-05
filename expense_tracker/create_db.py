import sqlite3

db = sqlite3.connect("expenses.db")

db.execute("DROP TABLE IF EXISTS expenses")

db.execute("DROP TABLE IF EXISTS categories")

db.execute("""
            CREATE TABLE categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
           """)

db.execute("""
            CREATE TABLE expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                category_id INTEGER,
                amount REAL,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
           """)
