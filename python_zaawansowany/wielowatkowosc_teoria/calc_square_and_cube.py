import threading
import time


def calc_square(numbers):
    print("Calculate square numbers: ")
    for i in numbers:
        print("square: ", str(i ** 2))
        time.sleep(0.1)


def calc_cube(numbers):
    print("Calculate cube numbers")
    for i in numbers:
        print("cube", str(i ** 3))


def main():
    arr = [2, 3, 8, 9]
    t1 = threading.Thread(target=calc_square, args=[arr])
    t2 = threading.Thread(target=calc_cube, args=[arr])

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Succeeded")


if __name__ == "__main__":
    main()
