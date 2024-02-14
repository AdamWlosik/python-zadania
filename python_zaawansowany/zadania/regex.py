import re

from Szkolenie import Szkolenie
from helpers import print_doc


class Task1Regex(Szkolenie):
    """Zad. 1
        Napisz program, który sprawdzi, czy string zawiera tylko
        i wyłącznie zbiór następujących znaków: (a-z, A-Z i 0-9).
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def rozwiazanie(self):
        text = "Nie tylko odpowiednie znaki!!"
        text2 = "Tylkoodpowiednieznaki234"
        print(self.check(text))
        print(self.check_compile(text))
        print(self.check(text2))
        print(self.check_compile(text2))

    @staticmethod
    def check_compile(text):
        """Metoda kompilująca wzorzec, na podstawie którego szukamy dopasowań"""
        pattern = re.compile(r'^[a-zA-Z0-9]+$')
        return bool(pattern.match(text))

    @staticmethod
    def check(text):
        """Metoda szukająca dopasowań """
        match = re.match(r'^[a-zA-Z0-9]+$', text)
        return bool(match)


class Task2Regex(Szkolenie):
    """Zad. 2
        Sprawdź, czy string rozpoczyna się pojedynczą cyfrą: 0 lub literą ‘b’.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        text = "Nie tylko odpowiednie znaki !!"
        text1 = "0Tylkoodpowiednieznaki234"
        text2 = "bTylkoodpowiednieznaki234"
        print(self.check(text))
        print(self.check(text1))
        print(self.check(text2))

    @staticmethod
    def check(text):
        """Metoda sprawdzająca początek str"""
        return bool(re.match(r'^[0b]', text))


class Task3Regex(Szkolenie):
    """Zad. 3
        Sprawdzaj, czy podany string zawiera ciąg dowolnych małych liter rozdzielonych znakiem _, np. aab_cbbbc
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def rozwiazanie(self):
        text = "nie tylko odpowiednie znaki !!"
        text1 = "aab_cbbbc"
        text2 = "bylkoodpow_iednieznaki"
        print(self.check(text))
        print(self.check(text1))
        print(self.check(text2))

    @staticmethod
    def check(text):
        pattern = r'^[a-z]+_+[a-z]+$'
        return bool(re.match(pattern, text))

