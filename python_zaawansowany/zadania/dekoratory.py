from helpers import print_doc
from python_zaawansowany.training import Training
from python_zaawansowany.zadania.decorators import logged


class Task1Dek(Training):
    """
        Zad. 1
        Napisz dekorator, który służyć będzie do logowania, z jakimi argumentami dana funkcja została wywołana.
        Skorzystaj z **kwargs, *args oraz zmiennej specjalnej __name__,
        aby logować również nazwę funkcji, którą wywołujemy.

        Kod:
        @logged
        def func(*args):
           return 3 + len(args)

        func(4, 4, 4)

        Output:
        you called func(4, 4, 4) it returned 6
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        self.func(4, 4, 4)

    @staticmethod
    @logged
    def func(*args) -> int:
        return 3 + len(args)
