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
        for i in range(x, y-1, -1):
            print(i)

    def zad3(self, x, y):
        for i in range(x, y+1, 5):
            print(i)

    def zad4(self, n):
        for i in range(n):
            print(2 ** i)

    def zad5(self, poczatek, koniec, dzielnik):
        for i in range(poczatek, koniec):
            if i % dzielnik == 0:
                print(i)


