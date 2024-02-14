import string

from Szkolenie import Szkolenie
from helpers import print_doc


class Zadanie1KZ(Szkolenie):
    """Zad 1.
        Utwórz listę składającą się z następujących elementów: 'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony'.
        Przekształć tę listę w zbiór i zachowaj pod nową nazwą, a następnie:
        –	policz, ile elementów zawiera oryginalna lista kolorów
        –	policz, ile różnych kolorów zostało użytych
        –	wyświetl każdy z elementów zbioru w oddzielnej linii
        –	dodaj do zbioru nazwę jakiegoś innego koloru (sprawdź efekt przez wyświetlenie zawartości)
        –	usuń ze zbioru jakiś kolor (ponownie sprawdź efekt)
    """

    def __init__(self, szkolenie, zadanie, kolor):
        super().__init__(szkolenie, zadanie)
        self.lista = None
        self.kolor = kolor

    def utworz_lista(self):
        self.lista = ['czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny',
                      'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']
        return self.lista

    def utworz_zbior(self):
        return set(self.lista)

    def suma_elementow(self):
        return len(self.lista)

    def suma_unikalnych_elementow(self, zbior):
        return len(zbior)

    def zbior_dodaj(self, zbior):
        zbior.add(self.kolor)
        return zbior

    def zbior_usun(self, zbior):
        zbior.discard(self.kolor)
        return zbior


class Zadanie2KZ(Szkolenie):
    """Zad 2.
        Napisz program, który wczyta dowolne zdanie podane przez użytkownika. Usunie z tego zdania znaki interpunkcyjne
        (, . : ; ! ?), a następnie:
        korzystając z metod krotek:
        ●	zliczy wszystkie wyrazy w zdaniu
        ●	wydrukuje wszystkie wyrazy ze zdania w jednej linii
        ●	poda jaki jest pierwszy i czwarty wyraz w tym zdaniu
        korzystając z metod zbiorów:
        ●	zliczy unikatowe wyrazy w zdaniu
        ●	wyświetli unikatowe wyrazy ze zdania w jednej linii
        ●	poda jaki jest pierwszy i czwarty wyraz w tym zdaniu, zakładając, że pierwszy wyraz rozpoczyna zbiór.
        ●	sprawdzi, czy elementy: pierwszy i czwarty z ostatnich poleceń podpunktów a i b są takie same czy też nie.
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    def wczytaj(self):
        zdanie = input("Podaje dowolne zdanie: ")
        return zdanie

    def usun_interpunkcje(self, zdanie):
        usuwanie = str.maketrans("", "", string.punctuation)
        zdanie_bez_interpunkcji = zdanie.translate(usuwanie)
        return zdanie_bez_interpunkcji

    def tworzenie_krotki(self, zdanie):
        slowa = zdanie.split()
        krotka = tuple(slowa)
        return krotka

    def zlicz_wyrazy(self, krotka):
        liczba_elementów = len(krotka)
        return liczba_elementów

    def wyswielt_wyrazy(self, krotka):
        wyswietl = ' '.join(krotka)
        return wyswietl

    def utworz_zbior(self, zdanie):
        slowa = zdanie.split()
        zbior = set(slowa)
        return zbior

    def wyswietl_wybrany_wyraz_zbioru(self, zbior, *wyrazy):
        wyswietlone_wyrazy = []
        for i, element in enumerate(zbior):
            if i + 1 in wyrazy:
                print(f"Wyświetlam {i + 1} wyraz zbioru: {element}")
                wyswietlone_wyrazy.append(element)
        return wyswietlone_wyrazy

    def zlicz_unikatowe(self, zbior):
        unikatowe = len(zbior)
        return unikatowe

    def wyswietl_unikatowe_wyrazy(self, zbior):
        wyswietl = " ".join(zbior)
        return wyswietl

    def czy_wyswietlone_wyraz_takie_same(self, wyrazy1, wyrazy2):
        if wyrazy1 == wyrazy2:
            return "W tym przypadku są takie same"
        else:
            return "W tym przypadku nie są takie same"


class Zadanie3KZ(Szkolenie):
    """Zad 3.
        Napisz program, który poprosi użytkownika o podanie zestawu ulubionych przez niego kolorów (dowolna liczba).
        Kolory powinny być wpisane w jednej linii jako tekst i rozdzielone spacją.
        W programie powinien znajdować się zbiór Twoich ulubionych kolorów. Należy porównać oba zbiory:
        Twój i użytkownika oraz sprawdzić, czy są jednakowe. Jeśli tak, należy wydrukować odpowiedni komentarz,
        jeśli nie należy podać te kolory, które:
        ●          ●	wybrał tylko użytkownik
        ●	preferuje jedynie autor programu
    """

    def __init__(self, szkolenie, zadanie, moj_zbior: set = None):
        super().__init__(szkolenie, zadanie)
        if not moj_zbior:
            self.moj_zbior = {'niebieski', 'czerwony', 'zolty', 'zielony'}
        else:
            self.moj_zbior = moj_zbior
        self.zbior_wczytany = None

    @print_doc
    def rozwiazanie(self):
        self._podaj_kolory()
        zbior_stala = self._utworz_zbior()

        if self.czy_jednakowe():
            print("Kolory są jednakowe")
        else:
            print(f"Kolory wybrane przez dwie osoby: {self.wspolne_kolory(zbior_stala)}")
            print(f"Kolory wybrane tylko przez użytkownika: "
                  f"{self.kolowy_wybrane_tylko_przez_uzytkownika(zbior_stala, self.moj_zbior)}")
            print(f"Kolory wybranie tylko przez autora: "
                  f"{self.kolowy_wybrane_tylko_przez_uzytkownika(self.moj_zbior, zbior_stala)}")

    def _podaj_kolory(self):
        """Dokumentacja metod"""
        self.zbior_wczytany = input("Podaj kolory w jednej lini i rozdzielone spacją: ")
        return self.zbior_wczytany

    def _utworz_zbior(self):
        slowa = self.zbior_wczytany.split()
        zbior = set(slowa)
        return zbior

    def _czy_jednakowe(self):
        if self.zbior_wczytany == self.moj_zbior:
            return True
        else:
            return False

    def _wspolne_kolory(self, zbior):
        wspolne_kolory = zbior.intersection(self.moj_zbior)
        return wspolne_kolory

    def _kolowy_wybrane_tylko_przez_uzytkownika(self, zbior1, zbior2):
        kolory = zbior1.difference(zbior2)
        return kolory


class Zadanie4KZ(Szkolenie):
    """Zad 4.
        Napisz program, który utworzy dwa zbiory:
        ●	zbiór A: liczb naturalnych parzystych mniejszych od n (n podaje użytkownik)
        ●	zbiór B: liczb naturalnych mniejszych od n, które przy dzieleniu przez 3 dają resztę 2 oraz zbiory będące
         wynikiem następujących operacji matematycznych:

        C = A + B, D = A & B, E = A – B, F = B ^ A (różnica symetryczna)

        Dla każdego z utworzonych zbiorów program poda informacje o jego nazwie, liczebności
        i zawartych w nim elementach. Na koniec program sprawdzi, czy zbiór B zawiera się w zbiorze A.
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.n = None
        self.podaj_n()
        self.zbiorA = set()
        self.zbiorB = set()
        self.utworz_zbiorA()
        self.utworz_zbiorB()

    def podaj_n(self):
        try:
            self.n = int(input("Podaj n: "))
        except ValueError:
            print("Nie psuj")

    def utworz_zbiorA(self):
        for i in range(0, self.n, 2):
            if i != 0:
                self.zbiorA.add(i)
        return self.zbiorA

    def zlicz_element(self, zbior):
        zlicz = len(zbior)
        return zlicz

    def utworz_zbiorB(self):
        for i in range(self.n):
            if i % 3 == 2:
                self.zbiorB.add(i)
        return self.zbiorB

    def utworz_zbiorC(self):
        return self.zbiorA | self.zbiorB

    def utworz_zbiorD(self):
        return self.zbiorA & self.zbiorB

    def utworz_zbiorE(self):
        return self.zbiorA - self.zbiorB

    def utworz_zbiorF(self):
        return self.zbiorA ^ self.zbiorB

    def czy_zbiorB_zawiera_sie_w_zbiorB(self):
        return self.zbiorB < - self.zbiorA
