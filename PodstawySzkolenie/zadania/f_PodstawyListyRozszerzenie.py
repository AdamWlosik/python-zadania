import random
import string

from Szkolenie import Szkolenie


class Zadanie1LR(Szkolenie):
    """Zad 1.
        Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), następnie:
        ●	korzystając z metod operujących na listach, podaj wyrazy ze zdania w odwrotnej kolejności.
    """

    def __init__(self, szkolenie, zadanie, zdanie):
        super().__init__(szkolenie, zadanie)
        self.zdanie = zdanie
        self.bez_interpunkcji = None
        self.usun_interpunkcje()
        self.lista = []
        self.utworz_liste()
        self.odwroc()

    def usun_interpunkcje(self):
        translator = str.maketrans("", "", string.punctuation)
        self.bez_interpunkcji = self.zdanie.translate(translator)

    def utworz_liste(self):
        self.lista = list(self.bez_interpunkcji.split())

    def odwroc(self):
        self.lista.reverse()


class Zadanie2LR(Szkolenie):
    """Zad 2.
        W pewnej grze liczbowej wylosowano następujące liczby:
        wynik = [12,1,45,76,50,23]. Okazało się jednak, że wylosowane wartości powinny zawierać się w
        przedziale od 1 do 49. Napisz program zastępujący dowolne liczby – nie tylko te konkretne z zadania -
        występujące w liście, które nie spełniają tego kryterium, na wylosowane liczby, które będą je spełniać.
        Program powinien także zakomunikować, że znalazł błędną wartość i dokonał dla niej zmiany.

        Podpowiedź:
        Użyj modułu random, który trzeba importować, czyli: import random na początku programu.
        Zawiera on szereg funkcji losowych - poczytaj w Internecie o funkcjach losowych w Pythonie
        3. Jeśli chcesz wylosować liczbę całkowitą z przedziału [a,b],
        to możesz użyć funkcji losowej: randint(a,b), np. randint(5,10).
    """

    def __init__(self, szkolenie, zadanie, wynik, min_los, max_los):
        super().__init__(szkolenie, zadanie)
        self.wynik = wynik
        self.min_los = min_los
        self.max_los = max_los
        self.nowe_wyniki = self.wynik.copy()
        self.sprawdzenie_przedzialu()

    def sprawdzenie_przedzialu(self):
        j = 0
        for i in self.wynik:
            if i < self.min_los or i > self.max_los:
                nowa_liczba = self.losowanie()
                print(f"Wylosowana liczba {i} jest z poza przedziały i zostanie zastąpiona liczba {nowa_liczba} ")
                self.nowa_lista(nowa_liczba, j)
            else:
                self.nowa_lista(i, j)
            j += 1

    def losowanie(self):
        wylosowana = random.randint(self.min_los, self.max_los)
        return wylosowana

    def nowa_lista(self, liczba, j):
        self.nowe_wyniki[j] = liczba


class Zadanie3LR(Szkolenie):
    """Zad 3.
        Napisz program, który będzie pracował z trzema listami:
        lista1 = ["abc", "def", "ghi", "jkl"]
        lista2 = [1, 2, 3, 4, 5]
        lista3 = ["xyz", 1, '2']

        Niech program:
        • wydrukuje te listy
        • wydrukuje pierwszy oraz czwarty element z lista1
        • przypisze drugiemu elementowi lista2 wartości drugiego elementu z lista3
        • przypisze trzeciemu elementowi lista3 wartość tekstową wpisaną z klawiatury
        • doda nowy element ‘słowo’ do lista1 za pomocą metody .append()
        • skasuje element o indeksie 2 z lista1
        • wyznaczy liczbę elementów lista3
        • powiększy lista1 o elementy lista3
        Po każdej przeprowadzonej zmianie wydrukuje zmienioną listę.
    """

    def __init__(self, szkolenie, zadanie, lista1, lista2, lista3):
        super().__init__(szkolenie, zadanie)
        self.lista1 = lista1
        self.lista2 = lista2
        self.lista3 = lista3
        self.wydrukuj()
        self.wydrukuj_element_listy(self.lista1, 0)
        self.wydrukuj_element_listy(self.lista1, 3)
        self.wydrukuj_przypisanie(self.lista2, 1, self.lista3, 1)

    def wydrukuj(self):
        print(f"Lista1: {self.lista1}\n"
              f"Lista2: {self.lista2}\n"
              f"Lista3: {self.lista3}")

    def wydrukuj_element_listy(self, lista, element):
        print(f"Drukuje {element} element z listy: {lista[element]}")

    def przypisz_wartosc(self, lista1, element1, lista2, element2):
        lista1[element1] = lista2[element2]
        return lista1

    def wydrukuj_przypisanie(self, lista1, element1, lista2, element2):
        print(f"Lista z nowymi przypisaniami: {self.przypisz_wartosc(lista1, element1, lista2, element2)}")

    def przypisz_wartosc_z_klawiatury(self, lista, element, wartosc):
        lista[element] = wartosc
        return lista

    def dodaj_append(self, slowo, lista):
        lista.append(slowo)
        return lista

    def skasuj_element(self, element, lista):
        del lista[element]
        return lista

    def liczba_elementow(self, lista):
        return len(lista)

    def polacz(self, lista1, lista2):
        lista1.extend(lista2)
        return lista1


class Zadanie4LR(Szkolenie):
    """Zad 4.
        Napisz program, który poprosi użytkownika o podanie imion kilku swoich dobrych znajomych.
        Korzystając z wprowadzonych danych, dla każdego z podanych znajomych, program ma wyświetlić
        spersonalizowany komunikat, na przykład powitanie, pozdrowienie, który będzie skierowany do konkretnej osoby.
    """

    def __init__(self, szkolenie, zadanie, imiona):
        super().__init__(szkolenie, zadanie)
        self.imiona = imiona
        self.lista = self.utworz_liste()
        self.wyswietl_powitanie()

    def utworz_liste(self):
        lista = list(self.imiona.split())
        return lista

    def wyswietl_powitanie(self):
        for i in self.lista:
            print(f"Witaj {i}, pozdrawiam Cię :)")


class Zadanie5LR(Szkolenie):
    """Zad 5.
        Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), a następnie korzystając z metod operujących na listach, program powinien:
        • podawać liczbę wyrazów w zdaniu
        • podawać wyrazy, które rozpoczynają się wielką literą, jeśli takie są, jeśli nie, również to zgłosić
        • sprawdzać i podawać, czy lista zawiera: „i”, „w”, „na”, „pod”, „dla”. Jeśli tak, to które są to wyrazy i jakie są ich indeksy na liście. Jeśli żaden z poszukiwanych wyrazów w zdaniu nie występuje program również powinien o tym informować
        • posortować wyrazy ze zdania alfabetycznie i wydrukować je w zmienionej kolejności.
    """

    def __init__(self, szkolenie, zadanie, zdanie, sprawdzenie):
        super().__init__(szkolenie, zadanie)
        self.zdanie = zdanie
        self.sprawdzenie = sprawdzenie
        self.bez_interpunkcji = self.usun_interpunkcje()
        self.liczba_wyrazow()
        self.lista = self.utworz_liste()
        self.wielka_litera()
        self.czy_zawiera()

    def usun_interpunkcje(self):
        translator = str.maketrans("", "", string.punctuation)
        bez_interpunkcji = self.zdanie.translate(translator)
        return bez_interpunkcji

    def liczba_wyrazow(self):
        print(f"Liczba wyrazów w zdaniu: {len(self.bez_interpunkcji.split())}")

    def utworz_liste(self):
        lista = list(self.bez_interpunkcji.split())
        print(lista)
        return lista

    def wielka_litera(self):
        duze_litery = False
        for i in self.lista:
            if i[0].isupper():
                print(i)
                duze_litery = True
        if not duze_litery:
            print("Wszystkie wyrazy zaczynają sie do małej litery")

    def czy_zawiera(self):
        zawiera = False
        for index, element in enumerate(self.lista):
            for i in self.sprawdzenie:
                if element == i:
                    print(f"Lista zawiera: {element}, ma on index: {index}")
                    zawiera = True
        if not zawiera:
            print("Lista nie zawiera podanych wyrazów")





