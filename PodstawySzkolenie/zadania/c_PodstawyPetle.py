from PodstawySzkolenie.Szkolenie import Szkolenie


class Szkolenie4(Szkolenie):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    def zad1_while(self, y):
        """Zad. 1
            Napisz program wyświetlający liczby całkowite z przedziału <0; y>,
            gdzie y podaje użytkownik. Wykonaj to na pętli for i while.
        """
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
        """Zad. 2
            Napisz program wyświetlający liczby całkowite z przedziału <100; 50>
            w porządku malejącym. Wykonaj to na pętli for i while.
        """
        print("Pętla while:")
        while x >= y:
            print(x)
            x -= 1

    def zad2_for(self, x, y):
        print("Pętla for:")
        for i in range(x, y - 1, -1):
            print(i)

    def zad3(self, x, y):
        """Zad. 3
            Napisz program wyświetlający liczby z przedziału <0, 5, 10, 15, …, 100>
        """
        for i in range(x, y + 1, 5):
            print(i)

    def zad4(self, n):
        """Zad. 4
            Napisz program, wyświetlający n kolejnych potęg liczby 2. Wartość n podaje użytkownik.
        """
        for i in range(n):
            print(2 ** i)

    def zad5(self, poczatek, koniec, dzielnik):
        """Zad. 5
            Napisz program, który wyświetli liczby z przedziału <50; 100> podzielne przez całkowitą liczbę k,
            którą podaje użytkownik. Przekształć program tak, aby przedział podawał również użytkownik.
        """
        for i in range(poczatek, koniec):
            if i % dzielnik == 0:
                print(i)

    def zad6_suma(self, suma, liczba):
        """Zad. 6
            Zadanie polega na napisaniu programu, który będzie sumować liczby całkowite wpisane przez użytkownika
            tak długo, aż po wczytaniu poprzedniej liczby suma zwiększyła się. Na koniec program wypisuje ostateczną
            sumę Początkowo suma wynosi 0. Zastosuj do tego rozwiązania pętlę while.
            Przykład:
            Użytkownik przykładowo wprowadza kolejno liczby 1, 2, 3, 0 wtedy zwrócona suma to 1 + 2 + 3 + 0 = 6.
            Z kolei dla liczb 1, 9, 2, -12 suma wyniesie 0.
        """
        suma += liczba
        return suma

    def zad6_war(self, stara_liczba, liczba):
        if isinstance(stara_liczba, int) and stara_liczba > liczba:
            print("Program się zakończył")
            return False
        else:
            return True

    def zad7_a(self):
        """
            Zad. 7
            Narysuj poniższe kształty:

            a)	szlaczek o długości 10
            **********
            b)	trójkąt prostokątny o wysokości 4
            *
            **
            ***
            ****
                  c) kwadrat o wymiarach 3 x 3
            ***
            ***
            ***
               d) choinkę o wysokości 5*;
                  *
                 ***
                *****
               *******
              *********

            Podpowiedź: wykorzystaj metodę center() https://www.w3schools.com/python/ref_string_center.asp

            """
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
        """Zad. 8
            Wypisz wartość średniej arytmetycznej pierwszych 10 liczb naturalnych.
        """
        suma = 0
        for i in range(liczby + 1):
            suma += i
        return suma

    def zad8_srednia(self, suma, liczby):
        return suma / liczby

    def zad9_paliwo(self, minimum, maximum, war):
        """Zad. 9
            Zadeklaruj trzy zmienne - pierwszą przechowującą informację o startowym poziomie paliwa,
            drugą określającą ilość astronautów na pokładzie, a trzecią mówiącą,
            na jakiej wysokości znajduje się rakieta.

            1.	Poproś użytkownika o podanie początkowego poziomu paliwa. Użytkownik ma kontynuować czynność,
             dopóki nie poda poprawnej wartości - mieszczącej się pomiędzy 5000 a 30000 litrów.
            2.	Stwórz drugą pętlę, która będzie prosić o użytkownika o podanie odpowiedniej ilości astronautów
             znajdujących na pokładzie. Pętla ma walidować podaną liczbę - tak, aby była dodatnia i nie większa niż 7.
            3.	Zasymuluj pętlą nr 3 lot statku kosmicznego. Kolejne iteracje mają zmniejszać obecny poziom paliwa
            o określoną wartość. Zużycie paliwa co 100 km zależy od ilości astronautów na pokładzie
             i jest równe: 300 l + 100 * ilosc_astronautow.

            Pętla więc ma uruchamiać się co 100 km i wykonać tyle iteracji, na ile wystarczy paliwa.
             Co każdą iterację ma wyświetlać się aktualnie przebyty dystans przez statek kosmiczny.

            4.	Po wykonaniu się pętli, powinien wyświetlić się komunikat: “Statek kosmiczny dotarł do orbity”,
             jeżeli przebyta odległość jest większa niż 2000 km lub w przypadku mniejszej odległości
             - “Statek kosmiczny nie dotarł do orbity”.

            """
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
        """Zad. 10*
            Sprawdzanie, czy liczba jest doskonała.
            Napisz program, który sprawdzi, czy podana przez usera liczba jest doskonała. Liczba doskonała, to taka liczba, która jest sumą wszystkich swoich dzielników właściwych (czyli mniejszych od niej samej).
            Przykłady liczb doskonałych: 6 (6 = 1 + 2 + 3), 28, 496, 8128.

            Podpowiedź:
            Wykorzystaj instrukcje warunkowe i modulo (%)

        """
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

