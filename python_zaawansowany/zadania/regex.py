import re

from Szkolenie import Szkolenie
from helpers import print_doc


class Task1Regex(Szkolenie):
    """Zad. 1
        Napisz program, który sprawdzi, czy string zawiera tylko
        i wyłącznie zbiór następujących znaków: (a-z, A-Z i 0-9).
        """
    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        text = ("Nie tylko odpowiednie zanki !!")
        text2 = "Tylkoodpowiednieznaki234"
        print(self.check(text))
        print(self.check(text2))

    def check(self, text):
        """Metoda """
        pattern = re.compile(r'^[a-zA-Z0-9]+$')
        return bool(pattern.match(text))
