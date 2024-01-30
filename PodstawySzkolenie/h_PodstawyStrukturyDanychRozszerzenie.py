import random

from PodstawySzkolenie.Szkolenie import Szkolenie


class Zadanie1PSDR(Szkolenie):
    """Zad 1.
        Utwórz dwie listy a i b. Sprawdź czy listy te mają chociaż jeden wspólny element.

    """

    def __init__(self, szkolenie, zadanie, napis1, napis2):
        super().__init__(szkolenie, zadanie)
        self.napis1 = napis1
        self.napis2 = napis2
        self.lista1 = self.utworz_liste(self.napis1)
        print(self.lista1)
        self.lista2 = self.utworz_liste(self.napis2)
        print(self.lista2)
        self.wspolny = self.czy_wspolny()
        self.wyswietl_odp()

    def utworz_liste(self, napis):
        lista = list(napis.split())
        return lista

    def czy_wspolny(self):
        czy_wspolny = any(element in self.lista1 for element in self.lista2)
        return czy_wspolny

    def wyswietl_odp(self):
        if self.czy_wspolny():
            print("Listy maja wspólny element")
        else:
            print("Listy nie mają wspólnego elementu")


class Zadanie2PSDR(Szkolenie):
    """
        Zad 2.
        Utwórz zbiór składający się z 15 losowo wygenerowanych wartości typu int z przedziału 5 - 120.
        Następnie usuń ze zbioru wszystkie liczby parzyste.
    """

    def __init__(self, szkolenie, zadanie, ile_elemetow, przedzial_min, przedzial_max):
        super().__init__(szkolenie, zadanie)
        self.przedzial_min = przedzial_min
        self.przedzial_max = przedzial_max
        self.ile_elementow = ile_elemetow
        self.zbior = self.utworz_zbior(self.ile_elementow)
        self.bez_parzystych = self.usun_parzyste()
        self.wyswietl()

    def utworz_zbior(self, i):
        zbior = set()
        war = True
        while war:
            zbior.add(self.wylosuj(self.przedzial_min, self.przedzial_max))
            if len(zbior) == i:
                war = False
        return zbior

    def wylosuj(self, przedzial_min, przedzial_max):
        wylosowana = random.randint(przedzial_min, przedzial_max)
        return wylosowana

    def usun_parzyste(self):
        nieparzyste = [liczba for liczba in self.zbior if liczba % 2 != 0]
        return nieparzyste

    def wyswietl(self):
        print(f"Zbiór {self.ile_elementow} wylosowanych liczb z przedziału "
              f"{self.przedzial_min} - {self.przedzial_max}: {self.zbior}")
        print(f"Zbiór z usuniętymi liczbami parzystymi: {self.bez_parzystych}")


class Zadanie3SPDR(Szkolenie):
    """Zad 3.
        Mając poniższy słownik:
        {‘a’ : 3, ‘b’ : 1, ‘c’ : 10, ‘d’ : 15, ‘e’ : 20}
        dokonaj jego odwrócenia, tzn. niech wartości staną się kluczami, a klucze wartościami.
        Dla powyższego przykładu poprawnym wynikiem będzie:
        {3 : ‘a’, 1 : ‘b’, 10 : ‘c’, 15 : ‘d’, 20 : ‘e’}
    """

    def __init__(self, szkolenie, zadanie, slownik):
        super().__init__(szkolenie, zadanie)
        self.slownik = slownik
        self.odwrocony = self.odwroc()
        self.wyswietl()

    def odwroc(self):
        nowy_slownik = {}
        for klucz, wartosc in self.slownik.items():
            nowy_slownik[wartosc] = klucz
        return nowy_slownik

    def wyswietl(self):
        print(f"Stary słownik: {self.slownik}")
        print(f"Nowy słownik: {self.odwrocony}")


class Zadanie4PSDR(Szkolenie):
    """Zad 4.
        Wyobraź sobie, że jesteś pogodynką i robisz zestawienie opadów deszczu na dany miesiąc.
        Problem polega jednak na tym, że dane miasta wraz z opadami są nieuporządkowane oraz użytkownik może
        wpisywać nieskończenie wiele par: miasto oraz opad aż do momentu podania pustej linii. Twoim zadaniem jest
        zinterpretowanie podanych danych wejściowych i podać wynik na wzór poniższego przykładu.

        Wejście:
        Boston 12
        Londyn 10
        Boston 12
        [pusta linia]

        Wyjście:
        Boston : 24
        Londyn : 10
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.slownik = {}
        self.wczytaj()
        self.wyswietl()

    def wczytaj(self):
        war = True
        while war:
            dane = input("Podaj parę miasto opad, enter zakończ: ")
            war = self.sprawdz_enter(dane)
            if not war:
                break
            self.rozdziel(dane)

    def sprawdz_enter(self, wpisano):
        if not wpisano.strip():
            return False
        else:
            return True

    def rozdziel(self, dane):
        rozdzielone = dane.split()
        miasto, opad = rozdzielone
        self.dodaj_slownik(miasto, opad)

    def dodaj_slownik(self, miasto, opad):
        self.slownik[miasto] = self.slownik.get(miasto, 0) + int(opad)
        # get(miasto, 0) sprawdza czy jest już taki element w słoniku

    def wyswietl(self):
        for klucz, wartosc in self.slownik.items():
            print(f"{klucz}: {wartosc}")


class Zadanie5PSDR(Szkolenie):
    """Zad 5.
        Program ma tworzyć rachunek za prestiżową kolację w restauracji dla poszczególnych osób.
    """

    def __init__(self, szkolenie, zadanie, lista):
        super().__init__(szkolenie, zadanie)
        self.cena = None
        self.potrawa = None
        self.osoba = None
        self.lista = lista
        self.rachunki = {}
        self.utworz_slownik()
        self.wyswietl()

    def utworz_slownik(self):
        for pozycja in self.lista:
            self.rozdziel_liste(pozycja)
            self.dodaj_osobe()
            self.rachunki[self.osoba]['potrawy'].append(self.potrawa)
            self.rachunki[self.osoba]["cena"] += self.cena

    def rozdziel_liste(self, pozycja):
        self.osoba, self.potrawa, self.cena = pozycja

    def dodaj_osobe(self):
        if self.osoba not in self.rachunki:
            self.rachunki[self.osoba] = {"potrawy": [], "cena": 0.0}

    def wyswietl(self):
        print(self.rachunki)


