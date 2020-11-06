
# Testing the weird lambda expression syntax
import threading
import time

def print_1_2():
    print("1")
    time.sleep(1)
    print("2")

def print_3_4():
    print("3")
    time.sleep(1)
    print("4")

# worker 
t1 = lambda: print_1_2()
t2 = lambda: print_3_4()

th1 = threading.Thread(target=t1)
th2 = threading.Thread(target=t2)

th1.start()
th2.start()


th1.join()
th2.join()