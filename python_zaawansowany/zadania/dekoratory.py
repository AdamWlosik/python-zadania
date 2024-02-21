import time
from dataclasses import dataclass

from helpers import print_doc
from python_zaawansowany.Training import Training
from python_zaawansowany.zadania.decorators import logged, stars_decorator, StarsDecorator, count, arg_check, timethis


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


class Task2Dek(Training):
    """Zad. 2
        Stwórz dekorator, który będzie służył do przyozdabiania wyświetlanego tekstu gwiazdkami.
        Dowolny tekst ten ma być wyświetlany z poziomu dekorowanej funkcji.

        Efekt:
        ************
        Hello World!
        ************

        Dodatkowo:
        Zrealizuj tę samą funkcjonalność, ale dekorator stwórz w oparciu o klasę i jej protokoły __call__ oraz __init__.
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        txt = "Hello World!"
        self.display(txt)
        self.display_class(txt)

    @staticmethod
    @stars_decorator
    def display(txt: str) -> None:
        print(txt)

    @staticmethod
    @StarsDecorator
    def display_class(txt: str) -> None:
        print(txt)


class Task3Dek(Training):
    """Zad. 3
        Napisz dekorator @count, który wyświetlał będzie tworzył słownik,
        w którym będziemy przechowywali informację, ile razy zostały wywołane poszczególne funkcje
        udekorowane właśnie tym dekoratorem.
        """

    def __init__(self, training: int, taks: int):
        super().__init__(training, taks)

    @print_doc
    def solution(self):
        self.example_func()
        self.example_func()
        self.example_func()
        self.example_func2()
        self.example_func2()
        self.example_func2()
        self.example_func2()
        self.example_func2()

    @count
    def example_func(self) -> None:
        pass

    @count
    def example_func2(self) -> None:
        pass


class Task4Dek(Training):
    """Zad. 4
        W szkoleniu nie zostało o tym wspomniane, ale możemy również określać przesyłane argumenty dekoratorów!
        Jedyna konieczność jaka będzie do zrealizowania, to dodanie kolejnej funkcji wrappującej, czyli np:

        def arg_check(arg):
            def check(old_func):
                def new_func():
                    # do sth with arg and call old_func as examp

                return new_func
            return check

        @arg_check(arg)
        def examp(num):
            # do sth

        Twoje zadanie to stworzyć dekorator, który sprawdzać będzie, czy określony w dekoratorze
        typ jest zgodny z typem zmiennej przesłanej do funkcji.

        Podpowiedź:
        -	Przesyłaj jako argument do dekoratora obiekt typu: int, float itd
        -	Sprawdzaj, czy typy są zgodne przy użyciu isinstance(zmienna, typ_oczekiwany)
        -	Jeżeli typ będzie niezgodny, rzucaj wyjątkiem

        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        try:
            self.examp(5)
            self.examp(5.33)
        except TypeError as error:
            print("Błąd: ", error)

    @staticmethod
    @arg_check(int)
    def examp(num: int) -> None:
        print(f"Przekazano poprawny argument {num}")


class Task5Dek(Training):
    """Zad. 5
        Utwórz dekorator @timethis mierzący czas wykonania dekorowanej funkcji.
        Wykorzystaj moduł time i metodę time.time().
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        self.example_func()

    @timethis
    def example_func(self):
        time.sleep(2)


class PropertyClass:

    def __init__(self, data):
        self.data = data

    @property
    def data_metod(self):
        return self.data


@dataclass
class Data:
    training: int
    task: int


class Addition:

    @classmethod
    def add(cls, x, y):
        return x + y


class Task6Dek(Training):
    """Zad. 6
    Zapoznaj się, do czego służą wbudowane w standard Pythona poniższe dekoratory:
    @property, @abstractmethod, @dataclass, @classmethod i @staticmethod.
    Zbuduj proste programy przedstawiające realizację tych dekoratorów i różnice między nimi.
    """

    def __init__(self, training: int, taks: int):
        super().__init__(training, taks)

    @print_doc
    def solution(self):
        self.display_theory()
        property_class = PropertyClass("Klasa ProperytyClass i metoda data_metod() jest przykładem użycia @property")
        print(property_class.data_metod)
        print("Klasa Training i metoda solution() jest przykładem użycia @abstractmethod")
        data = Data(self.training, self.task)
        print("Klasa Data jest przykładem użycia @dataclass,\n", data)

        print(f"Klasa Addition jest przykładem użycia @classmethod, "
              f"\n {self.task} + {self.training} =", Addition.add(self.task, self.training))
        print("Funkcja display_theory() jest przykładem użycia @staticmethod")

    @staticmethod
    def display_theory():
        print("@property: Ten dekorator służy do definiowania tzw. właściwości (properties) dla klasy. "
              "Pozwala na wywoływanie metody bez użycia nawiasów, co sprawia, że kod jest bardziej czytelny i zwięzły."
              "\n@abstractmethod: Ten dekorator jest często używany w klasach abstrakcyjnych. "
              "Metody oznaczone jako abstrakcyjne muszą być zaimplementowane w klasach dziedziczących, "
              "w przeciwnym razie zostanie zgłoszony błąd."
              "\n@dataclass: Ten dekorator służy do tworzenia klas, które służą głównie do przechowywania danych. "
              "Automatycznie generuje metody takie jak __init__(), __repr__(), __eq__(), itd., "
              "na podstawie zdefiniowanych pól."
              "\n@classmethod: Ten dekorator definiuje metodę, która jest powiązana z klasą, a nie z instancją klasy. "
              "Metoda ta przyjmuje jako pierwszy argument klasę (cls) zamiast instancji."
              "\n@staticmethod: Ten dekorator definiuje metodę, która nie ma dostępu do instancji ani do klasy. "
              "Jest to po prostu funkcja wewnątrz klasy, która jest logicznie związana z tą klasą.\n\n")
