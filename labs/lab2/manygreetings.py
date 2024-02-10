from multiprocessing import *

def sayHi2(n):
    print("Hi", n, "from process", current_process().pid)

def manyGreetings():
    name = input("Enter your name: ")
    num_proc = int(input("Enter the number of processes: "))

    for i in range(num_proc):
        (Process(target=sayHi2, args=(name,))).start()
manyGreetings()