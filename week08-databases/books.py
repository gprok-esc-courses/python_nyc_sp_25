import sqlite3

db = sqlite3.connect('books.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    authors TEXT
                )""")

while True:
    print("1. Display all books")
    print("2. Add book")
    print("3. Find book")
    print("4. Change book title")
    print("5. Delete book")
    print("0. EXIT")
    choice = int(input("Select :> "))

    if choice == 0:
        print("Bye!")
        break
    elif choice == 1:
        result = cursor.execute("SELECT * FROM books")
        rows = result.fetchall()
        for row in rows:
            print(row[0], "Title:", row[1])
        print("=================================")
    elif choice == 2:
        title = input("Title: ")
        authors = input("Authors: ")
        cursor.execute("INSERT INTO books (title, authors) VALUES (?, ?)", 
                       (title, authors))
        db.commit()
    elif choice == 3:
        keyword = input("Keyword: ")
        result = cursor.execute("SELECT * FROM books WHERE title LIKE ?", 
                                ('%'+keyword+'%',))
        rows = result.fetchall()
        for row in rows:
            print(row[0], "Title:", row[1])
        print("=================================")
    elif choice == 4:
        id = int(input("ID: "))
        result = cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        book = result.fetchone()
        if book is None:
            print("Book not found")
        else:
            print("Title:", book[1])
            title = input("New title: ")
            cursor.execute("UPDATE books SET title=? WHERE id=?", (title, id))
            db.commit()
    elif choice == 5:
        id = int(input("ID: "))
        result = cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        book = result.fetchone()
        if book is None:
            print("Book not found")
        else:
            print("Title:", book[1])
            confirm = input("Are you sure? Y/N: ")
            if confirm == 'Y':
                cursor.execute("DELETE FROM books WHERE id=?", (id,))
                db.commit()
