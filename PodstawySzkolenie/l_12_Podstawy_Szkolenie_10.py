from PodstawySzkolenie.Szkolenie import Szkolenie
from helpers import print_doc


class Zadanie1PS10(Szkolenie):
    """Zad 1.
        Stwórz klasę Shape i jej podklasę Square. Square ma posiadać konstruktor, który przyjmie length jako argument.
        Obie klasy mają posiadać metodę obliczającą pole figury. Domyślnie Shape ma zwracać wartość 0.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        square = Square(5)
        print("Pole kwadratu: ", square.calculate_area())


class Shape:

    def __init__(self):
        pass

    def calculate_area(self):
        return 0


class Square(Shape):
    def __init__(self, lenght):
        super().__init__()
        self.length = lenght

    def calculate_area(self):
        return self.length ** 2


class Zadanie2PS10(Szkolenie):
    """Zad 2.
        Zaprojektuj z użyciem koncepcji dziedziczenia hierarchię klas opisujących pojazdy komunikacji
        miejskiej. Wyraź w tej hierarchii następujące fakty:

        1. wszystkie pojazdy komunikacji miejskiej (k. m.) są pojazdami,
        2. komunikacja miejska używa tramwajów i autobusów,
        3. pojazdy są garażowane w zajezdniach, odpowiednio tramwajowych i autobusowych,
        4. każdy pojazd zna swoją szybkość maksymalną,
        5. każdy pojazd k. m. zna swój numer,
        6. każdy pojazd k. m. zna swoją zajezdnię,
        7. każdy tramwaj jest zestawem 1 do 3 wagonów (i wie, z ilu wagonów się składa),
        8. każdy autobus wie, ile zużył paliwa w bieżącym miesiącu,
        9. każda zajezdnia wie, jakie pojazdy do niej należą,
        10. każda zajezdnia ma nazwę.

        Każdy pojazd powinien mieć możliwość podawania swojego opisu w postaci napisu.
        Opis ma zawierać wszystkie informacje, które zna dany pojazd (np. numer, czy szybkość maksymalną).
        Opis zajezdni to nazwa zajezdni, jej typ i opisy poszczególnych pojazdów.
        Zajezdnia autobusowa podaje dodatkowo sumaryczne zużycie paliwa w bieżącym miesiącu,
        a tramwajowa ogólną liczbę wagonów.
        Do prezentowania informacji o obiekcie, wykorzystaj metodę specjalną __str__().

        Napisz program, który utworzy kilka obiektów reprezentujących wszystkie pojazdy i dwie zajezdnie
        (autobusową i tramwajową), przydzieli pojazdy do zajezdni, a następnie wypisze opis obu zajezdni.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        tramwaj1 = Tramwaj(100, 1, 3)
        tramwaj2 = Tramwaj(96, 2, 1)
        tramwaj3 = Tramwaj(85, 3, 2)
        autobus1 = Autobus(50, 1, 200)
        autobus2 = Autobus(50, 2, 220)
        autobus3 = Autobus(50, 3, 250)
        zajezdnia_autobusowa = ZajezdniaAutobusowa("Zajezdnia Autobusowa")
        zajezdnia_autobusowa.dodaj_pojazd(autobus1)
        zajezdnia_autobusowa.dodaj_pojazd(autobus2)
        zajezdnia_autobusowa.dodaj_pojazd(autobus3)
        print(zajezdnia_autobusowa)
        zajezdnia_tramwajowa = ZajezdniaTramwajowa("Zajezdnia Tramwajowa")
        zajezdnia_tramwajowa.dodaj_poojazd(tramwaj1)
        zajezdnia_tramwajowa.dodaj_poojazd(tramwaj2)
        zajezdnia_tramwajowa.dodaj_poojazd(tramwaj3)
        print(zajezdnia_tramwajowa)


class Pojazdy:

    def __init__(self, szybkosz_maksymalna):
        self.szybkosc_maksymalna = szybkosz_maksymalna


class Zajezdnia:

    def __init__(self, nazwa):
        self.nazwa = nazwa


class ZajezdniaTramwajowa(Zajezdnia):

    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.pojazdy = []


    def dodaj_poojazd(self, pojazd):
        self.pojazdy.append(pojazd)

    def sumuj_wagony(self):
        suma_wagonow = sum(pojazd.ilosc_wagonow for pojazd in self.pojazdy if isinstance(pojazd, Tramwaj))
        return suma_wagonow

    def __str__(self):
        opis_pojazdow = [str(pojazd) for pojazd in self.pojazdy]
        return (f"Nazwa zajezdni: {self.nazwa}, Typ: {type(self).__name__}, "
                f"Opis pojazdów: {', '.join(opis_pojazdow)}, \nSumaryczne zużycie paliwa: {self.sumuj_wagony()}")


class ZajezdniaAutobusowa(Zajezdnia):

    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.pojazdy = []

    def dodaj_pojazd(self, pojazd):
        self.pojazdy.append(pojazd)

    def sumuj_paliwo(self):
        suma_paliwa = sum(pojazd.zuzycie_paliwa for pojazd in self.pojazdy if isinstance(pojazd, Autobus))
        return suma_paliwa

    def __str__(self):
        opis_pojazdow = [str(pojazd) for pojazd in self.pojazdy]
        # zmienia w druk z domyślnego obiektu klasy na czytelnego str
        return (f"Nazwa zajezdni: {self.nazwa}, Typ: {type(self).__name__}, "
                f"Opis pojazdów: {', '.join(opis_pojazdow)}, \nSumaryczne zużycie paliwa: {self.sumuj_paliwo()}")


class KompnikacjaMiejska(Pojazdy):

    def __init__(self, szybkosc_maksymalna, numer):
        super().__init__(szybkosc_maksymalna)
        self.numer = numer


class Autobus(KompnikacjaMiejska):

    def __init__(self, szybkosc_maksymalna, numer, zuzycie_paliwa):
        super().__init__(szybkosc_maksymalna, numer)
        self.zuzycie_paliwa = zuzycie_paliwa

    def __str__(self):
        return (f"\n Pojazd: {type(self).__name__}, Szybkość maksymalna: {self.szybkosc_maksymalna}, "
                f"Numer: {self.numer}, Zużycie paliwa: {self.zuzycie_paliwa}")


class Tramwaj(KompnikacjaMiejska):

    def __init__(self, szybkosc_maksymalna, numer, ilosc_wagonow):
        super().__init__(szybkosc_maksymalna, numer)
        self.ilosc_wagonow = ilosc_wagonow

    def __str__(self):
        return (f"\n Pojazd: {type(self).__name__}, Szybkość maksymalna: {self.szybkosc_maksymalna}, "
                f"Numer: {self.numer}, Ilość wagonów: {self.ilosc_wagonow}")
