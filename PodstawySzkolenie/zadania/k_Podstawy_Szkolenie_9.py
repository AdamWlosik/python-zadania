from datetime import datetime
import random
from pprint import pprint

from Szkolenie import Szkolenie
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
        """Metoda wyliczająca nowy przebieg"""
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
        self.wlasciciel = self._change_ownership()
        self._display()

    def _deposit(self, kwota):
        """Metoda obliczająca stan konta po wpłacie i uwzględniając prowizje"""
        prowizja = 0
        for i in range(int(kwota)):
            if i % 100 == 0 and i != 0:
                prowizja += 2
        self.stan_konta += (kwota - prowizja)

    def _withdraw(self, kwota):
        """Metoda wypłacająca z konta z uwzględniająca czy wystarczająco środków"""
        if kwota <= self.stan_konta:
            self.stan_konta -= kwota
        else:
            print("Brak wystarczającej ilość środków na koncie")

    def _change_ownership(self):
        """Metoda zmieniająca imię nowego właściciela konta"""
        nowe_imie = input("Podaj nowe imię nowego właściciela konta: ")
        return nowe_imie

    def _display(self):
        print("Numer konta: ", self.numer_konta)
        print("Imię właściciela: ", self.wlasciciel)
        print("Stan konta: ", self.stan_konta)


class Zadanie5PS9(Szkolenie):
    """Zad. 5
        Stwórz program symulujący talię kart (klasa Deck) oraz pojedyncze karty (klasa Card).
        Karta ma być związana z takimi polami jak: wartość (np. 9) oraz figura (np. Diamond).
        W klasie Deck znajdować ma się lista reprezentująca stos kart w ramach jednej talii.
        W Deck znaleźć mają się takie metody jak: shuffle
        (która może wykorzystywać metodę o tej samej nazwie - shuffle - z biblioteki random) oraz deal
        (która będzie usuwała i zwracała ostatnią kartę z talii).

        Podpowiedź:
        Talia kart ma się składać z 52 różnych obiektów Card o wszystkich możliwych kombinacjach pól,
        np. (A - Diamond, A - Clubs itd). Aby utworzyć taką kombinację, utwórz dwie niezależne listy -
        w pierwszej przechowuj możliwe figury, a w drugiej wartości. Następnie przechodząc pętlami,
        łącz je ze sobą i twórz obiekty."""

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        figury = ["pik", "kier", "trefl", "karo"]
        wartosci = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        talia = Talia(figury, wartosci)
        utworzona_talia = talia.utworz_talie()
        print("Utworzona talia: ", utworzona_talia)
        potasowana_talia = talia.przetasuj()
        print("Potasowana talia: ", potasowana_talia)
        rozdana_karta = talia.rozdaj_karte()
        print("Rozdana karta: ", rozdana_karta)


class Karta:

    def __init__(self, wartosc, figura):
        self.wartosc = wartosc
        self.figura = figura
        # self.utworz_karte()

    def __str__(self):
        return f"{self.wartosc} - {self.figura}"

    def __repr__(self):
        """Wyświetla dobrze jako obiekt złozony lista itd"""
        return str(self)

    """def utworz_karte(self):
        return str(f"{self.wartosc} - {self.figura}")"""


class Talia:

    def __init__(self, figury, wartosci):
        self.figury = figury
        self.wartosci = wartosci
        self.talia = self.utworz_talie()

    def utworz_talie(self):
        """Metoda łącząca listy figury i wartości w jedną talię kart"""
        talia = []
        for figura in self.figury:
            for wartosc in self.wartosci:
                karta = Karta(wartosc, figura)
                print(karta)
                talia.append(karta)
                # dlaczego print(karta) drukuje A - karo
                # a print talia po dodtaniu karty do listy drukuje już
                # <PodstawySzkolenie.k_Podstawy_Szkolenie_9.Karta object at 0x00000215B57B65D0>
                # i jak to zmienić?
                print(talia)
        return talia

    def przetasuj(self):
        """Metoda tasująca listę kart"""
        random.shuffle(self.talia)
        return self.talia

    def rozdaj_karte(self):
        """Metoda wyciągające ostatni element z listy talia """
        if len(self.talia) > 0:
            rozdana_karta = self.talia[-1]
            self.talia.pop()
            return rozdana_karta
        else:
            return "Brak kart do rozdania"


class Zadanie6PS9(Szkolenie):
    """Zad. 6
        Zrób system, który obsługiwał będzie określone zamówienia. W programie istnieć będą 2 klasy: Manager oraz Order.
        W Managerze ma się znajdować słownik zamówień, w którym kluczem będzie obiekt zamówienia,
        a wartością jego ilość na stanie. W klasie Order natomiast mają znajdować się takie pola jak: id, nazwa, cena.

        Funkcjonalność programu to:
        - dodawanie nowego zamówienia do słownika (jeżeli dodawać będziemy obiekt,
            którego id znajduje się już w słowniku, to nie będziemy dodawali nowej pary do dicta,
            ale zwiększali ilość danego obiektu w słowniku (zwiększali odpowiednią wartość w słowniku)).
        - usuwanie o 1 zamówienia ze słownika o określonym id

        Podpowiedź:
        Pseudokod slownika:
        self.orders = {obiekt1 : jego_ilosc}

        Sprzedawanie produktu:

        def sell(self, id_to_sell):
            for order in self.orders:
                if order.id == id_to_sell:
                   self.orders[order] -= 1
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        manager = Manager()

        zamownienie1 = Zamowienia("zamowienie1", "Produkt A", 20.0)
        zamownienie2 = Zamowienia("zamowienie2", "Produkt B", 30.0)

        manager.dodaj_zamowienie(zamownienie1)
        manager.dodaj_zamowienie(zamownienie2)
        manager.dodaj_zamowienie(zamownienie1)
        manager.dodaj_zamowienie(zamownienie1)

        print("Stan zamówień po dodaniu:")
        print(manager.zamowienia)

        manager.usun_zamowinie("zamowienie1")
        manager.usun_zamowinie("zamowienie2")
        manager.usun_zamowinie("zamowienie2")

        print("Stan zamówień po usunięciu:")
        print(manager.zamowienia)

        manager.sprzedaj("zamowienie1")
        manager.sprzedaj("zamowienie1")

        print("Stan zamówień po sprzedaniu:")
        print(manager.zamowienia)


class Zamowienia:

    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena


class Manager:

    def __init__(self):
        self.zamowienia = {}

    def dodaj_zamowienie(self, zamowienie):
        """Metoda dodająca nowe zamówienie do słownika"""
        if zamowienie.id in self.zamowienia:
            self.zamowienia[zamowienie.id] += 1
        else:
            self.zamowienia[zamowienie.id] = 1

    def usun_zamowinie(self, id):
        """Metoda usuwająca zamówienie z listy po przyjętym id"""
        if id in self.zamowienia and self.zamowienia[id] > 0:
            self.zamowienia[id] -= 1
            print(f"Usunięto jedno zamówienie o id {id}.")
        else:
            print(f"Brak zamówienia o id {id}")

    def sprzedaj(self, id):
        """Metoda usuwające sprzedane zamówienia z listy"""
        for zamowienie in self.zamowienia:
            if id in zamowienie:
                self.zamowienia[zamowienie] -= 1


class Zadanie8PS9(Szkolenie):
    """Zad. 8
        Rozważ klasę Case, która będzie inicjalizowana wraz z poniższymi danymi:

        first_case = {
            ‘name’: ‘first_case’,
            ‘created_task’: ‘2021-10-26T19:48:12+00:00’,
            ‘end_task’: None
        }

        second_case = {
            ‘name’: ‘second_case’,
            ‘created_task’: ‘2021-09-26T19:48:12+00:00’,
            ‘end_task’: ‘2021-10-26T19:48:12+00:00’
        }

        Klasa Case ma zawierać metodę retrieve_seconds,
        która zwracać będzie różnicę czasową między end_task a created_task podaną w sekundach.

        UWAGA
        1.	Wartość None przypisana do klucza end_task oznacza, że task jeszcze trwa.
        2.	Zwróć uwagę na to, iż retrieve_seconds możemy wywoływać wielokrotnie
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        first_case_data = {
            'name': 'first_case',
            'created_task': '2021-10-26T19:48:12+00:00',
            'end_task': None
        }

        second_case_data = {
            'name': 'second_case',
            'created_task': '2021-09-26T19:48:12+00:00',
            'end_task': '2021-10-26T19:48:12+00:00'
        }

        first_case = Case(**first_case_data)
        second_case = Case(**second_case_data)

        # Wywołanie retrieve_seconds dla obiektów Case
        print(f"Różnica czasu dla first_case: {first_case.retrieve_seconds()} sekund")
        print(f"Różnica czasu dla second_case: {second_case.retrieve_seconds()} sekund")


class Case:
    def __init__(self, name, created_task, end_task):
        self.name = name
        self.created_task = self._datatime(created_task)
        self.end_task = self._datatime(end_task) if end_task is not None else None

    def _datatime(self, datetime_str):
        """Metoda przekształcająca ciąg znaków w obiekt typy datetime"""
        return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")

    def retrieve_seconds(self):
        """Metoda obliczająca różnice czasu z uwzględnieniem strefy czasowej"""
        current_time = datetime.now().astimezone()

        if self.end_task is None:
            return (current_time - self.created_task).total_seconds()
        else:
            return (self.end_task - self.created_task).total_seconds()


class Zadanie7PS9(Szkolenie):
    """Zad. 7
        Utworzyć klasy Notatka (Note) i Notatnik (Notebook). Klas notatki przechowuje autora,
        treść i czas utworzenia (autor i treść są podawane jako argumenty konstruktora,
        a czas jest pobierany i zapisywany przy tworzeniu obiektu).
        Konstruktor klasy Notatnik nie przyjmuje żadnych argumentów,
        lecz tworzy pustą listę do której będą dodawane obiekty klasy Notatka.
        Klasa Notatnika musi posiadać implementacje metod,
        pozwalających: dodać nową notatkę, dodać istniejącą notatkę, sprawdzić ile jest dodanych notatek,
        wyświetlić wszystkie dodane notatki. Dodatkowo musi być obsłużona sytuacja kiedy notatnik jest pusty.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        nb = Notebook()
        nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")
        nb.wyswietl_wszystko()

        n1 = Note("Andrii", "Sprawdzic instrukcje ")
        nb.dodaj(n1)
        nb.wyswietl_wszystko()


class Note:

    def __init__(self, autor, tresc):
        self.autor = autor
        self.tresc = tresc
        self.czas_utowrzenia = datetime.now()


class Notebook:

    def __init__(self):
        self.notatki = []

    def dodaj_nowa(self, autor, tresc):
        """Metoda dodająca nową notatkę do klasy i listy"""
        nowa_notatka = Note(autor, tresc)
        self.notatki.append(nowa_notatka)

    def dodaj(self, notatka):
        """Motorola sprawdzająca, czy notatka jest instancją klasy i dodająca ją do listy """
        if isinstance(notatka, Note):
            self.notatki.append(notatka)
        else:
            print("Notatka nie jest instancją klasy")

    def wyswietl_wszystko(self):
        if not self.notatki:
            print("Notatnik jest pusty")
        else:
            print("Masz takie notatki: ")
            for index, notatka in enumerate(self.notatki, start=1):
                print(f"{index}. {notatka.autor}: {notatka.tresc} "
                      f"o godzinie {notatka.czas_utowrzenia.strftime('%H:%M')}")


class Zadanie9PS9(Szkolenie):
    """Zad. 9 [*Challenge]

        1) Stwórz klasę Tank (zbiornik).
        Zbiornik posiada następujące atrybuty: nazwę oraz pojemność.
        Należy stworzyć następujące operacje:
        -	pour_water(volume) - ale w zbiorniku nie może być więcej wody niż pojemność
        -	pour_out_water(volume) - ale nie można odlać więcej wody niż jest dostępne w zbiorniku
        -	transfer_water(from, volume) - przelewa wodę ze zbiornika “from” do naszego
            (pod warunkiem, że przelewanie jest możliwe)
        Dodatkowo stworzyć metody, które pozwalają:
        -	Znaleźć zbiornik, w którym jest najwięcej wody
        -	Znaleźć zbiornik, który jest najbardziej zapełniony
        -	Znaleźć wszystkie puste zbiorniki
        2) Każda operacja na zbiorniku jest rejestrowana.
        Dla każdej operacji pamiętamy: datę i czas jej wykonania, jej nazwę, zbiornik,
        na którym była ona wykonana oraz ilość wody, jaka była brana pod uwagę oraz to,
        czy operacja się powiodła czy nie.

        Należy zaimplementować taką funkcjonalność oraz dodatkowo stworzyć metody, które:
        -	Pozwalają znaleźć zbiornik, na którym było najwięcej operacji zakończonych niepowodzeniem
        -	Pozwalają znaleźć zbiornik, w którym było najwięcej operacji danego typu (typ podajemy jako argument metody)

        3) To co zaimplementowaliśmy powyżej to demo “Event Sourcingu” - na czym ono polega?
        Zaimplementuj metodę check_state(tank_name), która pozwoli określić, czy stan wody jest spójny z tym,
        co mamy na liście historii operacji dla danego zbiornika.

        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        operation = Operation()

        tank1 = Tank("Tank1", 100, 50)
        tank2 = Tank("Tank2", 100, 40)
        tank3 = Tank("Tank3", 200, 50)
        tank4 = Tank("Tank4", 100, 50)
        tank5 = Tank("Tank5", 200, 50)
        tank6 = Tank("Tank6", 100, 0)
        tank7 = Tank("Tank7", 100, 0)

        operation.add_tank_to_list(tank1)
        operation.add_tank_to_list(tank2)
        operation.add_tank_to_list(tank3)
        operation.add_tank_to_list(tank4)
        operation.add_tank_to_list(tank5)
        operation.add_tank_to_list(tank6)
        operation.add_tank_to_list(tank7)

        """print("Tank1:")
        operation.pour_water(tank1, 20)
        print(f"Instancja klasy po dodaniu wody: ", tank1.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank1.operations_history)
        print("Tank2:")
        operation.pour_water(tank2, 300)
        print(f"Instancja klasy po dodaniu wody: ", tank2.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank2.operations_history)"""

        """print("Tank1:")
        operation.pour_out_water(tank1, 20)
        print(f"Instancja klasy po dodaniu wody: ", tank1.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank1.operations_history)
        print("Tank2:")
        operation.pour_out_water(tank2, 300)
        print(f"Instancja klasy po dodaniu wody: ", tank2.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank2.operations_history)"""

        """print("Tank1:")
        operation.transfer_water(tank1, tank2, 300)
        print(f"Instancja klasy po dodaniu wody: ", tank1.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank1.operations_history)
        print("Tank2:")
        print(f"Instancja klasy po dodaniu wody: ", tank2.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank2.operations_history)"""

        operation.pour_water(tank1, 20)
        operation.pour_water(tank1, 20)
        operation.pour_water(tank1, 20)
        operation.pour_water(tank4, 20)
        operation.pour_water(tank2, 300)
        operation.pour_water(tank2, 300)
        operation.pour_water(tank2, 300)
        operation.pour_out_water(tank1, 20)
        operation.pour_out_water(tank2, 300)
        operation.transfer_water(tank1, tank2, 300)
        operation.transfer_water(tank2, tank1, 20)
        operation.transfer_water(tank1, tank2, 20)
        print("Most water tank:", operation.find_tank_with_most_water())
        print("Highest water lvl tank:", operation.find_tank_with_the_highest_water_lvl())
        print("Empty tank:", operation.find_empty_tank())
        print("The most failed operation:", operation.find_tank_with_the_most_failed_operation())
        print("Tank with teh most operation of specified type",
              operation.find_tank_with_the_most_operation_of_type("pour water"))
        print("Check state: ", operation.check_state(tank1, 50))
        for tank_name, tank_data in operation.tanks_dict.items():
            print(tank_name)
            pprint(tank_data)


class Tank:

    def __init__(self, name, capacity, water_lvl):
        self.name = name
        self.capacity = capacity
        self.water_lvl = water_lvl
        self.operations_history = []


class Operation:
    def __init__(self):
        self.tanks_dict = {}

    def add_tank_to_list(self, tank):
        """Metoda sprawdzająca, czy zbiornik jest na liście, jeśli nie to go dodaje"""
        if tank.name not in self.tanks_dict:
            self.tanks_dict[tank.name] = {"capacity": tank.capacity, "water lvl": tank.water_lvl,
                                          "operation history": tank.operations_history}

        return self.tanks_dict

    def _update_tank_list(self, tank):
        """Metoda dodająca zmiany do listy"""
        self.tanks_dict[tank.name] = {"capacity": tank.capacity, "water lvl": tank.water_lvl,
                                      "operation history": tank.operations_history}
        # print(f"Tank list po update: ", self.tanks_dict)

    def _operation_history(self, operation_name, tank_name, volume, success):
        """Metoda zwracająca słownik historii operacji"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {
            'timestamp': timestamp,
            'name': operation_name,
            'tank': tank_name,
            'volume': volume,
            'success': success
        }

    def pour_water(self, tank, volume):
        """Metoda dolewająca wody do zbiornika"""
        if tank.name not in self.tanks_dict:
            self.add_tank_to_list(tank)
        water_lvl = self.tanks_dict[tank.name].get("water lvl")
        # print("Water lvl: ", water_lvl)
        capacity = self.tanks_dict[tank.name].get("capacity")
        # print("Capacity: ", capacity)
        if water_lvl + volume <= capacity:
            tank.water_lvl = water_lvl + volume
            tank.operations_history.append(self._operation_history("pour water", tank.name, volume, True))
            self._update_tank_list(tank)
        else:
            tank.operations_history.append(self._operation_history("pour water", tank.name, volume, False))
            self._update_tank_list(tank)

    def pour_out_water(self, tank, volume):
        """Metoda odlewająca wode ze zbiornika"""
        if tank.name not in self.tanks_dict:
            self.add_tank_to_list(tank)
        water_lvl = self.tanks_dict[tank.name].get("water lvl")
        # print("Water lvl: ", water_lvl)
        if water_lvl - volume >= 0:
            tank.water_lvl = water_lvl - volume
            tank.operations_history.append(self._operation_history("pour out water", tank.name, volume, True))
            self._update_tank_list(tank)
        else:
            tank.operations_history.append(self._operation_history("pour out water", tank.name, volume, False))
            self._update_tank_list(tank)

    def transfer_water(self, tank1, tank2, volume):
        """Metoda przelewająca wodę z tank1 do tank2 o volume"""
        if tank1.name not in self.tanks_dict:
            self.add_tank_to_list(tank1)
        if tank2.name not in self.tanks_dict:
            self.add_tank_to_list(tank2)
        water_lvl1 = self.tanks_dict[tank1.name].get("water lvl")
        water_lvl2 = self.tanks_dict[tank2.name].get("water lvl")
        capacity2 = self.tanks_dict[tank2.name].get("capacity")
        if water_lvl1 >= water_lvl1 - volume and capacity2 >= water_lvl2 + volume:
            tank2.water_lvl = water_lvl2 - volume
            tank1.water_lvl = water_lvl1 + volume
            tank2.operations_history.append(self._operation_history("transfer", tank2.name, -volume, True))
            tank1.operations_history.append(self._operation_history("transfer", tank1.name, volume, True))
            self._update_tank_list(tank1)
            self._update_tank_list(tank2)
        else:
            tank2.operations_history.append(self._operation_history("transfer", tank2.name, -volume, False))
            tank1.operations_history.append(self._operation_history("transfer", tank1.name, volume, False))
            self._update_tank_list(tank1)
            self._update_tank_list(tank2)

    def find_tank_with_most_water(self):
        """Metoda znajdująca zbiorniki z największą ilością wody"""
        max_water_lvl = None
        tanks_with_max_water_lvl = []

        for tank_name, tank_data in self.tanks_dict.items():
            water_lvl = tank_data.get('water lvl')
            if max_water_lvl is None or water_lvl > max_water_lvl:
                # Nowa największa wartość, zresetuj listę i dodaj aktualny zbiornik
                max_water_lvl = water_lvl
                tanks_with_max_water_lvl = [tank_name]
            elif water_lvl == max_water_lvl:
                # Równa największa wartość, dodaj aktualny zbiornik do listy
                tanks_with_max_water_lvl.append(tank_name)

        return tanks_with_max_water_lvl

    def find_tank_with_the_highest_water_lvl(self):
        """Metoda znajdująca najbardziej wypełniony zbiornik"""
        max_capacity_filling = None
        tanks_with_highest_water_lvl = []

        for tank_name, tank_data in self.tanks_dict.items():
            if tank_data.get('water lvl') != 0:
                capacity_filling = tank_data.get('capacity') / tank_data.get('water lvl')
                if max_capacity_filling is None or capacity_filling < max_capacity_filling:
                    max_capacity_filling = capacity_filling
                    tanks_with_highest_water_lvl = [tank_name]
                elif capacity_filling == max_capacity_filling:
                    tanks_with_highest_water_lvl.append(tank_name)
        return tanks_with_highest_water_lvl

    def find_empty_tank(self):
        """Metoda znajdująca puste zbiorniki"""
        empty_tank = []

        for tank_name, tank_data in self.tanks_dict.items():
            water_lvl = tank_data.get('water lvl')
            if water_lvl == 0:
                empty_tank.append(tank_name)
        return empty_tank

    def find_tank_with_the_most_failed_operation(self):
        """Metoda znajdująca zbiorniki z największą ilością nieudanych operacji"""
        tank_with_failed_operation = []
        frequency_dict = {}

        for tank_name, tank_data in self.tanks_dict.items():
            operation_history = tank_data.get('operation history')
            for element in operation_history:
                if not element['success']:
                    # print(element)
                    tank_with_failed_operation.append(tank_name)
                    # print(tank_with_failed_operation)
        for element in tank_with_failed_operation:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
        return max(frequency_dict, key=frequency_dict.get)

    def find_tank_with_the_most_operation_of_type(self, operation_type):
        """Metoda znajdująca zbiornik z największą liczbą operacji danego typu"""
        tank_operation = {}
        most_operation = {}

        for tank_name, tank_data in self.tanks_dict.items():
            operation_history = tank_data.get('operation history')
            tank_operation[tank_name] = {}
            for element in operation_history:
                for key, value in element.items():
                    if key == 'name':
                        tank_operation[tank_name][value] = tank_operation[tank_name].get(value, 0) + 1
                        # print(tank_operation)

        for tank_name, tank_data in tank_operation.items():
            operation = tank_data.get(operation_type)
            # print(operation)
            if operation:
                most_operation[tank_name] = operation
                # print(most_operation)

        max_value = max(most_operation.values())
        keys_with_max_values = [key for key, value in most_operation.items() if value == max_value]
        # print(keys_with_max_values)
        return keys_with_max_values

    def check_state(self, tank, start_value):
        """Metoda sprawdzająca spójność stanu wody z historią operacji"""
        water_level_from_history = 0

        for operation in tank.operations_history:
            if operation['success']:
                if operation['name'] == 'pour water':
                    water_level_from_history += operation['volume']
                elif operation['name'] == 'transfer':
                    water_level_from_history += operation['volume']
                elif operation['name'] == 'pour out water':
                    water_level_from_history -= operation['volume']
        return (tank.water_lvl - start_value) == water_level_from_history
