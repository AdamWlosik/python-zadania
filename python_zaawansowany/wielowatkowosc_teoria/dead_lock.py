import threading


def do_deadlock():
    lock = threading.Lock()
    print("Before firs acquire")
    lock.acquire()
    print("Before second acquire")
    lock.acquire()
    lock.release()
    print("You'll never come over here!")


def main():
    do_deadlock()


if __name__ == "__main__":
    main()
