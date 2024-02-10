from multiprocessing import *

def dig(name, hole, lock):
    lock.acquire()
    print("worker: " + name + " hole: " + str(hole))
    lock.release()
def assigndiggers():
    lock = Lock()
    workerNames = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i in range(10):
        Process(target=dig, args=(workerNames[i], i, lock)).start()
assigndiggers()