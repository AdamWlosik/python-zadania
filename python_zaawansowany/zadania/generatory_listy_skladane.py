from typing import Generator

from helpers import print_doc
from python_zaawansowany.training import Training


class Task1GLS(Training):
    """Zad 1.
        Napisz funkcję generatora, która generować będzie kilka dowolnych wartości.
        Pobierz te wartości przy użyciu globalnej metody next() oraz metody generatora __next__().
        Rzuć wyjątkiem wewnątrz generatora (po jego kilkukrotnym wywołaniu) i zbadaj stack trace.
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        gen = self.generator()
        try:
            for _ in range(5):
                print(next(gen))
        except ValueError as error:
            print("Wystąpił wyjątek:", error)
        gen = self.generator()
        try:
            for _ in range(5):
                print(gen.__next__())
        except ValueError as error:
            print("Wystąpił wyjątek: ", error)

    @staticmethod
    def generator() -> Generator[int, None, None]:
        "Metoda generująca dowolne wartosci i zwracająca wyjątek"
        value: int = 0
        while True:
            yield value
            value += 1
            if value == 4:
                raise ValueError("Wyjątek wartość = 4")


class Task2GLS(Training):
    """Zad 2.
        Stwórz generator, który generował będzie kolejne liczby pierwsze.
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        generator = self.prime_generator()
        for _ in range(10):
            print(next(generator))

    @staticmethod
    def is_prime(number: int) -> bool:
        """Metoda sprawdzjąca czy liczba jest pierwsza"""
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def prime_generator(self) -> Generator[int, None, None]:
        "Metoda generująca liczby pierwsze"
        number = 2
        while True:
            if self.is_prime(number):
                yield number
                number += 1


class Task3GLS(Training):

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        examp = (i for i in range(10))
        print(examp)
        print("Zamiast examp = (i for i in range(10)) należy zapisać examp = [i for i in range(10)]")
        examp = [i for i in range(10)]
        print(examp)


class Task4GLS(Training):

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        generator = self.fibo_generator()
        for _ in range(10):
            print(next(generator))

    @staticmethod
    def fibo_generator() -> Generator[int, None, None]:
        """Metoda obliczjąca kolejne wyrazu ciągu fibo"""
        a = 1
        b = 2
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b


class Task5GLS(Training):
    """Zad 4.
        Mając tak utworzoną listę liczb:
        numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]
        Wykorzystując, list comprehension, utwórz nową o nazwie filtered_numbers,
        w której znajdą się tylko liczby niedodatnie z numbers.
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]
        print(numbers)
        filtered_numbers = [number for number in numbers if number < 0]
        print(filtered_numbers)


class Task6GLS(Training):
    """Zad 5.
        Bazując na następującym tekście:
        “The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains
        all of the letters of the English alphabet”,
        wydziel go na listę przechowującą długości kolejnych wyrazów z pominięciem słowa “the”, np.

        length_of_words = [5, 5, 3, 5, ...], co odpowiada kolejno długościom wyrazów: quick, brown, fox, jumps.
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        text = ("The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains"
                "all of the letters of the English alphabet")
        words = [word for word in text.split() if word.lower() != "the"]
        length_of_worlds = [len(word) for word in words]
        print(length_of_worlds)


class Task7GLS(Training):
    """Zad. 6
        Mając do dyspozycji poniższą listę trójwymiarową:

        three_d = [
        [[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]],
        [[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]
        ]

        przefiltruj ją tak, by znalazły się tylko te najbardziej wewnętrzne listy, których ilość elementów przekracza 4.

        Wynikiem powinna być lista:

        [[0, -1, -2, -3, -4, -5, -6], [1, 10, 15, 1, 20, 20, 20], [-15, -13, 14, 20, -1]]
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        three_d = [
            [[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]],
            [[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]
        ]

        filtered_lists = [inner_list for outer_list in three_d for inner_list in outer_list if len(inner_list) > 4]
        print(filtered_lists)


