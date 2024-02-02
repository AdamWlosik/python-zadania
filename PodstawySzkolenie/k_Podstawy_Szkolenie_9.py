from PodstawySzkolenie.Szkolenie import Szkolenie
from helpers import print_doc


class Zadanie1PS9(Szkolenie):
    """Zad. 1
        Stwórz klasę reprezentującą studenta. Cechy studenta określaj z poziomu konstruktora.
        Dodaj do klasy metodę wyświetlającą informacje o danym obiekcie.
        """

    def __init__(self, szkolenie, zadanie, imie, nazwisko, numer_indeksu, kierunek):
        super().__init__(szkolenie, zadanie)
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.kierunek = kierunek

    @print_doc
    def rozwiazanie(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Numer indeksu: {self.numer_indeksu}")
        print(f"Kierunek: {self.kierunek}")


class Zadanie2PS9(Szkolenie):
    """Zad. 2
        Stwórz klasę reprezentującą pojazd.
        Dodaj do niej pola określające maksymalną prędkość obiektu oraz jego przebieg.
        Dodaj do klasy metodę, która zwiększać będzie wartość pola przebiegu o przesłaną wartość typu float.
        """

    def __init__(self, szkolenie, zadanie, zwieksz):
        super().__init__(szkolenie, zadanie)
        self.predkosc_max = 250
        self.przebieg = 20000.300
        self.zwieksz = zwieksz

    @print_doc
    def rozwiazanie(self):
        nowy_przebieg = self._zwieksz_przebieg()
        print("Nowy przebieg: ", nowy_przebieg)

    def _zwieksz_przebieg(self):
        """Metoda wyliczajaca nowy przbieg"""
        nowy_przebieg = self.przebieg + self.zwieksz
        return nowy_przebieg


class Zadanie3PS9(Szkolenie):
    """Zad. 3
        Stwórz klasę reprezentującą Prostokąt.
        Dodaj do niej metody obliczające pole i obwód z przechowywanych pól - szerokości i długości.
        """

    def __init__(self, szkolenie, zadanie, szerokosc, dlugosc):
        super().__init__(szkolenie, zadanie)
        self.szerokosc = szerokosc
        self.dlugosc = dlugosc

    @print_doc
    def rozwiazanie(self):
        obwod = self._oblicz_obwod()
        pole = self._oblicz_pole()
        print(f"Pole: {pole}\n"
              f"Obwód: {obwod}")

    def _oblicz_obwod(self):
        """Metoda obliczająca obwód"""
        obwod = 2 * (self.dlugosc + self.szerokosc)
        return obwod

    def _oblicz_pole(self):
        """Metoda obliczająca pole"""
        pole = self.szerokosc * self.dlugosc
        return pole


class Zadanie4PS9(Szkolenie):
    """Zad. 4
        Stwórz Pythonową klasę BankAccount, która reprezentować będzie konto bankowe zawierające takie informacje jak:
         numer_konta, nazwa właściciela konta, stan konta.
        1.	Stwórz konstruktor odpowiednio uzupełniający pola.
        2.	Napisz metodę deposit(), która przyjmować będzie kwotę, jaką chcesz wpłacić na konto. Dodaj założenie,
            że za każde wpłacone 100 zł, pobierana będzie prowizja równa 2 zł.
        3.	Stwórz metodę withdraw(), która przyjmować będzie jako parametr kwotę, którą chcesz wypłacić z konta.
            Program ma wyświetlać odpowiedni komunikat, gdy niemożliwe jest wypłacanie wskazanej ilości pieniędzy
            (przykładowo z powodu braku wystarczającej ilości środków na koncie).
        4.	Napisz metodę change_ownership(), która przyjmować będzie imię nowego właściciela konta
            i będzie aplikowała tę zmianę w obiekcie klasy.
        5.	Stwórz metodę display(), która będzie wyświetlać wszystkie informacje o koncie.
        """

    def __init__(self, szkolenie, zadanie, numer_konta, wlasciciel, stan_konta):
        super().__init__(szkolenie, zadanie)
        self.numer_konta = numer_konta
        self.wlasciciel = wlasciciel
        self.stan_konta = stan_konta

    @print_doc
    def rozwiazanie(self):
        try:
            kwota = float(input("Podaj kwotę, którą chcesz wpłacić: "))
            self._deposit(kwota)
        except ValueError:
            print("Nie psuj")
        try:
            kwota_wyplaty = float(input("Podaj kwotę, którą chcesz wypłacić: "))
            self._deposit(kwota_wyplaty)
        except ValueError:
            print("Nie psuj")

    def _deposit(self, kwota):
        """Motoda obliczająca stan konta po wpłacie i uwzględniając prowizje"""
        prowizja = 0
        for i in range(int(kwota)):
            if i % 100 == 0 and i != 0:
                prowizja += 2
        self.stan_konta += (kwota - prowizja)

    def _withdraw(self, kwota):
        """Metoda wypłacająca z konta z uwzględniająca czy wystaczająca srodków"""
        if kwota <= self.stan_konta:
            self.stan_konta -= kwota
        else:
            print("Brak wsyatczającej ilość środków na koncie")


