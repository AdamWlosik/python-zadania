import json
from collections import OrderedDict

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
    INWOKACJA = """ Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
                    Ile cię trzeba cenić, ten tylko się dowie,
                    Kto cię stracił. Dziś piękność twą w całej ozdobie"""

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.text = ("""Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
                        Ile cię trzeba cenić, ten tylko się dowie, 
                        Kto cię stracił. Dziś piękność twą w całej ozdobie""")

    @print_doc
    def rozwiazanie(self):
        self._zapisz_plik()
        self._wyswietl_parzyste()

    def _zapisz_plik(self):
        """Metoda zapisująca podany tekst do pliku"""
        with open("przyklad.txt", "w", encoding="utf8") as plik:
            plik.write(self.INWOKACJA)

    def _wyswietl_parzyste(self):
        """Metoda wyświetlająca parzyste linie wczytane z pliku"""
        with open("przyklad.txt", encoding="utf8") as plik:
            linie = plik.readlines()
            for index, linia in enumerate(linie, start=1):
                if index % 2 == 0:
                    print(linia)


class Zadanie4PS8(Szkolenie):
    """Zad 4.
        Jaka jest różnica między kodowaniem UTF-8 a ASCII? Jaki byłby rezultat odczytania
        z pliku polskich liter (np. ą, ę, ć) bez zmiany sposobu formatowania danych?
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        with open("utf8 - ascii i róznice.txt", encoding="utf8") as plik:
            for linia in plik:
                print(linia, end='')


class Zadanie5PS8(Szkolenie):
    """Zad 5.
        Załóżmy, że plik przyklad.txt składa się tylko i wyłącznie z następującej linii tekstu:
        Panno święta, co Jasnej bronisz Częstochowy
        Jaki efekt otrzymamy, po zapisie poniższych poleceń?
        with open("przyklad.txt", encoding="utf-8") as plik:
            plik.tell()
            plik.seek(43)
            print(plik.read(1)) # ???
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        with open("przyklad2.txt", encoding="utf-8") as plik:
            plik.tell()
            plik.seek(43)
            print(plik.read(1))
        # zwraca "o" a jeśli dobrze rozumiem to tell() zwraca początkową pozycje wskaźnika 0
        # sek(43) robi 43 przejścia a plik ma zanki od 0-42
        # read(1) odczytuje znak o 1 od aktualnej pozycje słownika czyli takie zank nie istnieje?


class Zadanie6PS8(Szkolenie):
    """Zad 6.
        Odczytaj 4. linię z pliku: test.txt o zawartości:
        line1
        line2
        line3
        line4
        line5
        line6
        line7
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        with open("text.txt") as plik:
            for index, line in enumerate(plik):
                if index == 3:
                    print(line)


class Zadanie7PS8(Szkolenie):
    """Zad 7.
        Masz do dyspozycji plik przyklad.txt o następującej zawartości:
        Jak czarne ptaki, lecąc lecąc w wyższą nieba nieba stronę,
        Coraz się zgromadzały. Ledwie słońce zbiegło zbiegło
        Z południa, już już ich stado pół pół niebios obiegło

        Jak możesz zauważyć, gdzieniegdzie wkradły się powtórzenia słów. Zmodyfikuj i zapisz nowy plik tak, aby się ich pozbyć.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.zawartosc_pliku = None
        self.slowa = None
        self.lista = []
        self.nowa_lista = []
        self.nowy_str = str

    @print_doc
    def rozwiazanie(self):
        self.zawartosc_pliku = self._wczytaj_plik()
        self.slowa = self._podziel_str()
        self.lista = self._utworz_liste()
        print("Lista:", self.lista)
        self.nowa_lista = self._usun_powtorzenia()
        print("Nowa lista: ", self.nowa_lista)
        self.nowy_str = self._uwtorz_nowego_str(self.nowa_lista)
        print(self.nowy_str)
        self._zapisz()

    @print_doc
    def rozwiazanie_OrderDict(self):
        """Rozwiązanie przy pomocy OrderDict słownika z zachowaniem kolejności i kluczu deafultowym None"""
        self.zawartosc_pliku = self._wczytaj_plik()
        self.slowa = self._podziel_str()
        bez_powtorzen = OrderedDict.fromkeys(self.slowa)
        print(bez_powtorzen)
        self.nowy_str = self._uwtorz_nowego_str(bez_powtorzen)
        print(self.nowy_str)
        self._zapisz()

    def _wczytaj_plik(self):
        """Motoda wczczytująca plik txt do zmiennej"""
        with open("przyklad7.txt", encoding="utf=8") as plik:
            zawartosc_pliku = plik.read()
            return zawartosc_pliku

    def _podziel_str(self):
        """Metoda dzieląca stringa na całe słowa """
        slowa = self.zawartosc_pliku.split()
        return slowa

    def _utworz_liste(self):
        """Metoda tworząca listę ze słów z pliku"""
        lista = []
        for slowo in self.slowa:
            lista.append(slowo)
        return lista

    def _usun_powtorzenia(self):
        """Metoda sprawdzająca czy bieżący i następny element listy jest taki sam i usuwająca powtórzenia"""
        nowa_lista = []
        for index, wyraz in enumerate(self.lista):
            if index + 1 < len(self.lista) and wyraz != self.lista[index + 1] \
                    or index + 1 == len(self.lista):
                nowa_lista.append(wyraz)
        return nowa_lista

    def _uwtorz_nowego_str(self, dana):
        """Metoda towrząca nowego stringa ze wcześniej utworzonej listy"""
        nowy_str = " ".join(dana)
        return nowy_str

    def _zapisz(self):
        with open("przyklad7odp.txt", "w", encoding="utf8") as plik:
            plik.write(str(self.nowy_str))


class Zadanie9PS8(Szkolenie):
    """Zad 9.
        W załączeniu znajduje się plik data.json. Przechowuje on informacje o różnych pakietach informacji.
        Twoim zadaniem jest napisanie skryptu, który będzie odczytywał taki pliku i drukował poniższy komunikat
        zawierający informacje o każdym z pakietów:
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        self._wydrukuj_interface()
        dane_json = self._odczytaj_json()
        self._wydrukuj_dane(dane_json)

    def _wydrukuj_interface(self):
        """Motoda służąca do drukowania górnej stopki interface"""
        print("Interface Status")
        print("=" * 80)
        print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
        print("{:<50} {:<20} {:<8} {:<6}".format("-" * 50, "-" * 20, "-" * 8, "-" * 6))

    def _odczytaj_json(self):
        """Motoda wczytująca dane z pliku json do zmiennej"""
        with open("10 Podstawy Szkolenie 8 - data.json", encoding="utf=8") as plik:
            dane_json = json.load(plik)
            return dane_json

    def _wydrukuj_dane(self, dane_json):
        """Motoda drukująca dane z pliku json do konsoli
           Z json pracowałem raz także tutaj chat gpt pomógł"""
        for dana in dane_json.get("imdata", []):
            # pobiera wartość dla klucza imdata jęśli nie istnieje
            # dzięki metodzie get używamy wrtości domyślnej, którą jest [}
            l1PhysIf = dana.get("l1PhysIf", {}).get("attributes", {})
            dn = l1PhysIf.get("dn", "")
            description = l1PhysIf.get("descr", "")
            speed = l1PhysIf.get("speed", "inherit")
            mtu = l1PhysIf.get("mtu", "unspecified")
            print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))


class Zadanie8PS8(Szkolenie):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.odwrocony_slownik = {}

    @print_doc
    def rozwiazanie(self):
        self.odwrocony_slownik = self._odwroc(klucz1='wartość1', klucz2='wartość2', klucz3='wartość3')
        self._zapis_json()
        print('Rozwiązanie zapisane do pliku "output.json"')

    def _odwroc(self, **kwargs):
        """Metoda odwracjąca słownik"""
        odwrocony_slownik = {wartosc: klucz for klucz, wartosc in kwargs.items()}
        return odwrocony_slownik

    def _zapis_json(self):
        with open("output.json", "w", encoding='utf8') as plik:
            json.dump(self.odwrocony_slownik, plik, ensure_ascii=False)
