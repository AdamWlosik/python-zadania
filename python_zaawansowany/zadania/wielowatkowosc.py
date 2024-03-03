import multiprocessing
import random
import threading
import time
from pprint import pprint

from helpers import print_doc
from python_zaawansowany.training import Training


class Task1W(Training):
    """Zad 1
    Stwórz program, który będzie sortował dziesięć 100-elementowych tablic
    z wykorzystaniem bubble sorting w podejściu wielowątkowym (multithreading)
    oraz wieloprocesowym (multiprocessing). Porównaj czasy.

    Rozważ również problem:
    Ile wątków należy stworzyć, aby program był wykonany jak najszybciej i
    optymalnie? Aby odpowiedzieć na to pytanie, zapoznaj się z “Amdahl’s Law”.
    """

    def __init__(self, training: int, taks: int):
        super().__init__(training, taks)

    @print_doc
    def solution(self):
        pprint(
            "Aby odpowiedzieć na pytanie o optymalną liczbę wątków lub procesów, które należy stworzyć, "
            "można sięgnąć po prawo Amdahla. Prawo to mówi o tym, że mimo zwiększenia liczby procesorów, "
            "przyspieszenie danej operacji jest ograniczone przez część sekwencyjną (niepodlegającą równoległemu "
            "przetwarzaniu) tej operacji. W przypadku sortowania bąbelkowego, większość operacji jest sekwencyjna, "
            "więc zbyt wiele wątków lub procesów może spowodować spowolnienie z powodu narzutu związane z "
            "zarządzaniem nimi.Optymalna liczba wątków lub procesów będzie zależeć od natury zadania, "
            "ale zazwyczaj dobrym pomysłem jest eksperymentowanie z różnymi liczbami i monitorowanie czasu "
            "wykonania, aby znaleźć optymalną wartość."
        )
        arr = [[random.randint(1, 1000) for _ in range(100)] for _ in range(10)]

        start_time = time.time()
        self.multithread_bubble_sort(arr)
        print(
            "Czas sortowania wielowątkowego: %.5f sekund" % (time.time() - start_time)
        )

        start_time = time.time()
        self.multiprocessing_bubble_sort(arr)
        print(
            "Czas sortowania wieloprecesorowego: %.5f sekund"
            % (time.time() - start_time)
        )

    @staticmethod
    def bubble_sort(arr) -> None:
        """Metoda sortująca algorytmem bubble sort"""
        n = len(arr)
        for i in range(n):
            for j in range(0, n - 1 - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def multithread_bubble_sort(self, arr):
        """Metoda sortująca wielowątkowo"""
        threads: list = []
        for i in range(len(arr)):
            thread = threading.Thread(target=self.bubble_sort, args=(arr[i],))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def multiprocessing_bubble_sort(self, arr):
        processes: list = []
        for i in range(len(arr)):
            process = multiprocessing.Process(target=self.bubble_sort, args=(arr[i],))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()
