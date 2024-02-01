from PodstawySzkolenie.Szkolenie import Szkolenie
from helpers import print_doc


class Zadanie1PS8(Szkolenie):
    """Zad 1.
        Określ, czy poniższe ścieżki do plików .txt są względne/bezwzględne:
        C:\przyklad.txt
        \katalog\przyklad.txt
        C:\outer_dir\inner_dir\przyklad.txt
        \outer_dir\innedr_dir\przyklad.txt
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        print("Scieżka bezwzględna podaje pełną lokalizacje to znaczy, ze zaczyna się od dysku\n"
              "Ścieżki bezwzględne: \n"
              "\katalog\przyklad.txt\n"
              "\outer_dir\innedr_dir\przyklad.txt\n"
              "Ścieżki względne: \n"
              "C:\przyklad.txt\n"
              "C:\outer_dir\inner_dir\przyklad.txt")


class Zadanie2PS8(Szkolenie):
    """Zad 2.
        Znajdź błąd w poniższym przykładzie realizującym odczyt danych z pliku: przyklad.txt.

        plik = open("przyklad.txt", "r")
        linie = plik.readlines()
        print(linie)
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        print("Brakuje zamknięcia pliku używając: \n"
              "plik.colse()\n"
              "lub użycia konstrukcji with: \n"
              "with open('przyklad.txt, 'r') as plik:")


class Zadanie3PS8(Szkolenie):
    """Zad 3.
        Stwórz plik o nazwie przyklad.txt i umieść w nim następujący tekst:
        Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
        Ile cię trzeba cenić, ten tylko się dowie,
        Kto cię stracił. Dziś piękność twą w całej ozdobie
        Następnie wyświetl z pliku zawartość jego parzystych linii.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.text = ("""Litwo, Ojczyzno moja! ty jesteś jak zdrowie "
                     "Ile cię trzeba cenić, ten tylko się dowie Kto cię stracił. "
                     "Dziś piękność twą w całej ozdobie""")

    @print_doc
    def rozwiazanie(self):
        self._zapisz_plik(self.text)
        self._wyswietl_parzyste()

    def _zapisz_plik(self, text):
        """Metoda zapisujeąca podant tekst do pliku"""
        with open("przyklad.txt", "w", encoding="utf8") as plik:
            plik.write(text)

    def _wyswietl_parzyste(self):
        """Metoda wyświetlająca parzyste linie wczytane z pliku"""
        with open("przyklad.txt", encoding="utf8") as plik:
            linie = plik.readlines()
            for index, linia in enumerate(linie, start=1):
                if index % 2 == 0:
                    print(linia)

