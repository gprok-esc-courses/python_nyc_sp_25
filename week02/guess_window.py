from tkinter import Tk, Button, Entry, Label 
import random 

secret = random.randint(1, 100)
counter = 0

def check_guess():
    global secret
    global counter
    counter = counter + 1
    guess = int(guess_entry.get())
    if guess > secret:
        msg_label.configure(text="DOWN")
    elif guess < secret:
        msg_label.configure(text="UP")
    else: 
        message = "FOUND " + str(counter) + " guesses"
        msg_label.configure(text=message)

window = Tk()
window.title("GUESS GAME")
window.geometry("350x250")

guess_label = Label(window, text="Guess:")
guess_label.grid(row=0, column=0)
guess_entry = Entry(window)
guess_entry.grid(row=0, column=1)
check_btn = Button(window, text="Check", command=check_guess)
check_btn.grid(row=0, column=2)

msg_label = Label(window, text="-")
msg_label.grid(row=1, column=0, columnspan=3)

window.mainloop()