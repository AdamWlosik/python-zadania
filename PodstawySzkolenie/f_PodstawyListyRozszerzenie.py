import random
import string

from PodstawySzkolenie.Szkolenie import Szkolenie


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
        wylosowana = random.randint(self.min_los, self.max_los )
        return wylosowana

    def nowa_lista(self, liczba, j):
        self.nowe_wyniki[j] = liczba

