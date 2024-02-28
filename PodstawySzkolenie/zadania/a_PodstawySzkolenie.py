from PodstawySzkolenie.Szkolenie import Szkolenie


class Szkolenie1(Szkolenie):
    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    # może to być metoda @staticmethod bo nie korzysta z konstruktów klasy więc niepotrzebne jest tworzenie
    # instancji klasy do skorzystania z niej ale już tak zostawiłem
    def zad1(self):
        """🗒️   Zad. 1
        Na podstawie poznanych poleceń, wskaż dowolne, które mogłyby świadczyć o tym,
        że Python jest wysokopoziomowym językiem programowania.
        """
        return "print(), input(), def()"

    def zad2(self):
        """Zad. 2
        Czym jest konkatenacja stringów? Która z poniższych operacji jest możliwa?
        1 + 1; “str” + 1; “str” + “ “ + “str”
        """
        print("Konkatencja stringów to operacja ich łączenia")
        print(f"1 + 1 = {1 + 1} MOŻLIWE")
        print(
            '"str" + 1 = TypeError: can only concatenate str (not "int") to str,  NIEMOŻLIWE'
        )
        print('"str" + " " + "str" = "str str" MOŻLIWE')

    def zad3(self, liczba1, liczba2):
        """Zad. 3
        Czy poniższe operacje są poprawne i mają sens?

        Jaki będzie output na ekranie?
        """
        wynik = liczba1 + liczba2
        return wynik

    def zad4(self):
        """Zad. 4
        Wskaż nieprawidłowo nazwane zmienne:
        nazwa_psa = “Reksio”, nazwaKota = “Filemon”, zmienna = “Devs-Mentoring”, płeć = “mężczyzna”,
        WartoscLiczbowa = 5, czyZonaty = False,
        czy LubiPsy = False
        """
        print(
            "Niepoprawne nazwy zmiennych to: \n"
            "czy LubiPsy \n"
            "Poprawne, nie wyrzucające błędy ale nie zalecane: \n"
            "zmienna, płeć, WartoscLiczbowa"
        )

    def zad5(self, zmienne):
        """Zad. 5
        Jakiego typu są poniższe zmienne: (w celu uproszczenia, zastosowano tę samą nazwę zmiennej)
        z = 5, z = -1, z = 0, z = 0.0, z = -1.123, z = “c”, z = ‘c’, z = “programowanie”, z = False, z = True
        """
        for zmienna in zmienne:
            print(f"zmienna {zmienna} jest typu {type(zmienna)}")

    def zad6(self):
        """Wskaż nieprawidłowe odpowiedniki dla operatorów przypisania:
        a += 5 -–> a = a + 5
        a -= 5 -–> a = 5 – a
        a *= 5 -–> a = 5 * a
        a*= 5 -–> a = a * 5
        a /= 5 --> a = 5/a
        """
        print(
            "Nieprawidłowe odpowiedniki: \n"
            "a -= 5 --> a = 5 - a, poprawne a -=5 --> a = a - 5 \n"
            "a /= 5 --> a = 5/a, poprawne a /= 5 --> a = a/5"
        )

    def zad7(self, wzrost, waga):
        """Zad. 7
        Utwórz w programie zmienne przechowujące Twój wzrost oraz wiek. Zapytaj użytkownika o jego wagę i wzrost.
        Następnie na podstawie tych informacji oblicz wartość BMI i umieść ją w zmiennej o etykiecie bmi.
        Wyświetl wartość obliczonego BMI.
        Wzór na BMI: bmi = waga / wzrost^2 (wzrost ^2 to proces potęgowania)
        """
        return waga / wzrost**2

    def zad8(self, dzialanie, zmienna1, zmienna2):
        """Jaki będzie wynik operacji i jakiego będzie on typu:
        5 / 2; 1 + 1; 1.0 + 1; 2.0 + 2.0; “napis” + 1; “napis” + “napis”; True + True;
        5 % 2; 10 % 2; 20 % 30; 100 % 3;
        100 // 3; 5 // 3; 1 // 3
        3**3; 2**2; 2**0
        """
        if dzialanie == "dzielenie":
            try:
                wynik = zmienna1 / zmienna2
                print(f"{zmienna1} / {zmienna2} = {wynik}, jest on typu: {type(wynik)}")
            except ZeroDivisionError:
                print("Nie dziel przez 0")
            except TypeError:
                print(
                    f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}"
                )
        elif dzialanie == "dodawanie":
            try:
                wynik = zmienna1 + zmienna2
                print(f"{zmienna1} + {zmienna2} = {wynik}, jest on typu: {type(wynik)}")
            except TypeError:
                print(
                    f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}"
                )
        elif dzialanie == "modulo":
            try:
                wynik = zmienna1 % zmienna2
                print(f"{zmienna1} % {zmienna2} = {wynik}, jest on typu: {type(wynik)}")
            except TypeError:
                print(
                    f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}"
                )
        elif dzialanie == "dzielenie calkowite":
            try:
                wynik = zmienna1 // zmienna2
                print(
                    f"{zmienna1} // {zmienna2} = {wynik}, jest on typu: {type(wynik)}"
                )
            except ZeroDivisionError:
                print("Nie dziel przez 0")
            except TypeError:
                print(
                    f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}"
                )
        elif dzialanie == "potegowanie":
            try:
                wynik = zmienna1**zmienna2
                print(
                    f"{zmienna1} ** {zmienna2} = {wynik}, jest on typu: {type(wynik)}"
                )
            except TypeError:
                print(
                    f"nie można wykonać działania {dzialanie} na zmiennych {zmienna1} i {zmienna2}"
                )

    def zad9(self, napis):
        """Zad. 9
        Korzystając z funkcji input(), pobierz dowolny napis od użytkownika. Następnie utwórz nowy
        string z zamienioną pierwszą literą z ostatnią i wyświetl efekt na ekranie, np.
        > Użytkownik wprowadził wyraz “Hello world!”
        > Program wydrukuje na ekranie nowy napis: “dello worlH!”

        Podpowiedź:
        Spróbuj wykonać tę operację, działając jedynie na oryginalnym napisie. Czy jest to możliwe?
        """
        if len(napis) >= 2:
            napis = napis[-1] + napis[1:-1] + napis[0]
        else:
            print("Napis powinien zawierać conajmniej dwie litery")
        return napis

    def zad10(self, zmienna1, zmienna2):
        """Zad. 10
        Mamy w programie zdefiniowane następujące zmienne:
        a = 5
        b = 6

        Jak wiesz, jest to typ całkowity (int). Spróbuj przekonwertować (konwertowaliśmy już str na typ int,
        jak to zrobić na odwrót?) te wartości na typ str i następnie dokonaj konkatenacji stringów.
        Efektem powinien być napis: “56”.
        """
        zmienna1 = str(zmienna1)
        zmienna2 = str(zmienna2)
        return zmienna1 + zmienna2

    def zad11(self, imie1, imie2):
        """Zad. 11
        Utwórz dwa dowolne stringi o różnych wartościach. Utwórz trzeci napis, który będzie się składał
        z pierwszej połówki pierwszego napisu oraz drugiej połówki drugiego napisu.
        Skorzystaj z ujemnych indeksów.
        imie1 = “Kacper”
        imie2 = “Lucjan”
        imie3 = “Kacjan”
        """
        imie3 = imie1[: -(len(imie1) // 2)] + imie2[-len(imie2) // 2 :]  # noqa E203
        return imie3

    def zad12(self):
        """Zad. 12
        Co oznacza zapis tekst1 = tekst2[:]?
        """
        print(
            "Zapis tekst1 = tekst2[:] oznacza, że tekst1 stanie się kopią zawartości tekst2 \n"
            "dzięki temu stworzymy nowy obiekt tekst1, który ma taką zawartość jak tekst2 \n"
            "ale nie będzie on tym samym obiektem więc edycja jednego z nich nie bedzie wpływać na drugi"
        )

    def zad13(self):
        """Zad. 13
        Dlaczego w programowaniu istnieje konieczność korzystania z tzw. kodów ASCII?
        """
        print(
            "Jest wiele powodów, dla których używamy kodów ascii oto kilka z nich: \n"
            "Każdy znak w kodzie ascii ma przypisana wartość liczbową co umożliwia komputerom przechowywanie, "
            "przesyłanie i przetwarzanie tekstu. \n"
            "Jako, że kody ascii sa uniwersalne pozwalaną na komunikacje między systemami \n"
            "Są wykorzystywane do reprezentacji kalwiszy na klawiaturze i innych urządzeń wejścia \n"
            "Są wykorzystywane do porównywania, sortowania manipolowania tekstem \n"
            "Są wykorzystywane do kodowania np protokół HTTP "
        )

    def zad14(self):
        """Zad. 14
        Znajdź przykłady 3 sposobów na szyfrowanie znaków w systemach informatycznych
        i zapoznaj się z ich działaniem (jakie operacje matematyczne przeprowadzają?).
        """
        # używając zad14.txt zamiast pełnej ścieżki błąd:
        # FileNotFoundError: [Errno 2] No such file or directory: 'zad14.txt'
        with open("/PodstawySzkolenie/zad14.txt", encoding="utf-8") as plik:
            for line in plik.readlines():
                print(line, end="")
