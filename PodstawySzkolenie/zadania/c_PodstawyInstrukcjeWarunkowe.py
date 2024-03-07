import random
import time

from PodstawySzkolenie.Szkolenie import Szkolenie


class Szkolenie3(Szkolenie):

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    def zad1(self, bok1, bok2, bok3):
        """Zad 1.
        Poproś użytkownika o podanie 3 dowolnych długości boków trójkąta. Sprawdź,
        czy jest to trójkąt prostokątny (wykorzystaj własność trójkąta prostokątnego,
        która mówi że suma kwadratów dwóch dowolnych boków jest równa kwadratowi długości trzeciego).
        """
        if bok1 + bok2 == bok3**2:
            print("Trójkąt prostokątny")
        else:
            print("To nie jest trójkąt prostokątny")

    def zad2(self, liczba):
        """Zad 2.
        Napisz program sprawdzający, czy podana przez użytkownika jest ujemna, dodatnia lub czy ma wartość równą 0.
        """
        if liczba < 0:
            return "ujemna"
        elif liczba > 0:
            return "dodatnia"
        elif liczba == 0:
            return "zero"

    def zad3(self, liczby):
        """Zad 3.
        Pobierz od użytkownika 3 liczby i wyświetl największą z nich.
        """
        max_liczba = max(liczby)
        return max_liczba

    def zad4(self, slowo1, slowo2):
        """Zad 4.
        Zasymuluj grę w papier, kamień, nożyce. Oczywiście będzie to uproszczona wersja, ponieważ będzie zapewniała
        wprowadzenie danych tylko jednorazowo. Pobierz od użytkownika numer 1 słowo spośród: "kamień", "papier",
        "nożyce", operację przeprowadź również dla użytkownika numer 2. Następnie wyświetl,
        który z użytkowników wygrał to jednorazowe starcie (pamiętaj o tym, który przedmiot
        jest w grze "silniejszy" od drugiego). Dodatkowo zabezpiecz program przed wprowadzeniem
        nieprawidłowych danych, czyli jeżeli użytkownik nie wprowadzi ani "kamień", ani "papier",
        ani "nożyce" program ma natychmiastowo przerwać działanie i wyświetlić komunikat: "Błędne dane!".
        """
        if slowo1 == slowo2:
            print("Remis!")
        elif (
            (slowo1 == "kamień" and slowo2 == "nożyce")
            or (slowo1 == "papier" and slowo2 == "kamień")
            or (slowo1 == "nożyce" and slowo2 == "papier")
        ):
            print("Wygrywa gracz numer 1!")
        else:
            print("Wygrywa gracz numer 2!")

    def zad5(self, liczby):
        """Zad 5.
        Napisz program pobierający od użytkownika 2 liczby. Sprawdź, czy co najmniej 1 z nich jest parzysta.
        """
        czy_parzysta = False
        for libcza in liczby:
            if libcza % 2 == 0:
                print(f"liczba {libcza} jest liczbą parzystą")
                czy_parzysta = True
        if not czy_parzysta:
            print("Brak liczb parzystych")

    def zad6_losowanie(self, opcje):
        """Zad 6.
        1. Użytkownik wybiera czy obstawia reszkę, czy orła (literka r – reszka,
        literka o – orzeł)
        2. Po dokonaniu wyboru, Komputer odlicza 3,2,1, a następnie dokonuje
        'rzutu', czyli losowego wyboru orzeł / reszka.
        3. Komputer wyświetla wynik rzutu.
        4. Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli
        komputer to dodaje punkt dla komputera.
        Podpowiedź:
        W celu losowania wartości wykorzystaj metodę randint() (pamiętaj o linijce import
        random na samej górze programu) i przypisz konkretne liczby do orła/reszki.
        Przykład:
        import random
        print(random.randint(0, 5)) # wyświetlanie wartości z przedziału [0; 5]
        print(random.randint(10, 12)) # wyświetlanie wartości z przedziału [10; 12]
        """
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
