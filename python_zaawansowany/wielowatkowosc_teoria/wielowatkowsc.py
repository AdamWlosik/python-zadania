import threading


def new_thread():
    print("Thread is running")
    for x in range(10):
        print(x)


t1 = threading.Thread(target=new_thread())
t1.start()
t1.join()
