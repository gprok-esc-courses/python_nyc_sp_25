from tkinter import Tk, Button

def button_event(value):
    print("Button " + str(value) + " is clicked.")

window = Tk() 

b1 = Button(window, text="B 1", command=lambda: button_event(1))
b1.grid(row=0, column=0)

b2 = Button(window, text="B 2", command=lambda: button_event(2))
b2.grid(row=0, column=1)

b3 = Button(window, text="B 3", command=lambda: button_event(3))
b3.grid(row=0, column=2)

window.mainloop()