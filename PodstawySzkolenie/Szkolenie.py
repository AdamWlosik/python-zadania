import abc
from abc import ABC

from helpers import print_doc


class Szkolenie(ABC):
    """Klasa abstrakcyjna szkolenie"""
    def __init__(self, szkolenie, zadanie):
        self.szkolenie = szkolenie
        self.zadanie = zadanie
        self.tytul()

    def tytul(self):
        print(f"Wybrałeś szkolenie: {self.szkolenie} i zadanie: {self.zadanie}: ")

    # @abc.abstractmethod
    def rozwiazanie(self):
        pass
