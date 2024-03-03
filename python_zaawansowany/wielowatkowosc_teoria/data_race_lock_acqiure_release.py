import threading

value = 0
lock = threading.Lock()  # tworzenie obiektu


# def increase_by_one():
#     global value
#     lock.acquire()  # blokuje wątek
#     for i in range(1000000):
#         value += 1
#     lock.release()  # odblokowuje po wykonaniu


def increase_by_one():
    global value

    with lock:  # można użyć zamiast acqiure i realase
        for i in range(100000):
            value += 1


def main():
    threads = [
        threading.Thread(target=increase_by_one),
        threading.Thread(target=increase_by_one),
    ]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(value)


if __name__ == "__main__":
    main()
