import string

from PodstawySzkolenie.Szkolenie import Szkolenie


class Zadanie1KZ(Szkolenie):

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

    def __init__(self, szkolenie, zadanie, moj_zbior):
        super().__init__(szkolenie, zadanie)
        self.moj_zbior = moj_zbior
        self.zbior = None
        self.podaj_kolory()

    def podaj_kolory(self):
        self.zbior = input("Podaj kolory w jednej lini i rozdzielone spacją: ")
        return self.zbior

    def utworz_zbior(self):
        slowa = self.zbior.split()
        zbior = set(slowa)
        return zbior

    def czy_jednakowe(self):
        if self.zbior == self.moj_zbior:
            return True
        else:
            return False

    def wspolne_kolory(self, zbior):
        wspolne_kolory = zbior.intersection(self.moj_zbior)
        return wspolne_kolory

    def kolowy_wybrane_tylko_przez_uzytkownika(self, zbior1, zbior2):
        kolory = zbior1.difference(zbior2)
        return kolory


class Zadanie4KZ(Szkolenie):

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
