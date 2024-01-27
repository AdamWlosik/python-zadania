class Szkolenie1:
    def __init__(self, szkolenie, zadanie):
        self.szkolenie = szkolenie
        self.zadanie = zadanie
        self.tytul()

    def tytul(self):
        print(f"Wybrałeś szkolenie: {self.szkolenie} i zadanie: {self.zadanie}: ")

    # może to być metoda @staticmethod bo nie korzysta z konstruktów klasy więc niepotrzebne jest tworzenie
    # instancji klasy do skorzystania z niej ale już tak zostawiłem
    def zad1(self):
        return "print(), input(), def()"

    def zad2(self):
        print("Konkatencja stringów to operacja ich łączenia")
        print(f"1 + 1 = {1 + 1} MOŻLIWE")
        print('"str" + 1 = TypeError: can only concatenate str (not "int") to str,  NIEMOŻLIWE')
        print('"str" + " " + "str" = "str str" MOŻLIWE')

    def zad3(self, liczba1, liczba2):
        wynik = liczba1 + liczba2
        return wynik

    def zad4(self):
        print("Niepoprawne nazwy zmiennych to: \n"
              "czy LubiPsy \n"
              "Poprawne, nie wyrzucające błędy ale nie zalecane: \n"
              "zmienna, płeć, WartoscLiczbowa")

    def zad5(self, zmienne):
        for zmienna in zmienne:
            print(f"zmienna {zmienna} jest typu {type(zmienna)}")

    def zad6(self):
        print("Nieprawidłowe odpowiedniki: \n"
              "a -= 5 --> a = 5 - a, poprawne a -=5 --> a = a - 5 \n"
              "a /= 5 --> a = 5/a, poprawne a /= 5 --> a = a/5")

    def zad7(self, wzrost, waga):
        return waga / wzrost ** 2

    def zad8(self, dzialanie, zmienna1, zmienna2):
        if dzialanie == "dzielenie":
            try:
                wynik = zmienna1 / zmienna2
                print(f"{zmienna1} / {zmienna2} = {wynik}, jest on typu: {type(wynik)}")
            except ZeroDivisionError:
                print("Nie dziel przez 0")
            except TypeError:
                print(f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}")
        elif dzialanie == "dodawanie":
            try:
                wynik = zmienna1 + zmienna2
                print(f"{zmienna1} + {zmienna2} = {wynik}, jest on typu: {type(wynik)}")
            except TypeError:
                print(f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}")
        elif dzialanie == "modulo":
            try:
                wynik = zmienna1 % zmienna2
                print(f"{zmienna1} % {zmienna2} = {wynik}, jest on typu: {type(wynik)}")
            except TypeError:
                print(f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}")
        elif dzialanie == "dzielenie calkowite":
            try:
                wynik = zmienna1 // zmienna2
                print(f"{zmienna1} // {zmienna2} = {wynik}, jest on typu: {type(wynik)}")
            except ZeroDivisionError:
                print("Nie dziel przez 0")
            except TypeError:
                print(f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}")
        elif dzialanie == "potegowanie":
            try:
                wynik = zmienna1 ** zmienna2
                print(f"{zmienna1} ** {zmienna2} = {wynik}, jest on typu: {type(wynik)}")
            except TypeError:
                print(f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}")

    def zad9(self, napis):
        if len(napis) >= 2:
            napis = napis[-1] + napis[1:-1] + napis[0]
        else:
            print("Napis powinien zawierać conajmniej dwie litery")
        return napis

    def zad10(self, zmienna1, zmienna2):
        zmienna1 = str(zmienna1)
        zmienna2 = str(zmienna2)
        return zmienna1 + zmienna2

    def zad11(self, imie1, imie2):
        imie3 = imie1[: - (len(imie1) // 2)] + imie2[- len(imie2) // 2:]
        return imie3

    def zad12(self):
        print("Zapis tekst1 = tekst2[:] oznacza, że tekst1 stanie się kopią zawartości tekst2 \n"
              "dzięki temu stworzymy nowy obiekt tekst1, który ma taką zawartość jak tekst2 \n"
              "ale nie będzie on tym samym obiektem więc edycja jednego z nich nie bedzie wpływać na drugi")

    def zad13(self):
        print("Jest wiele powodów, dla których używamy kodów ascii oto kilka z nich: \n"
              "Każdy znak w kodzie ascii ma przypisana wartość liczbową co umożliwia komputerom przechowywanie, "
              "przesyłanie i przetwarzanie tekstu. \n"
              "Jako, że kody ascii sa uniwersalne pozwalaną na komunikacje między systemami \n"
              "Są wykorzystywane do reprezentacji kalwiszy na klawiaturze i innych urządzeń wejścia \n"
              "Są wykorzystywane do porównywania, sortowania manipolowania tekstem \n"
              "Są wykorzystywane do kodowania np protokół HTTP ")

    def zad14(self):
        # używając zad14.txt zamiast pełnej ścieżki błąd
        # FileNotFoundError: [Errno 2] No such file or directory: 'zad14.txt'
        with open("C:\\Users\\adamw\\OneDrive\\Pulpit\\Mentoring\\python-zadania\\PodstawySzkolenie\\zad14.txt",
                  encoding="utf-8") as plik:
            for line in plik.readlines():
                print(line, end="")

