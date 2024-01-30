from PodstawySzkolenie.Szkolenie import Szkolenie


class Zadanie1PSDR(Szkolenie):
    """Zad 1.
        Utwórz dwie listy a i b. Sprawdź czy listy te mają chociaż jeden wspólny element.

    """

    def __init__(self, szkolenie, zadanie, napis1, napis2):
        super().__init__(szkolenie, zadanie)
        self.napis1 = napis1
        self.napis2 = napis2
        self.lista1 = self.utworz_liste(self.napis1)
        print(self.lista1)
        self.lista2 = self.utworz_liste(self.napis2)
        print(self.lista2)
        self.wspolny = self.czy_wspolny()
        self.wyswietl_odp()

    def utworz_liste(self, napis):
        lista = list(napis.split())
        return lista

    def czy_wspolny(self):
        czy_wspolny = any(element in self.lista1 for element in self.lista2)
        return czy_wspolny

    def wyswietl_odp(self):
        if self.czy_wspolny():
            print("Listy maja wspólny element")
        else:
            print("Listy nie mają wspólnego elementu")
