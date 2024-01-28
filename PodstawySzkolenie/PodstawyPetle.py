from PodstawySzkolenie.Szkolenie import Szkolenie


class Szkolenie4(Szkolenie):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    def zad1_while(self, y):
        x = 0
        print("Pętla while:")
        while y:
            print(x)
            x += 1
            y -= 1

    def zad1_for(self, y):
        print("Pętla for:")
        for x in range(0, y):
            print(x)

    def zad2_while(self, x, y):
        print("Pętla while:")
        while x >= y:
            print(x)
            x -= 1

    def zad2_for(self, x, y):
        print("Pętla for:")
        for i in range(x, y - 1, -1):
            print(i)

    def zad3(self, x, y):
        for i in range(x, y + 1, 5):
            print(i)

    def zad4(self, n):
        for i in range(n):
            print(2 ** i)

    def zad5(self, poczatek, koniec, dzielnik):
        for i in range(poczatek, koniec):
            if i % dzielnik == 0:
                print(i)

    def zad6_suma(self, suma, liczba):
        suma += liczba
        return suma

    def zad6_war(self, stara_liczba, liczba):
        if isinstance(stara_liczba, int) and stara_liczba > liczba:
            print("Program się zakończył")
            return False
        else:
            return True

    def zad7_a(self):
        print("*" * 10)

    def zad7_b(self, h):
        for i in range(h + 1):
            print("*" * i)

    def zad7_c(self, bok1, bok2):
        for i in range(bok2):
            print("*" * bok1)

    def zad7_d(self, h):
        j = h
        for i in range(h + 1):
            print(" " * j + "*" * (i * 2 - 1) + " " * j)
            j -= 1

    def zad7_d_center(self, h):
        for i in range(h + 1):
            print(("*" * (i * 2 - 1)).center(h * 2 - 1))

    def zad8_suma(self, liczby):
        suma = 0
        for i in range(liczby + 1):
            suma += i
        return suma

    def zad8_srednia(self, suma, liczby):
        return suma / liczby

    def zad9_paliwo(self, minimum, maximum, war):
        while war:
            try:
                poziom_paliwa = int(input("Podaj ilość paliwa z przedziału (5000, 30000): "))
                if maximum >= poziom_paliwa >= minimum:
                    war = False
                else:
                    print("Wartość z poza przedziału")
            except ValueError:
                print("Nie psuj!")
        return poziom_paliwa

    def zad9_astro(self, war, min_astro, max_astro):
        while war:
            try:
                ilosc_astronautow = int(input("Podaj liczbe astronautów z przedziału (1, 7): "))
                if max_astro >= ilosc_astronautow >= min_astro:
                    war = False
                else:
                    print("Wartość z poza przedziału")
            except ValueError:
                print("Nie psuj!")
        return ilosc_astronautow

    def zad9_lot(self, poziom_paliwa, ilosc_astro):
        dystans = 0
        while True:
            zuzycie_paliwa = 300 + 100 * ilosc_astro
            poziom_paliwa -= zuzycie_paliwa
            if poziom_paliwa < 0:
                break
            else:
                dystans += 100
                print(f"Przebyty dystans to: {dystans} km")
        return dystans

    def zad9_dolecial(self, dystans, odleglosc_orbity):
        if dystans > odleglosc_orbity:
            return "dotarł"
        else:
            return "nie dotarł"

    def zad10_liczba(self):
        try:
            liczba = int(input("Podaj liczbę: "))
        except ValueError:
            print("Nie psuj")
        return liczba

    def zad10_dzielniki(self, liczba):
        dzielniki = []
        for i in range(1, liczba):
            if liczba % i == 0:
                dzielniki.append(i)
        return dzielniki

    def zad10_doskonala(self, liczba, dzielniki):
        if sum(dzielniki) == liczba:
            return "Liczba jest doskonała"
        else:
            return "Liczba nie jest doskonała"

