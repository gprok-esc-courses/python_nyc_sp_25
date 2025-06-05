import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def get_db_conn():
    db = sqlite3.connect('expenses.db')
    return db

def display_menu():
    print("==== EXPENSES MENU =====")
    print("1. Add Category")
    print("2. View Categories")
    print("3. Add expense")
    print("4. Expense by category")
    print("5. Totals")
    print("6. Totals Graph")
    print("0. EXIT")

def display_bar_chart(totals):
    categories = []
    values = []
    for row in totals:
        categories.append(row[0])
        values.append(row[1])
    x = np.array(categories)
    y = np.array(values)
    plt.bar(x, y)
    plt.show()

class Category:
    def __init__(self, id, name):
        self.id  = id
        self.name = name 

    def __str__(self):
        return str(self.id) + ". " + self.name 
    
class Expense:
    def __init__(self, id, descr, category_id, amount):
        self.db = get_db_conn()
        category_repo = CategoryRepository()
        self.id = id 
        self.descr = descr 
        self.category = category_repo.get_by_id(category_id)
        self.amount = amount

    def __str__(self):
        return str(self.id) + ". " + self.category.name + ", " + str(self.amount) + \
                ", " + self.descr
    
class CategoryRepository:
    def __init__(self):
        self.db = get_db_conn()

    def save(self, category_name):
        self.db.execute('INSERT INTO categories (name) VALUES (?)', (category_name,))
        self.db.commit()

    def get_by_id(self, id):
        result = self.db.execute("SELECT * FROM categories WHERE id=?", (id,)).fetchone()
        category = Category(result[0], result[1])
        return category
    
    def get_all(self):
        result = self.db.execute("SELECT * FROM categories").fetchall()
        categories = []
        for row in result:
            cat = Category(row[0], row[1])
            categories.append(cat)
        return categories
    
class ExpenseRepository:
    def __init__(self):
        self.db = get_db_conn()

    def save(self, category_id, descr, amount):
        self.db.execute("INSERT INTO expenses (description, category_id, amount) VALUES (?,?,?)",
                        (descr, category_id, amount))
        self.db.commit()

    def get_by_category(self, category_id):
        result = self.db.execute("SELECT * FROM expenses WHERE category_id=?", (category_id,)).fetchall()
        expenses = []
        for row in result:
            ex = Expense(row[0], row[1], row[2], row[3])
            expenses.append(ex)
        return expenses
    
    def get_totals(self):
        query = """
                SELECT c.name as category, SUM(e.amount) as total
                FROM expenses e
                INNER JOIN categories c ON c.id=e.category_id
                GROUP BY c.name
                ORDER BY total DESC
                """
        result = self.db.execute(query).fetchall()
        totals = []
        for row in result:
            totals.append([row[0], row[1]])
        return totals
    

if __name__ == "__main__":
    category_repo = CategoryRepository()
    expense_repo = ExpenseRepository()

    choice = -1
    while choice != 0:
        display_menu()
        choice = int(input("Choose: "))
        match choice:
            case 1:
                name = input("Category Name: ")
                category_repo.save(name)
            case 2:
                categories = category_repo.get_all()
                for cat in categories:
                    print(cat.id, cat.name)
            case 3:
                descr = input("Description: ")
                amount = input("Amount: ")
                cat_id = int(input("Category ID: "))
                expense_repo.save(cat_id, descr, amount)
            case 4:
                cat_id = int(input("Category ID: "))
                expenses = expense_repo.get_by_category(cat_id)
                for e in expenses:
                    print(e)
            case 5:
                totals = expense_repo.get_totals()
                for row in totals:
                    print(row[0], ": ", row[1])
            case 6:
                totals = expense_repo.get_totals()
                display_bar_chart(totals)
            case 0:
                print("Bye!")
            case _:
                print("Wrong choice")