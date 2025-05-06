from tkinter import Tk, Entry, Button, Label 

def button_clicked():
    name = name_field.get()
    print(name)
    message = "Welcome " + name
    message_label.configure(text=message)

window = Tk()
window.title("Welcome")
window.geometry("300x300")

name_field = Entry(window)
name_field.grid(row=0, column=0)

go_button = Button(window, text="GO", command=button_clicked)
go_button.grid(row=1, column=0)

message_label = Label(window, text="Welcome Stranger")
message_label.grid(row=2, column=0)

window.mainloop()