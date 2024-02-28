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


class Zadanie4PPR(Szkolenie):
    """Zad 4.
    Napisz program generujący wszystkie możliwe kombinacje liczb 4-cyfrowych,
    np. 1000, 1001, 1002, ..., 9999.
    """

    def __init__(self, szkolenie, zadanie, zakres_min, zakres_max):
        super().__init__(szkolenie, zadanie)
        self.generuj()
        self.zakres_min = zakres_min
        self.zakres_max = zakres_max

    def generuj(self):
        for i in range(self.zakres_min, self.zakres_max):
            print(i)


class Zadanie5PPR(Szkolenie):
    """Zad 5.
    Stwórz następującą strukturę danych (słownik):
    zamowienia = {"Klient_1335" : {"nazwa_potrawy" : "rosół", "ocena" : 5, "rachunek" : 20.0}, "Klient_222"
    {"nazwa_deseru” : "lody waniliowe", "rachunek" : 5.0 }}
    Następnie wyświetl nazwy wszystkich klientów i dla każdego z nich stwórz podsumowanie zamówienia:
    """

    def __init__(self, szkolenie, zadanie, zamowienia):
        super().__init__(szkolenie, zadanie)
        self.zamowienia = zamowienia
        self.wyswietl()

    def wyswietl(self):
        for klient, szczegoly in self.zamowienia.items():
            print(f"Klient: {klient}")
            for klucz, wartosc in szczegoly.items():
                print(f"{klucz}: {wartosc}")
            print("-" * 50)


class Zadanie6PPR(Szkolenie):
    """Zad 6.
    Stwórz program, który policzy częstotliwość cyfr w danej liczbie (którą poda użytkownik).
    Przykład:
    Input: 1235555
    Output:
    1: 1
    2: 1
    3: 1
    5: 4

    Podpowiedź:
    Aby łatwo przechodzić po wszystkich cyfrach w liczbie, przekonwertuj ją na typ str.
     Częstotliwość występowania danych cyfr możesz przechowywać wewnątrz słownika.
    """

    def __init__(self, szkolenie, zadanie, liczba):
        super().__init__(szkolenie, zadanie)
        self.liczba = liczba
        self.liczba_str = self.konwertuj_str()
        self.wystepowanie = self.zlicz()
        self.wyswietl()

    def konwertuj_str(self):
        napis = str(self.liczba)
        return napis

    def zlicz(self):
        wystepowanie = {}
        for cyfra in self.liczba_str:
            wystepowanie[cyfra] = wystepowanie.get(cyfra, 0) + 1
        return wystepowanie

    def wyswietl(self):
        for cyfra, ilosc in self.wystepowanie.items():
            print(f"{cyfra}: {ilosc}")


class Zadanie7PPR(Szkolenie):
    """
    Zad 7.
    Napisz program wyznaczający n (podawane przez użytkownika)
    pierwszych liczb ciągu Fibonacciego. Przykład:
    dla n = 5
    0, 1, 1, 2, 3, 5
    """

    def __init__(self, szkolenie, zadanie, n, fibo):
        super().__init__(szkolenie, zadanie)
        self.n = n
        self.fibo = fibo
        self.fibonacci = self.oblicz_fibo()
        self.wyswietl()

    def oblicz_fibo(self):
        fibo = self.fibo
        while len(fibo) < self.n:
            fibo.append(fibo[-1] + fibo[-2])
        return fibo

    def wyswietl(self):
        print(f"{self.n} pierwszych liczb ciągu Fibonacciego: ")
        print(", ".join(map(str, self.fibonacci)))
