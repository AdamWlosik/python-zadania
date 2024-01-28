import string

from PodstawySzkolenie.Szkolenie import Szkolenie


class Zadanie1S(Szkolenie):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.klucz = None
        self.slowinik = None
        self.uwtorz_slownik()
        self.menu()

    def uwtorz_slownik(self):
        self.slowinik = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2',
                         'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}

    def menu(self):
        while True:
            try:
                wybor = int(input("Aby wyświetlić wszystkie klucze wybierz 1 \n"
                                  "Aby wyświetlić wartość wybranego klucza wybierz 2 \n"
                                  "Aby dodać informacje o nowym albumie wybierz 3 \n"
                                  "Aby usunąć informacje o albumie wybierz 4 \n"
                                  "Aby zakończyć wybierz 0 \n"
                                  ""))
                if 0 > wybor > 4:
                    print("Nie psuj!")
            except ValueError:
                print("Nie psuj!")
            if wybor == 1:
                self.wyswietl_klucze()
            elif wybor == 2:
                self.pobierz_lancuch()
                self.wyswielt_wartosc_podanego_kulcza()
            elif wybor == 3:
                self.dodaj()
            elif wybor == 4:
                self.usun()
            elif wybor == 0:
                break

    def wyswietl_klucze(self):
        klucze = self.slowinik.keys()
        print(f"Klucze słownika: {klucze}")

    def pobierz_lancuch(self):
        self.klucz = input("Podaj klucz, po którym chcesz wyświetlić: ")

    def wyswielt_wartosc_podanego_kulcza(self):
        """Używam self.slowinik.get(self.klucz), aby uniknąć błędu KeyError, gdy klucz nie istnieje.
        Metoda get() zwraca wartość dla danego klucza, a jeśli klucz nie istnieje,
        zwraca wartość domyślną (domyślnie None)."""
        war = self.slowinik.get(self.klucz)
        if war:
            print(f"Wartość dla podanego klucza {self.klucz}: {self.slowinik[self.klucz]}")
        else:
            print("Brak danych")

    def dodaj(self):
        klucz = input("Podaj klucz, który chcesz dodać: ")
        wartosc = input(f"Podaj wartość dla dodanego klucza {klucz}: ")
        self.slowinik[klucz] = wartosc

    def usun(self):
        klucz = input("Podaj klucz: ")
        try:
            del self.slowinik[klucz]
        except KeyError:
            print("Klucz nie istnieje")


class Zadanie3S(Szkolenie):

    def __init__(self, szkolenie, zadanie, tekst):
        super().__init__(szkolenie, zadanie)
        self.tekst = tekst
        self.tekst_bez_interpunkcji = None
        self.usun_interpunkcje()
        self.slowa = None
        self.podzial_tekstu()
        self.slownik = {}
        self.dodaj_do_slownika()
        self.wyswietl_slownik()

    def usun_interpunkcje(self):
        znaki = str.maketrans("", "", string.punctuation)
        self.tekst_bez_interpunkcji = self.tekst.translate(znaki)
        # print(self.tekst_bez_interpunkcji)

    def podzial_tekstu(self):
        self.slowa = self.tekst_bez_interpunkcji.lower().split()
        # print(self.slowa)

    def dodaj_do_slownika(self):
        for wyraz in self.slowa:
            self.slownik[wyraz] = self.slownik.get(wyraz, 0) + 1

    def wyswietl_slownik(self):
        for klucz, wartosc in self.slownik.items():
            print(f"{klucz}: {wartosc}")


class Zadanie4S(Szkolenie):

    def __init__(self, szkolenie, zadanie, slownik, tekst):
        super().__init__(szkolenie, zadanie)
        self.slownik = slownik
        self.tekst = tekst
        self.przeksztalc()

    def przeksztalc(self):
        for polska_nazwa, lacinska_nazwa in self.slownik.items():
            self.tekst = self.tekst.replace(polska_nazwa, f"{polska_nazwa} ({lacinska_nazwa})")
            # połączenie klucz wartosc w jednego stringa i podmienienie
        print(self.tekst)


class Zadanie5S(Szkolenie):

    def __init__(self, szkolenie, zadanie, n):
        super().__init__(szkolenie, zadanie)
        self.n = n
        self.slownik = {}
        self.generuj_slownik()
        # breakpoint()

    def generuj_slownik(self):
        for i in range(1, self.n + 1):
            self.slownik[i] = i * i


class Zadanie6S(Szkolenie):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.odpowiedz = "Obiekty modyfikowalne, takie jak listy czy słowniki, nie mogą być kluczami w słowniku,\n" \
                         "warto zauważyć, że krotki, które same zawierają obiekty modyfikowalne,\n" \
                         "również nie mogą być kluczami, ponieważ krotki są niemodyfikowalne,\n" \
                         "ale zawartość obiektów wewnątrz krotek może ulec zmianie."


class Zadanie7S(Szkolenie):

    def __init__(self, szkolenie, zadanie, slownik1, slownik2):
        super().__init__(szkolenie, zadanie)
        self.slownik1 = slownik1
        self.slownik2 = slownik2
        self.scalony_slownik = {}
        self.scal()

    def scal(self):
        self.scalony_slownik = self.slownik1 | self.slownik2


class Zadanie8S(Szkolenie):

    def __init__(self, szkolenie, zadanie, slownik):
        super().__init__(szkolenie, zadanie)
        self.slownik = slownik
        self.lista_unikalnych = []
        self.lista = []
        self.utworz_liste()
        self.utworz_liste_unikalnych()

    def utworz_liste(self):
        self.lista = list(self.slownik.values())

    def utworz_liste_unikalnych(self):
        self.lista_unikalnych = [wartosc for wartosc in set(self.lista) if self.lista.count(wartosc) == 1]
        # pętla przechodzi po wartości w wartości z set(self.lista)
        # z warunkime wystąpenia wartosc raz w liście self.lista
