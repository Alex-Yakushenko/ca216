import time
from multiprocessing import *

def greet2(q):
    for i in range(5):
        print("waiting")
        name = q.get()
        print(f"Hello {name}")
def sendName2():
    q = Queue()
    Process(target=greet2, args=(q,)).start()
    for i in range(5):
        time.sleep(2)
        q.put("alex")
sendName2()