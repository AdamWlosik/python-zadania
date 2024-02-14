from Szkolenie import Szkolenie
from helpers import print_doc


class Zadanie1(Szkolenie):
    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        pass