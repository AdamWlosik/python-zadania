import threading

value = 0


def increase_by_one():
    global value
    for i in range(1000000000):
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


# TODO
# Dlaczego u mnie wynik: 200000, szybkość procesora (chyba nie bo zwiększyłem range),
# wykorzystuje najpierw 6 wątki później spada do 3

if __name__ == "__main__":
    main()
