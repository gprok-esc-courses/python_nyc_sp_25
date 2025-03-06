import random
from my_library import read_integer

secret = random.randint(1, 100) 

counter = 0 

guess = 0

while guess != secret:
    guess = read_integer("Guess: ")
    counter = counter + 1
    if guess > secret:
        print("DOWN")
    elif guess < secret:
        print("UP")
    else: 
        print("FOUND")
        print("in", counter, "guesses")