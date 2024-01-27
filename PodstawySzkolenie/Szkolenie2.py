import random

from PodstawySzkolenie.Szkolenia import Szkolenia


class Szkolenie2(Szkolenia):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    def zad1(self, tekst):
        print(f"Wprowadzony tekst: \n"
              f"{tekst}")
        print(f"Liczba znaków w tekście: {len(tekst)}")
        print(f"Pierwszy znak w tekście: {tekst[0]}\n"
              f"Ostatni znak w tekście: {tekst[-1]}")
        losowa_liczba1, losowa_liczba2, losowa_liczba3 = random.sample(range(1, len(tekst)), k=3)
        print(f"Pierwszy dowolny znak: {tekst[losowa_liczba1]}")
        print(f"Pierwszy dowolny znak: {tekst[losowa_liczba2]}")
        print(f"Pierwszy dowolny znak: {tekst[losowa_liczba3]}")

    def zad2(self):
        try:
            ilosc_kotow = int(input("Ile kotów ma Ala? "))
        except ValueError:
            print("nie psuj!")
        print("Dziś ala znalazła jeszcze 3 koty pod blokiem")
        ilosc_kotow += 3
        print(f"Teraz Ala ma {ilosc_kotow} kotów")
        print(f"{', '.join(f'Teraz Ala ma {ilosc_kotow} kotów'.split())}")
        print('\n'.join(f'Teraz Ala ma {ilosc_kotow} kotów'.split()))
        if not f'teraz Ala ma {ilosc_kotow} kotów'.islower():
            print(f'teraz Ala ma {ilosc_kotow} kotów.'.lower())
        # zmieniłem pierwszą literę na małą i użyłem funkcji zmieniającej ją ne wielką o to chyba chodziło
        print(f'teraz Ala ma {ilosc_kotow} kotów'.capitalize())

    def zad3(self):
        print(f"{'DOM'.replace('DOM', 'domek')}")

    def zad4(self, slowo):
        return slowo.upper()

    def zad5(self, napis):
        return napis.lstrip()

    def zad6(self, kolory):
        # dlaczego nie działa bez tworzenia dodatkowej zmiennej
        rozdzielone_kolory = kolory.split(',')
        # print(rozdzielone_kolory)
        return rozdzielone_kolory[2]

