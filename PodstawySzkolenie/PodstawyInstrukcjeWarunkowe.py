import random
import time

from PodstawySzkolenie.Szkolenie import Szkolenie


class Szkolenie3(Szkolenie):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    def zad1(self, bok1, bok2, bok3):
        if bok1 + bok2 == bok3 ** 2:
            print("Trójkąt prostokątny")
        else:
            print("To nie jest trójkąt prostokątny")

    def zad2(self, liczba):
        if liczba < 0:
            return "ujemna"
        elif liczba > 0:
            return "dodatnia"
        elif liczba == 0:
            return "zero"

    def zad3(self, liczby):
        max_liczba = max(liczby)
        return max_liczba

    def zad4(self, slowo1, slowo2):
        if slowo1 == slowo2:
            print("Remis!")
        elif ((slowo1 == "kamień" and slowo2 == "nożyce") or
              (slowo1 == "papier" and slowo2 == "kamień") or
              (slowo1 == "nożyce" and slowo2 == "papier")):
            print("Wygrywa gracz numer 1!")
        else:
            print("Wygrywa gracz numer 2!")

    def zad5(self, liczby):
        czy_parzysta = False
        for libcza in liczby:
            if libcza % 2 == 0:
                print(f"liczba {libcza} jest liczbą parzystą")
                czy_parzysta = True
        if not czy_parzysta:
            print("Brak liczb parzystych")

    def zad6_losowanie(self, opcje):
        for i in range(3, 0, -1):
            time.sleep(0.5)
            print(f"{i}")
        wylosowano = random.choice(opcje)
        if wylosowano == "r":
            print("reszka")
        else:
            print("orzeł")
        return wylosowano

    def zad6_punktacja(self, wylosowano, wybor, punkty_gracza, punkty_komputera):
        if wybor == wylosowano:
            punkty_gracza += 1
        else:
            punkty_komputera += 1
        return punkty_gracza, punkty_komputera
