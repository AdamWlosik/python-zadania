import random

from Szkolenie import Szkolenie


class Szkolenie2(Szkolenie):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    def zad1(self, tekst):
        """1. Program ma wykonać kilka operacji na pobranym od użytkownika dowolnym tekście (stringu),
            który ma co najmniej siedem znaków.
            Operacje te to:
            ●	wprowadzenie i wyświetlenie na ekranie tego tekstu
            ●	wyświetlenie liczby znaków, które on zawiera
            ●	wyświetlenie pierwszego i ostatniego znaku tego tekstu
            ●	wyświetlenie dowolnych 3 znaków z środka tego tekstu.
        """
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
        """2. Program ma (w zadaniach zastosuj nowy sposób formatowania tekstu f-string):
            ●	zapytać ile kotów ma Ala i pobrać od użytkownika tę liczbę
            ●	wyświetlić na ekranie zdanie:  ‘Dzisiaj Ala znalazła jeszcze 3 koty …’
                (zamiast kropek napisz od siebie gdzie je znalazła)
            ●	dodać 3 do wprowadzonej wcześniej liczby
            ●	wyświetlić na ekranie zdanie:  ‘Teraz Ala ma już … kotów’
                (w miejsce kropek wpisujecie obliczoną przez program prawidłową liczbę)
            ●	wyświetlić to zdanie tak, aby każde słowo było oddzielone przecinkiem
            ●	wyświetlić to zdanie tak, by każde słowo znajdowało się w osobnej linijce
            ●	sprawdzić, czy wszystkie litery są małe i jeśli nie, to zamienić je na małe (wyświetl  wynik tej zmiany)
            ●	zmień pierwszą literę zdania na wielką i wyświetl zdanie po tej modyfikacji.
        """
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
        """3. Zamień słowo DOM na domek"""
        print(f"{'DOM'.replace('DOM', 'domek')}")

    def zad4(self, slowo):
        """4. W dowolnym słowie podanym przez użytkownika zamień wszystkie litery na duże.  """
        return slowo.upper()

    def zad5(self, napis):
        """5. Pobierz od użytkownika dowolny napis zawierający 5 białych znaków (spacji) na początku, a następnie:
            ▪ wyświetl ten napis
            ▪ usuń wiodące białe znaki i wyświetl napis po tej zmianie
        """
        return napis.lstrip()

    def zad6(self, kolory):
        """6. Wprowadź jako jeden długi tekst 5 dowolnych kolorów rozdzielonych przecinkami.
            Następnie rozdziel wszystkie kolory na pojedyncze słowa. Wyświetl trzeci wprowadzony kolor. """
        # dlaczego nie działa bez tworzenia dodatkowej zmiennej
        rozdzielone_kolory = kolory.split(',')
        # print(rozdzielone_kolory)
        return rozdzielone_kolory[2]

