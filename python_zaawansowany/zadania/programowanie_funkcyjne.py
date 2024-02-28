from functools import reduce

from helpers import print_doc
from python_zaawansowany.training import Training


class Task1PF(Training):
    """Zad 1.
        Napisz funkcję lambda, który doda wartość 15 do przesłanej wartości w postaci argumentu.
        Stwórz również lambdę, która przyjmie dwa argumenty x i y oraz obliczy ich iloczyn. Wyświetl wyniki.
        """

    def __init__(self, training: int, taks: int):
        super().__init__(training, taks)

    @print_doc
    def solution(self) -> None:
        add = lambda x: x + 15
        multiply = lambda x, y: x * y
        value = 10
        x = 2
        y = 4
        print(f"Wynik dodawania {value} + 15 = {add(value)}")
        print(f"Wynik mnożenia {x} * {y} = {multiply(x, y)}")


class Task2PF(Training):
    """Zad 2.
        Napisz program, który posortuje listę krotek przy wykorzystaniu funkcji lambda oraz metody .sort().
        Lambdę wykorzystuj przy wskazaniu, według którego (drugiego) elementu ma odbywać się sortowanie.

        to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        to_sort.sort(key=lambda x: x[1])
        print(to_sort)


class Task3PF(Training):
    """Zad 3.
        Stwórz program, który zwróci kwadraty oraz sześciany wartości zapisanych w liście. Wykorzystaj funkcje lambda.

        Oryginalna lista:
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        Kwadraty liczb:
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

        Sześciany liczb:
        [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print("Oryginalna lista:")
        print(numbers)
        square = list(map(lambda x: x ** 2, numbers))
        print("Kwadraty liczb:")
        print(square)
        cube = list(map(lambda x: x ** 3, numbers))
        print("Sześciany liczb:")
        print(cube)


class Task4PF(Training):
    """Zad 4.
        Wykorzystując paradygmat funkcyjny oraz metodę count(),
        sprawdź ile ciągów nie zawiera w sobie napisu składającego się z dwóch 1 obok siebie.

        lines = [‘10000101011’, ‘111111’, ‘01010101010010’, ‘011001100001’, ‘001010101011’
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        lines = ["10000101011", "111111", "01010101010010", "011001100001", "001010101011", "0001"]
        filter_lines = list(filter(lambda line: line.count("11") == 0, lines))
        print(filter_lines)
        print(f"{len(filter_lines)} ciągi ")


class Task5PF(Training):
    """Zad 5.
        Napisz program, który obliczy sumę trzech list o tej samej długości i zwróci wynik jednej konkretnej liczby.
        Wykorzystaj reduce() oraz lambdę.

        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        nums3 = [7, 8, 9]
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        nums3 = [7, 8, 9]
        nums_sum = reduce(lambda x, y: x + y, nums1 + nums2 + nums3)
        print("Suma: ", nums_sum)


class Task6PF(Training):
    """Zad 6.
        Stwórz program, który przekonwertuje listę krotek na listę stringów. Wykorzystaj map().

        colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

        na

        ['red pink', 'white black', 'orange green']


        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
        converted_colors = list(map(lambda x: " ".join(x), colors))
        print(converted_colors)


class Task7PF(Training):
    """Zad 7.
        Mając do dyspozycji poniższą listę liczb całkowitych:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        Stwórz listę new_nums, która będzie zawierała kwadraty powyższych liczb,
        ale tylko takich, które są parzyste. Wykorzystaj lambdy.
        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self) -> None:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # even_nums = filter(lambda x: x % 2 == 0, nums)
        new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
        print(new_nums)


class Task8PF(Training):
    """Zad. 8
        Wyobraź sobie, iż masz do dyspozycji następującą listę 4 zamówionych produktów o następujących właściwościach:
        id, nazwa, ilość, cena.

        orders = [
        ["34587", "Learning Python, Mark Lutz", 4, 40.95],
        ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],
        ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
        ]

        Twoim zadaniem jest stworzenie programu budującego fakturę dla powyższej listy. Lista ta ma zawierać krotki,
        które przechowywać będą kolejno id danego produktu i cenę, jaką należy za niego zapłacić.
        Jednak istnieje pewne dodatkowe utrudnienie - wartość zamówień poniżej 100 zł, musi być zwiększana o 10.
        Czyli wynikiem dla powyższej listy będzie:

        invoice = [('34587', 163.8), ('98762', 284.0), ('77226', 108.85000000000001), ('88112', 84.97)]

        """

    def __init__(self, training: int, task: int):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        orders = [
            ["34587", "Learning Python, Mark Lutz", 4, 40.95],
            ["98762", "Programming Python, Mark Lutz", 5, 56.80],
            ["77226", "Head First Python, Paul Barry", 3, 32.95],
            ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
        ]
        invoice = [(order[0], order_value + 10 if order_value < 100 else order_value)
                   for order, order_value in map(lambda x: (x, x[2] * x[3]), orders)]

        print(invoice)
