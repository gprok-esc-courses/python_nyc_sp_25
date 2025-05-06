from tkinter import Tk, Canvas 

window = Tk()
window.title("Drawing Area")
window.geometry("300x300")

canvas = Canvas(window, bg='white', width=290, height=290)
canvas.grid(row=0, column=0)

canvas.create_line(10, 10, 40, 40)
canvas.create_rectangle(50, 10, 90, 50, fill='red')

window.mainloop()