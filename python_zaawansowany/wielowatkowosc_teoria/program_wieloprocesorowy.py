import time
from multiprocessing import Pool
from threading import Thread


# program wielowątkowy
class Wielowatkowy:
    TIME = 25000000

    @staticmethod
    def countdown(n: int):
        while n > 0:
            n -= 1

    if __name__ == "__main__":
        t1 = Thread(target=countdown, args=[TIME])
        t2 = Thread(target=countdown, args=[TIME])

        start = time.time()
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        end = time.time()

        print("Time taken in seconds, multithread: ", end - start)


# ----------------------------------------------------------------------------------
# program wieloprocesorowy


class Wieloprocesorowy:
    TIME = 25000000

    @staticmethod
    def countdown(n: int):
        while n > 0:
            n -= 1

    if __name__ == "__main__":
        pool = Pool(processes=2)
        start = time.time()
        p1 = pool.apply_async(countdown, [TIME])
        p2 = pool.apply_async(countdown, [TIME])
        pool.close()
        pool.join()
        end = time.time()
        print("Time taken in second, multiprocessing: ", end - start)
