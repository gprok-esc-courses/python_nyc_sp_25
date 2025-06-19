from time import time, sleep
import random
from threading import Thread 


def counter(name):
    for i in range(1, 6):
        print(name + " " + str(i))
        sleep(random.randint(2, 5))


    
names = ["A", "B", "C" , "D"]    
start = time()
threads = []
for name in names:
    th = Thread(target=counter, args=name)
    threads.append(th)
    th.start()
for th in threads:
    th.join()
end = time()

print("Time elapsed: ", end-start)