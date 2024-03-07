import string

from PodstawySzkolenie.Szkolenie import Szkolenie


class Zadanie1S(Szkolenie):
    """Zad 1.
    Wprowadź poniższy słownik do programu. Program ma działać, tak jak poniżej:
    • wyświetla wszystkie klucze na konsoli (tzn. nazwy wszystkich albumów),
    • pobiera od użytkownika łańcuch tekstowy i sprawdza czy odpowiada on kluczowi ze słownika.

    Jeśli tak, to wyświetlany jest odpowiedni komunikat, np.: "Wykonawcą albumu "Achtung baby" jest “U2".
    W przeciwnym razie wyświetlany jest komunikat: "Brak danych".

    {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance',
     'Invisible Touch' : 'Genesis'}
    """

    """Zad 2.
          Zmodyfikuj kod z zadania 1 tak, aby możliwe było dodawanie i usuwanie przez użytkownika informacj
          o nowych albumach do słownika. Program ma zawierać proste menu.
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.klucz = None
        self.slowinik = None
        self.uwtorz_slownik()
        self.menu()

    def uwtorz_slownik(self):
        self.slowinik = {
            "The Sensual World": "Kate Bush",
            "Shaday": "Ofra Haza",
            "Achtung Baby": "U2",
            "Aion": "Dead Can Dance",
            "Invisible Touch": "Genesis",
        }

    def menu(self):
        while True:
            try:
                wybor = int(
                    input(
                        "Aby wyświetlić wszystkie klucze wybierz 1 \n"
                        "Aby wyświetlić wartość wybranego klucza wybierz 2 \n"
                        "Aby dodać informacje o nowym albumie wybierz 3 \n"
                        "Aby usunąć informacje o albumie wybierz 4 \n"
                        "Aby zakończyć wybierz 0 \n"
                        ""
                    )
                )
                if 0 > wybor > 4:
                    print("Nie psuj!")
            except ValueError:
                print("Nie psuj!")
            if wybor == 1:
                self.wyswietl_klucze()
            elif wybor == 2:
                self.pobierz_lancuch()
                self.wyswielt_wartosc_podanego_kulcza()
            elif wybor == 3:
                self.dodaj()
            elif wybor == 4:
                self.usun()
            elif wybor == 0:
                break

    def wyswietl_klucze(self):
        klucze = self.slowinik.keys()
        print(f"Klucze słownika: {klucze}")

    def pobierz_lancuch(self):
        self.klucz = input("Podaj klucz, po którym chcesz wyświetlić: ")

    def wyswielt_wartosc_podanego_kulcza(self):
        """Używam self.slowinik.get(self.klucz), aby uniknąć błędu KeyError, gdy klucz nie istnieje.
        Metoda get() zwraca wartość dla danego klucza, a jeśli klucz nie istnieje,
        zwraca wartość domyślną (domyślnie None)."""
        war = self.slowinik.get(self.klucz)
        if war:
            print(
                f"Wartość dla podanego klucza {self.klucz}: {self.slowinik[self.klucz]}"
            )
        else:
            print("Brak danych")

    def dodaj(self):
        klucz = input("Podaj klucz, który chcesz dodać: ")
        wartosc = input(f"Podaj wartość dla dodanego klucza {klucz}: ")
        self.slowinik[klucz] = wartosc

    def usun(self):
        klucz = input("Podaj klucz: ")
        try:
            del self.slowinik[klucz]
        except KeyError:
            print("Klucz nie istnieje")


class Zadanie3S(Szkolenie):
    """Zad 3.
    Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze). Wartości przypisane do tych kluczy
     mają być równe ilości wystąpień słowa w tekście.

    "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume
     of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping,
     rapping at my chamber door. This visitor, I muttered, tapping at my chamber door
     - Only this, and nothing more."
    """

    def __init__(self, szkolenie, zadanie, tekst):
        super().__init__(szkolenie, zadanie)
        self.tekst = tekst
        self.tekst_bez_interpunkcji = None
        self.usun_interpunkcje()
        self.slowa = None
        self.podzial_tekstu()
        self.slownik = {}
        self.dodaj_do_slownika()
        self.wyswietl_slownik()

    def usun_interpunkcje(self):
        znaki = str.maketrans("", "", string.punctuation)
        self.tekst_bez_interpunkcji = self.tekst.translate(znaki)
        # print(self.tekst_bez_interpunkcji)

    def podzial_tekstu(self):
        self.slowa = self.tekst_bez_interpunkcji.lower().split()
        # print(self.slowa)

    def dodaj_do_slownika(self):
        for wyraz in self.slowa:
            self.slownik[wyraz] = self.slownik.get(wyraz, 0) + 1

    def wyswietl_slownik(self):
        for klucz, wartosc in self.slownik.items():
            print(f"{klucz}: {wartosc}")


class Zadanie4S(Szkolenie):
    """Zad 4.
    Przekształć poniższy tekst, dopisując w nawiasach do polskich nazw ptaków ich łacińskie odpowiedniki.
    (TEkst w main)
    """

    def __init__(self, szkolenie, zadanie, slownik, tekst):
        super().__init__(szkolenie, zadanie)
        self.slownik = slownik
        self.tekst = tekst
        self.przeksztalc()

    def przeksztalc(self):
        for polska_nazwa, lacinska_nazwa in self.slownik.items():
            self.tekst = self.tekst.replace(
                polska_nazwa, f"{polska_nazwa} ({lacinska_nazwa})"
            )
            # połączenie klucz wartosc w jednego stringa i podmienienie
        print(self.tekst)


class Zadanie5S(Szkolenie):
    """Zad 5.
    Napisz skrypt, który wygeneruje i wyprintuje słownik zawierający liczby pomiędzy
    (1 - n; n jest liczbą podawaną przez użytkownika) w formie (x, x*x).
    Przykładowy input: n = 5
    Oczekiwany wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """

    def __init__(self, szkolenie, zadanie, n):
        super().__init__(szkolenie, zadanie)
        self.n = n
        self.slownik = {}
        self.generuj_slownik()
        # breakpoint()

    def generuj_slownik(self):
        for i in range(1, self.n + 1):
            self.slownik[i] = i * i


class Zadanie6S(Szkolenie):
    """Zad 6.
    Wyszukaj w zewnętrznych źródłach, jakie obiekty nie mogą być kluczami w słowniku.
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.odpowiedz = (
            "Obiekty modyfikowalne, takie jak listy czy słowniki, nie mogą być kluczami w słowniku,\n"
            "warto zauważyć, że krotki, które same zawierają obiekty modyfikowalne,\n"
            "również nie mogą być kluczami, ponieważ krotki są niemodyfikowalne,\n"
            "ale zawartość obiektów wewnątrz krotek może ulec zmianie."
        )


class Zadanie7S(Szkolenie):
    """Zad 7.
    Napisz program, który scali ze sobą dwa dowolne słowniki.
    Mając do dyspozycji następujące słowniki:
    lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
    friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

    Otrzymamy:
    {1: 'Rahima', 2: 'Alishba', 3: 'Fizza', 4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

    Zwróć uwagę na to, że słowniki mogą być różnej długości.
    """

    def __init__(self, szkolenie, zadanie, slownik1, slownik2):
        super().__init__(szkolenie, zadanie)
        self.slownik1 = slownik1
        self.slownik2 = slownik2
        self.scalony_slownik = {}
        self.scal()

    def scal(self):
        self.scalony_slownik = self.slownik1 | self.slownik2


class Zadanie8S(Szkolenie):
    """Zad 8.
    Napisz program, który wydrukuje wszystkie unikalne wartości ze słownika.
    Dla danych:
    { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
    Oczekujemy wyniku:
    “S002”, “S009”, “S007”
    """

    def __init__(self, szkolenie, zadanie, slownik):
        super().__init__(szkolenie, zadanie)
        self.slownik = slownik
        self.lista_unikalnych = []
        self.lista = []
        self.utworz_liste()
        self.utworz_liste_unikalnych()

    def utworz_liste(self):
        self.lista = list(self.slownik.values())

    def utworz_liste_unikalnych(self):
        self.lista_unikalnych = [
            wartosc for wartosc in set(self.lista) if self.lista.count(wartosc) == 1
        ]
        # pętla przechodzi po wartości w wartości z set(self.lista)
        # z warunkime wystąpenia wartosc raz w liście self.lista
