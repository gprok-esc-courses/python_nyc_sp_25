from time import time, sleep
import random


def counter(name):
    for i in range(1, 6):
        print(name + " " + str(i))
        sleep(random.randint(2, 5))


    
names = ["A", "B", "C" , "D"]    
start = time()
for name in names:
    counter(name)
end = time()

print("Time elapsed: ", end-start)