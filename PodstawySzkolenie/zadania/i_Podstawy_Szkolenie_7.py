from Szkolenie import Szkolenie


class Zadanie1PS7(Szkolenie):
    """
        Zad 1.
        Zdefinuj funkcję, która znajdzie i zwróci indeks największego elementu z przekazanej jako parametr listy

        nums = [4, 6, 8, 24, 12, 2]

        Dodatkowo:
        Zapoznaj się funkcją enumerate z dokumentacji """

    def __init__(self, szkolenie, zadanie, nums):
        super().__init__(szkolenie, zadanie)
        self.nums = nums
        self.index = self.znajdz_najwiekszy()

    def znajdz_najwiekszy(self):
        index_max = 0
        wartosc_max = self.nums[0]
        for index, wartosc in enumerate(self.nums):
            if wartosc > wartosc_max:
                index_max = index
                wartosc_max = wartosc
        return f"{index_max}, ma on wartość: {wartosc_max}"


class Zadanie2PS7(Szkolenie):
    """Zad 2.
        Czym się różni argument od parametru funkcji, default arguments od keyword arguments?
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    """Parametr funkcji:
        Definicja: Parametr to zmienna używana w deklaracji funkcji. 
        To nazwa, która występuje w nawiasach okrągłych podczas definiowania funkcji.
        Przykład: W funkcji def dodaj(a, b):, a i b są parametrami.
        def dodaj(a, b):
            wynik = a + b
            return wynik
        
        Argument funkcji:
        Definicja: Argument to wartość przekazana do funkcji podczas jej wywołania. 
        To rzeczywista wartość, która jest przypisywana do parametru.
        Przykład: W wywołaniu funkcji dodaj(3, 5), 3 i 5 są argumentami.
        suma = dodaj(3, 5)
        
        Default Argument (Domyślny argument):
        Definicja: Domyślny argument to taki, który otrzymuje wartość domyślną w przypadku, gdy nie zostanie przekazana wartość podczas wywoływania funkcji.
        Przykład:
        def powitanie(imie="Świato"):
            print(f"Witaj, {imie}!")
        powitanie()  # Wyświetli "Witaj, Świato!"
        powitanie("Anna")  # Wyświetli "Witaj, Anna!"
        
        Keyword Argument (Nazwany argument):
        Definicja: Nazwany argument to taki, który jest przekazywany do funkcji w formie klucz=wartość. Pozwala to na przekazywanie argumentów bez konieczności pamiętania kolejności parametrów funkcji.
        Przykład:
        def powitanie(imie, wiek):
            print(f"Witaj, {imie}! Masz {wiek} lat.")
        powitanie(imie="Anna", wiek=25)
        
        Podsumowując, parametr to zmienna w definicji funkcji, a argument to wartość przypisywana do tego parametru
        podczas wywoływania funkcji. Domyślny argument to parametr, który ma wartość domyślną, a nazwany argument
        to argument przekazywany za pomocą formy klucz=wartość, co pozwala na przekazywanie argumentów
        bez konieczności pamiętania kolejności."""


class Zadanie3PS7(Szkolenie):
    """Zad 3.
        Napisz funkcję fizz_buzz, która przyjmuje argument liczbowy.
        1.	Jeżeli liczba jest podzielna przez 3, funkcja powinna zwrócić “Fizz”.
        2.	Jeżeli liczba jest podzielna przez 5, zwróć “Buzz”.
        3.	Jeżeli liczba jest podzielna równocześnie przez 3 i 5, zwróć “FizzBuzz”.
        4.	W przeciwnym razie, zwracaj przekazaną liczbę.
    """

    def __init__(self, szkolenie, zadanie, liczba):
        super().__init__(szkolenie, zadanie)
        self.liczba = liczba
        self.wynik = self.fizz_buzz(self.liczba)

    def fizz_buzz(self, liczba):
        if liczba % 3 == 0 and liczba % 5 == 0:
            return "FizzBuzz"
        else:
            if liczba % 3 == 0:
                return "Fizz"
            elif liczba % 5 == 0:
                return "Buzz"
            else:
                return liczba


class Zadanie4PS7(Szkolenie):
    """Zad 4.
        Napisz funkcję odbierającą w postaci *args dowolną ilość elementów i zwracającą ich iloczyn.
    """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.iloczyn()

    def iloczyn(self, *args):
        wynik = 1
        for i in args:
            wynik *= i
        return wynik


class Zadanie5PS7(Szkolenie):
    """Zad 5.
        Prześlij przy użyciu **kwargs listę liczb parzystych i nieparzystych. W funkcji dokonaj ich połączenia
         w jedną listę w następujący sposób: [nieparzysta, parzysta nieparzysta, parzysta ...]
        """

    def __init__(self, szkolenie, zadanie, lista_parzyste, lista_nieparzyste):
        super().__init__(szkolenie, zadanie)
        self.wynik = self.polacz(parzyste=lista_parzyste, nieparzyste=lista_nieparzyste)

    def polacz(self, **kwargs):
        wynik = []
        if 'nieparzyste' in kwargs:
            wynik.extend(kwargs['nieparzyste'])
        if 'parzyste' in kwargs:
            j = 1
            for liczba in kwargs['parzyste']:
                wynik.insert(j, liczba)
                j += 2
        return wynik


class Zadanie6PS7(Szkolenie):
    """Zad 6.
        Napisz funkcję, która jako argument przyjmuje 10-cio elementową listę liczb całkowitych.
        Ma ona zwrócić przefilitrowaną listę elementów składającą się tylko z liczb dwucyfrowych
        wyselekecjonowanych z odebranej listy
        """

    def __init__(self, szkolenie, zadanie, lista):
        super().__init__(szkolenie, zadanie)
        self.wynik = self.filtrowanie(lista)

    def filtrowanie(self, lista):
        nowa_lista = []
        for element in lista:
            if element > 9:
                nowa_lista.append(element)
        return nowa_lista


class Zadanie7PS7(Szkolenie):
    """Zad. 7
        Pamiętasz zadanie nr 9 z cyklu zadań: 5 Podstawy Pętle (to o astronautach)?
        Masz następujące zadanie - zrefaktoryzować wówczas napisany kod w taki sposób,
        aby rozwiązanie oprzeć o funkcje!
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)
        self.wyswietl_informacje()

    def wyswietl_informacje(self):
        print("Zadanie zostało już wcześniej opartę na funkcjach")


class Zadanie8PS7(Szkolenie):
    """Zad 8*.
        Napisz funkcję, ktora przyjmować będzie godzinę i minutę (wykorzystaj keyword arguments)
        i powinna ona zwrócić kąt (podany w stopniach) między wskazówką godzinową a minutową w tym podanym czasie.

        Podpowiedź:
        Możesz wykorzystać funkcję abs w celu obliczania wartości bezwzględnej, np.
        print(abs(-5)) # 5
        """

    def __init__(self, szkolenie, zadanie, godzina, minuta):
        super().__init__(szkolenie, zadanie)
        self.kat = self.oblicz_kat(godzina=godzina, minuta=minuta)

    def oblicz_kat(self, godzina, minuta):
        kat_godzina = (godzina % 12) * 30 + minuta * 0.5
        kat_minuta = minuta * 6
        roznica_katow = abs(kat_godzina - kat_minuta)
        return roznica_katow


