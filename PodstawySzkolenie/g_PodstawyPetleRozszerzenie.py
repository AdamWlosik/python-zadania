import string

from PodstawySzkolenie.Szkolenie import Szkolenie


class Zadanie1PPR(Szkolenie):
    """Zad 1.
        Napisz program wydrukowywujący poniższy wzór:

        *
        * *
        * * *
        * * * *
        * * * * *
        * * * *
        * * *
        * *
        *
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.wydrukuj()

    def wydrukuj(self):
        for i in range(1, 6):
            print("*" * i)
            if i == 5:
                for i in range(4, 0, -1):
                    print("*" * i)
                i = 6


class Zadanie2PPR(Szkolenie):
    """Zad 2.
        Napisz program, sprawdzający czy dany wyraz jest palindromem
        (jest czytany tak samo od przodu i tyłu), np. sedes, Anna.
    """

    def __init__(self, szkolenie, zadanie, wyraz):
        super().__init__(szkolenie, zadanie)
        self.wyraz = wyraz
        self.male_litery = self.zmniejsz()
        self.obrocony_wyraz = self.obroc()
        self.porownaj()

    def zmniejsz(self):
        nowy_wyraz = self.wyraz.lower()
        return nowy_wyraz

    def obroc(self):
        nowy_wyraz = self.male_litery[::-1]
        return nowy_wyraz

    def porownaj(self):
        if self.male_litery == self.obrocony_wyraz:
            print(f"{self.wyraz} jest palindromem")
        else:
            print(f"{self.wyraz} nie jest palindromem")


class Zadanie3PPR(Szkolenie):
    """Zad 3.
        W trakcie Wigilii Bożego Narodzenia, pięciu członków rodziny: Adam, Stanisław, Joanna, Kornelia i Kacper
        składają sobie życzenia. Stwórz program, który wyświetli wszystkie możliwe połączenia między członkami rodzin,
        jakie mogą zajść w trakcie składania sobie życzeń, np. Adam - Stanisław, Adam - Joanna, Adam - Kornelia,
        Adam - Kacper itd.
    """

    def __init__(self, szkolenie, zadanie, osoby):
        super().__init__(szkolenie, zadanie)
        self.osoby = osoby
        self.bez_interpunkcji = self.usun_interpunkcje()
        self.lista = self.utworz_liste()
        self.wyswietl_zyczenia()

    def usun_interpunkcje(self):
        translator = str.maketrans("", "", string.punctuation)
        bez_interpunkcji = self.osoby.translate(translator)
        return bez_interpunkcji

    def utworz_liste(self):
        lista = list(self.bez_interpunkcji.split())
        return lista

    def wyswietl_zyczenia(self):
        for osoba1 in self.lista:
            for osoba2 in self.lista:
                print(f"{osoba1} - {osoba2}")




