from multiprocessing import *
import random
import time

def addManyNumbers(numNumbers, q):
    s = 0
    for i in range(numNumbers):
        s = s + random.randint(1, 100)
    q.put(s)

def addManyPairs():
    totalNumbers = 100000

    q = Queue()
    p1 = Process(target=addManyNumbers, args=(totalNumbers//2, q))
    p2 = Process(target=addManyNumbers, args=(totalNumbers//2, q))
    p1.start()
    p2.start()

    a = q.get()
    b = q.get()
    print(f"sum: " + str(a + b))

def runner():
    for i in range(100):
        Process(target=addManyPairs).start()
runner()