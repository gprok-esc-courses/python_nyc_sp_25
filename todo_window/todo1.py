from tkinter import Tk, ttk, StringVar, END, DISABLED, NORMAL, RIGHT, Y
import sqlite3 

class DBConnection:
    def __init__(self):
        self.db = sqlite3.connect('todo.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            task TEXT, 
                            project TEXT,
                            completed INTEGER
                        )
                       """)
        self.db.commit()

    def get_connection(self):
        return self.db
    

class TodoListApp:
    def __init__(self, window):
        self.window = window
        self.conn = DBConnection()
        self.db = self.conn.get_connection()
        self.cursor = self.db.cursor()

        # Frame for the task form
        self.form_frame = ttk.LabelFrame(window, text="Task Data")
        self.form_frame.pack(fill='x')

        task_label = ttk.Label(self.form_frame, text="Task: ").grid(row=0, column=0)
        project_label = ttk.Label(self.form_frame, text="Project: ").grid(row=1, column=0)
        self.task_value = StringVar()
        task_field = ttk.Entry(self.form_frame, textvariable=self.task_value, width=30).grid(row=0, column=1)
        self.project_value = StringVar()
        proj_field = ttk.Entry(self.form_frame, textvariable=self.project_value, width=30).grid(row=1, column=1)

        # Frame for the buttons
        self.button_frame = ttk.Frame(window)
        self.button_frame.pack(fill='x')

        self.add_btn = ttk.Button(self.button_frame, text="Add New", command=self.add_new).grid(row=0, column=0)
        self.save_btn = ttk.Button(self.button_frame, text="Save", command=self.add_new_task).grid(row=0, column=1)
        self.upd_btn = ttk.Button(self.button_frame, text="Update", command=self.update_task).grid(row=0, column=2)
        self.complete_btn = ttk.Button(self.button_frame, text="Complete", command=self.complete_task).grid(row=0, column=3)

        # Frame for the tasks list
        self.tasks_frame = ttk.Frame(window)
        self.tasks_frame.pack(fill="both", expand=True)

        self.scroll = ttk.Scrollbar(self.tasks_frame)
        self.scroll.pack(side=RIGHT, fill=Y) 

        self.list = ttk.Treeview(self.tasks_frame, columns=("ID", "Task", "Project"), show="headings",
                                 yscrollcommand=self.scroll.set)
        self.list.heading("ID", text="ID")
        self.list.heading("Task", text="Task")
        self.list.heading("Project", text="Project")
        self.list.column("ID", width=30)
        self.list.column("Task", width=200)
        self.list.column("Project", width=150)

        self.list.pack(fill="both", expand=True)
        self.scroll.config(command=self.list.yview)

        self.list.bind("<<TreeviewSelect>>", self.list_item_selected)

        self.load_tasks()

    def clear_fields(self):
        self.task_value.set('')
        self.project_value.set('')

    def add_new(self):
        self.clear_fields()

    def add_new_task(self):
        task = self.task_value.get()
        project = self.project_value.get() 
        print(task, project)
        if len(task) == 0 or len(project) == 0:
            print("Task and/or Project empty")
            return
        self.cursor.execute("INSERT INTO tasks (task, project, completed) VALUES (?, ?, 0)",
                            (task, project))
        self.db.commit()
        self.clear_fields()
        self.load_tasks()

    def update_task(self):
        selection = self.list.selection()
        item = self.list.item(selection[0], "values")
        id = item[0]
        task = self.task_value.get()
        project = self.project_value.get()
        if len(task) == 0 or len(project) == 0:
            print("Task and/or Project empty")
            return
        self.cursor.execute("UPDATE tasks SET task=?, project=? WHERE id=?", (task, project, id))
        self.db.commit()
        self.clear_fields()
        self.load_tasks()

    def complete_task(self):
        selection = self.list.selection()
        item = self.list.item(selection[0], "values")
        id = item[0]
        self.cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (id,))
        self.db.commit()
        self.clear_fields()
        self.load_tasks()

    def load_tasks(self):
        for item in self.list.get_children():
            self.list.delete(item)
        self.cursor.execute("SELECT id, task, project FROM tasks WHERE completed=0")
        tasks = self.cursor.fetchall()
        for task in tasks:
            self.list.insert("", END, values=task)

    def list_item_selected(self, event):
        selection = self.list.selection()
        item = self.list.item(selection[0], "values")
        print(item)
        self.clear_fields()
        self.task_value.set(item[1])
        self.project_value.set(item[2])


        


root = Tk()
root.title("TODO LIST")
root.geometry("700x500")
app = TodoListApp(root)
root.mainloop()