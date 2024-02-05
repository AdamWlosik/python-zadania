import datetime
import random

from PodstawySzkolenie.c_PodstawyPetle import Szkolenie4
from PodstawySzkolenie.a_PodstawySzkolenie import Szkolenie1
from PodstawySzkolenie.b_PodstawySzkolenie3_1StringiRozszerzenie import Szkolenie2
from PodstawySzkolenie.c_PodstawyInstrukcjeWarunkowe import Szkolenie3
from PodstawySzkolenie.d_PodstawyKrotkiIZbioryRozszerzenie import Zadanie1KZ, Zadanie2KZ, Zadanie3KZ, Zadanie4KZ
from PodstawySzkolenie.e_PodstawySlownikiRozszerzenie import Zadanie1S, Zadanie3S, Zadanie4S, Zadanie5S, Zadanie6S, \
    Zadanie7S, Zadanie8S
from PodstawySzkolenie.f_PodstawyListyRozszerzenie import Zadanie1LR, Zadanie2LR, Zadanie3LR, Zadanie4LR, Zadanie5LR
from PodstawySzkolenie.g_PodstawyPetleRozszerzenie import Zadanie1PPR, Zadanie2PPR, Zadanie3PPR, Zadanie4PPR, \
    Zadanie5PPR, Zadanie6PPR, Zadanie7PPR
from PodstawySzkolenie.h_PodstawyStrukturyDanychRozszerzenie import Zadanie1PSDR, Zadanie2PSDR, Zadanie3SPDR, \
    Zadanie4PSDR, Zadanie5PSDR, Zadanie6PSDR
from PodstawySzkolenie.i_Podstawy_Szkolenie_7 import Zadanie1PS7, Zadanie3PS7, Zadanie4PS7, Zadanie5PS7, Zadanie6PS7, \
    Zadanie7PS7, Zadanie8PS7
from PodstawySzkolenie.j_Podstawy_Szkolenie_8 import Zadanie1PS8, Zadanie2PS8, Zadanie3PS8, Zadanie4PS8, Zadanie5PS8, \
    Zadanie6PS8, Zadanie7PS8, Zadanie8PS8, Zadanie9PS8
from PodstawySzkolenie.k_Podstawy_Szkolenie_9 import Zadanie1PS9, Zadanie2PS9, Zadanie3PS9, Zadanie4PS9, Zadanie5PS9, \
    Zadanie6PS9, Zadanie8PS9, Zadanie7PS9, Zadanie9PS9
from PodstawySzkolenie.l_12_Podstawy_Szkolenie_10 import Zadanie1PS10, Zadanie2PS10


def main():
    while True:
        try:
            szkolenie = int(input("\nAby zakończyć wybierz 0 lub wprowadź numer szkolenia: "))
            if szkolenie == 0:
                break
            zadanie = int(input("Wprowadź numer zadania: "))
        except ValueError:
            print("Prosze nie psuć!")
            continue

        if szkolenie == 1:
            szkolenie = str(szkolenie) + ": PodstawySzkolenie"
            szkolenie1 = Szkolenie1(szkolenie, zadanie)

            if zadanie == 1:
                print(szkolenie1.zad1())
            elif zadanie == 2:
                szkolenie1.zad2()
            elif zadanie == 3:
                liczba1 = input("Podaj I składnik sumy: ")
                liczba2 = input("Podaj II składnik sumy: ")
                print(szkolenie1.zad3(liczba1, liczba2))
                print("Operacje są niepoprawne ponieważ dodajemy liczby int w postaci str")
            elif zadanie == 4:
                szkolenie1.zad4()
            elif zadanie == 5:
                szkolenie1.zad5([5, -1, 0, 0.0, -1.123, "c", 'c', "programowanie", False, True])
            elif zadanie == 6:
                szkolenie1.zad6()
            elif zadanie == 7:
                # tutaj chyba jest błąd w poleceniu, bo nie wiem po co są zmienne z moim wiekiem i wzrostem
                moj_wzrost = 182
                moj_wiek = 27
                try:
                    wzrost = int(input("Podaj wzrost: "))
                    waga = int(input("Podaj waga: "))
                    bmi = szkolenie1.zad7(wzrost, waga)
                except ValueError:
                    print("nie psuj!")
                print(bmi)
            elif zadanie == 8:
                szkolenie1.zad8("dzielenie", 5, 2)
                szkolenie1.zad8("dodawanie", 1, 1)
                szkolenie1.zad8("dodawanie", 1.0, 1.0)
                szkolenie1.zad8("dodawanie", 2.0, 2.0)
                szkolenie1.zad8("dodawanie", "napis", 1)
                szkolenie1.zad8("dodawanie", "napis", "napis")
                szkolenie1.zad8("dodawanie", True, True)
                szkolenie1.zad8("modulo", 5, 2)
                szkolenie1.zad8("modulo", 10, 2)
                szkolenie1.zad8("modulo", 20, 30)
                szkolenie1.zad8("modulo", 100, 3)
                szkolenie1.zad8("dzielenie calkowite", 100, 3)
                szkolenie1.zad8("dzielenie calkowite", 5, 3)
                szkolenie1.zad8("dzielenie calkowite", 1, 3)
                szkolenie1.zad8("potegowanie", 3, 3)
                szkolenie1.zad8("potegowanie", 2, 2)
                szkolenie1.zad8("potegowanie", 2, 0)
            elif zadanie == 9:
                # w przykładie zamienia przed ostatni znak "d" zamiast osatniego "!" jakie jest poprawne rozwiązanie?
                napis = input("Wprowadź dowoly napis: ")
                print(szkolenie1.zad9(napis))
                print("Możemy działać jedynie na orginalnym napisie lub utworzyć nową zmienna")
            elif zadanie == 10:
                a = 5
                b = 6
                print(szkolenie1.zad10(a, b))
            elif zadanie == 11:
                imie1 = "Kacper"
                imie2 = "Lucjan"
                print(szkolenie1.zad11(imie1, imie2))
            elif zadanie == 12:
                szkolenie1.zad12()
            elif zadanie == 13:
                szkolenie1.zad13()
            elif zadanie == 14:
                szkolenie1.zad14()

        elif szkolenie == 2:
            szkolenie = str(szkolenie) + ": PodstawySzkolenie3_1StringiRozszerzenie"
            szkolenie2 = Szkolenie2(szkolenie, zadanie)

            if zadanie == 1:
                tekst = input("Wprowadź dowolny tekst zawierający conajmniej 7 znaków: ")
                if len(tekst) < 7:
                    print("Podany tekst ma mniej niż 7 znaków")
                    continue
                else:
                    szkolenie2.zad1(tekst)
            elif zadanie == 2:
                szkolenie2.zad2()
            elif zadanie == 3:
                szkolenie2.zad3()
            elif zadanie == 4:
                slowo = input("Podaje dowolne słowo: ")
                print(szkolenie2.zad4(slowo))
            elif zadanie == 5:
                napis = input("Podaj dowolny napis zawierający na początku 5 białych znaków: ")
                if napis[:5].isspace():
                    print(szkolenie2.zad5(napis))
                else:
                    print("Napis nie zawiera 5 białych znaków na początku")
                    continue
            elif zadanie == 6:
                kolory = input("Podaj 5 dowolnych kolorów oddzielonych przecinkami: ")
                print(szkolenie2.zad6(kolory))

        elif szkolenie == 3:
            szkolenie = str(szkolenie) + ": PodstawyInstrukcjeWarunkowe"
            szkolenie3 = Szkolenie3(szkolenie, zadanie)

            if zadanie == 1:
                try:
                    bok1, bok2, bok3 = map(int, input("Podaj 3 długości boków trójkąta oddzielone spacją: ").split())
                except ValueError:
                    print("Nie psuj!")
                    continue
                szkolenie3.zad1(bok1, bok2, bok3)
            elif zadanie == 2:
                try:
                    liczba = int(input("Podaj liczbę: "))
                except ValueError:
                    print("Nie psuj!")
                    continue
                print(f"liczba {szkolenie3.zad2(liczba)}")
            elif zadanie == 3:
                try:
                    liczby = map(int, input("Podaj 3 liczby oddzielone spacją: ").split())
                except ValueError:
                    print("Nie psuj!")
                    continue
                print(szkolenie3.zad3(liczby))
            elif zadanie == 4:
                slowo1 = input("Użytkownik 1 podaje papier, kamień, nożyce: ")
                slowo2 = input("Użytkownik 2 podaje papier, kamień, nożyce: ")
                dostepne_wybory = ["kamień", "papier", "nożyce"]
                if slowo1 not in dostepne_wybory or slowo2 not in dostepne_wybory:
                    print("Błędne dane!")
                    continue
                else:
                    szkolenie3.zad4(slowo1, slowo2)
            elif zadanie == 5:
                try:
                    liczby = map(int, input("Podaj diwe liczby oddzielone spacją: ").split())
                except ValueError:
                    print("Nie psuj!")
                szkolenie3.zad5(liczby)
            elif zadanie == 6:
                punkty_gracza = 0
                punkty_komputera = 0
                while True:
                    wybor = input('Jeśli chcesz wybrać orła wciśnij "o" \n'
                                  'Jeśli chcesz wybrać reszkę wciśnij "r" \n')
                    opcje = ["r", "o"]
                    if wybor not in opcje:
                        print("Błędny wybór")
                        continue
                    else:
                        wylosowano = szkolenie3.zad6_losowanie(opcje)
                        punktacja = szkolenie3.zad6_punktacja(wylosowano, wybor, punkty_gracza, punkty_komputera)
                        punkty_gracza = punktacja[0]
                        punkty_komputera = punktacja[1]
                    print(f"Punkty gracza: {punkty_gracza}, punkty komputera: {punkty_komputera}")
                    koniec = input("Czy chcesz zagrać raz jeszcze? t - zagrajmy, n - zakończy rozgrywkę: ").lower()
                    if koniec == "t":
                        continue
                    elif koniec == "n":
                        break
                    else:
                        print("Nie psuj!")
                        break

        elif szkolenie == 4:
            szkolenie = str(szkolenie) + ": PodstawyPetle"
            szkolenie4 = Szkolenie4(szkolenie, zadanie)

            if zadanie == 1:
                try:
                    y = int(input("Podaj koniec przedziału: "))
                except ValueError:
                    print("Nie psuj")
                szkolenie4.zad1_while(y)
                szkolenie4.zad1_for(y)
            elif zadanie == 2:
                szkolenie4.zad2_while(100, 50)
                szkolenie4.zad2_for(100, 50)
            elif zadanie == 3:
                szkolenie4.zad3(0, 100)
            elif zadanie == 4:
                try:
                    n = int(input("Podaj liczbę n: "))
                except ValueError:
                    print("Nie psuj!")
                szkolenie4.zad4(n)
            elif zadanie == 5:
                try:
                    poczatek, koniec, dzielnik = map(int, input("Podaj początek i koniec przedziału oraz "
                                                                "dzielnik rozdzielone spacją: ").split())
                except ValueError:
                    print("Nie psuj!")
                    continue
                szkolenie4.zad5(poczatek, koniec, dzielnik)
            elif zadanie == 6:
                warunek = True
                suma = 0
                stara_liczba = False
                while warunek:
                    try:
                        liczba = int(input("Podaj liczbę: "))
                    except ValueError:
                        print("Nie psuj!")
                    suma = szkolenie4.zad6_suma(suma, liczba)
                    print(f"Suma = {suma}")
                    warunek = szkolenie4.zad6_war(stara_liczba, liczba)
                    stara_liczba = liczba
            elif zadanie == 7:
                print("a: ")
                szkolenie4.zad7_a()
                print("b: ", end="")
                szkolenie4.zad7_b(4)
                print("c: ")
                szkolenie4.zad7_c(3, 3)
                print("d: ")
                szkolenie4.zad7_d(5)
                print("d z wykorzystaniem center(): ")
                szkolenie4.zad7_d_center(5)
            elif zadanie == 8:
                liczby = 10
                suma = szkolenie4.zad8_suma(liczby)
                print(f"Średnia = {szkolenie4.zad8_srednia(suma, liczby)}")
            elif zadanie == 9:
                poziom_paliwa = 0
                ilosc_astronautow = 0
                wysokosc = 0
                # osobna deklaracja tych zmiennych w pythonie chyba nie ma sensu,
                # w javie byłoby to konieczne, ale tu chyba nie
                maximum_paliwo = 30000
                minimum_paliwo = 500
                max_astro = 7
                min_astro = 1
                war = True
                odleglosc_orbity = 2000
                poziom_paliwa = szkolenie4.zad9_paliwo(minimum_paliwo, maximum_paliwo, war)
                ilosc_astronautow = szkolenie4.zad9_astro(war, min_astro, max_astro)
                dystans = szkolenie4.zad9_lot(poziom_paliwa, ilosc_astronautow)
                print(f"Statek kosmiczny {szkolenie4.zad9_dolecial(dystans, odleglosc_orbity)} do orbity")
            elif zadanie == 10:
                liczba = szkolenie4.zad10_liczba()
                dzielniki = szkolenie4.zad10_dzielniki(liczba)
                doskonala = szkolenie4.zad10_doskonala(liczba, dzielniki)
                print(doskonala)

        elif szkolenie == 5:

            # TODO
            print("6 Podstawy Szkolenie 4 - 6, Do zrobienia później ")

        elif szkolenie == 6:
            szkolenie = str(szkolenie) + ": PodstawyKrotkiIZbioryRozszerzenie"

            if zadanie == 1:
                kolor = "zolty"
                zadanie1 = Zadanie1KZ(szkolenie, zadanie, kolor)
                # tak wiem przerost formy nad treścia ale wyrabiam nawyk pisana wszystkiego
                # w ten spsób nie wiem, czy to dobrze?
                lista = zadanie1.utworz_lista()
                zbior = zadanie1.utworz_zbior()
                print(f"Lista zawiera {zadanie1.suma_elementow()} elementow")
                print(f"Zostało użytych {zadanie1.suma_unikalnych_elementow(zbior)} różnych kolorów")
                print(f"Dodałem do zbioru kolor {kolor} \n"
                      f"zbiór: {zadanie1.zbior_dodaj(zbior)}")
                print(f"Usunąłem ze zbioru kolor {kolor} \n"
                      f"zbior: {zadanie1.zbior_usun(zbior)}")
            elif zadanie == 2:
                zadanie2 = Zadanie2KZ(szkolenie, zadanie)
                zdanie = zadanie2.wczytaj()
                bez_interpunkcji = zadanie2.usun_interpunkcje(zdanie)
                print(f"Zdanie bez interpunkcji: {bez_interpunkcji}")
                krotka = zadanie2.tworzenie_krotki(bez_interpunkcji)
                print(f"Krotka: {krotka}")
                print(f"Krotka zawiera {zadanie2.zlicz_wyrazy(krotka)} elementów ")
                nowe_zdanie = zadanie2.wyswielt_wyrazy(krotka)
                print(f"Wyświetlam wszystkie wyrazy ze zdania w jednej lini: \n"
                      f"{nowe_zdanie}")
                zbior = zadanie2.utworz_zbior(nowe_zdanie)
                print(f"Zbior: {zbior}")
                wyswietlone_wyrazy1 = zadanie2.wyswietl_wybrany_wyraz_zbioru(zbior, 1, 4)
                print(f"Suma unikatowych wyrazów w zdaniu: {zadanie2.zlicz_unikatowe(zbior)}")
                unikatowe_zdanie = zadanie2.wyswietl_unikatowe_wyrazy(zbior)
                print(f"Unikatowe wyrazy w zdaniu: {unikatowe_zdanie}")
                zbior2 = zadanie2.utworz_zbior(unikatowe_zdanie)
                print(f"Zbiór2: {zbior2}")
                wyswietlone_wyrazy2 = zadanie2.wyswietl_wybrany_wyraz_zbioru(zbior2, 1, 4)
                print(f"Elementy nie muszą być takie same ponieważ zbiory mają nie uporządkowaną kolejność \n"
                      f"{zadanie2.czy_wyswietlone_wyraz_takie_same(wyswietlone_wyrazy1, wyswietlone_wyrazy2)}")
                # coś jest nie tak, bo za każdym razem są takie same, ale dużo zadań przede mną take wrócić
            elif zadanie == 3:
                zadanie3 = Zadanie3KZ(szkolenie, zadanie)
                # print(zadanie3.__class__.__doc__)
                zadanie3.rozwiazanie()
                zadanie3._podaj_kolory()
            elif zadanie == 4:
                zadanie4 = Zadanie4KZ(szkolenie, zadanie)
                print(f"Zbiór A składa się z {zadanie4.zlicz_element(zadanie4.zbiorA)} elementów i zawiera:"
                      f" {zadanie4.zbiorA}")
                print(f"Zbiór B składa się z {zadanie4.zlicz_element(zadanie4.zbiorB)} elementów i zawiera:"
                      f" {zadanie4.zbiorB}")
                zbiorC = zadanie4.utworz_zbiorC()
                print(f"Zbiór C składa się z {zadanie4.zlicz_element(zbiorC)} elementów i zawiera: {zbiorC}")
                zbiorD = zadanie4.utworz_zbiorD()
                print(f"Zbiór D składa się z {zadanie4.zlicz_element(zbiorD)} elementów i zawiera: {zbiorD}")
                zbiorE = zadanie4.utworz_zbiorE()
                print(f"Zbiór E składa się z {zadanie4.zlicz_element(zbiorE)} elementów i zawiera: {zbiorE}")
                zbiorF = zadanie4.utworz_zbiorF()
                print(f"Zbiór F składa się z {zadanie4.zlicz_element(zbiorF)} elementów i zawiera: {zbiorF}")

        elif szkolenie == 7:
            szkolenie = str(szkolenie) + ": PodstawySlownikiRozszerzenie"
            if zadanie == 1:
                zadanie1 = Zadanie1S(szkolenie, zadanie)
            elif zadanie == 2:
                zadanie2 = Zadanie1S(szkolenie, zadanie)
            elif zadanie == 3:
                tekst = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and " \
                        "curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a " \
                        "tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered," \
                        " tapping at my chamber door - Only this, and nothing more."
                zadanie3 = Zadanie3S(szkolenie, zadanie, tekst)
            elif zadanie == 4:
                slownik = {'kos': 'Turdus merula', 'wilga': 'Oriolus oriolus', 'rudzik': 'Erithacus rubecula',
                           'kukulka': 'Cuculus canorus', 'pleszka': 'Phoenicurus phoenicurus',
                           'bogatka': 'Parus major', 'drozd': 'Turdus philomelos', 'zieba': 'Fringilla coelebs',
                           'dzwoniec': 'Chloris chloris', 'szczygiel': 'Carduelis carduelis',
                           'szpak': 'Sturnus vulgaris', 'kopciuszek': 'Phoenicurus ochruros'}

                tekst = "W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik," \
                        " a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi" \
                        " sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja" \
                        " pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko" \
                        " w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek." \
                        " Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel."
                zadanie4 = Zadanie4S(szkolenie, zadanie, slownik, tekst)
            elif zadanie == 5:
                try:
                    n = int(input("Podaj liczbę n: "))
                except ValueError:
                    print("Nie psuj!")
                zadanie5 = Zadanie5S(szkolenie, zadanie, n)
                print(zadanie5.slownik)
            elif zadanie == 6:
                zadanie6 = Zadanie6S(szkolenie, zadanie)
                print(zadanie6.odpowiedz)
            elif zadanie == 7:
                lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
                friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}
                zadanie7 = Zadanie7S(szkolenie, zadanie, lovers, friends)
                print(zadanie7.scalony_slownik)
            elif zadanie == 8:
                slownik = {"V": "S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX": "S005", "X": "S009",
                           "XI": "S007"}
                zadanie8 = Zadanie8S(szkolenie, zadanie, slownik)
                print(zadanie8.lista_unikalnych)

        elif szkolenie == 8:
            szkolenie = str(szkolenie) + ": PodstawyListyRozszerzenie"
            if zadanie == 1:
                zdanie = input("Podaj dowolne zdanie ze znakami interpunkcyjnymi: ")
                zadanie1 = Zadanie1LR(szkolenie, zadanie, zdanie)
                print(f"Odwrócona lista bez interpunkcji: {zadanie1.lista}")
            elif zadanie == 2:
                wynik = [12, 1, 45, 76, 50, 23]
                min_losowanie = 1
                max_losowanie = 49
                zadanie2 = Zadanie2LR(szkolenie, zadanie, wynik, min_losowanie, max_losowanie)
                print(f"Nowe wyniki: {zadanie2.nowe_wyniki}")
            elif zadanie == 3:
                lista1 = ["abc", "def", "ghi", "jkl"]
                lista2 = [1, 2, 3, 4, 5]
                lista3 = ["xyz", 1, '2']
                zadanie3 = Zadanie3LR(szkolenie, zadanie, lista1, lista2, lista3)
                wartosc = input("Wprowadź wartość do przypisania: ")
                print(f"Lista3 z przypisane wartością z klawiatury:"
                      f" {zadanie3.przypisz_wartosc_z_klawiatury(zadanie3.lista3, 2, wartosc)}")
                print(f"Lista1 z dodanym metoda .append(), wyrazem 'slowo': "
                      f"{zadanie3.dodaj_append('slowo', zadanie3.lista1)}")
                print(f"Lista1 ze skasowanym elementem: "
                      f"{zadanie3.skasuj_element(1, zadanie3.lista1)}")
                print(f"Liczba elementów listy3: "
                      f"{zadanie3.liczba_elementow(zadanie3.lista3)}")
                print(f"Lista1 powiększona o elementy listy3: "
                      f"{zadanie3.polacz(zadanie3.lista1, zadanie3.lista3)}")
            elif zadanie == 4:
                imiona = input("Podaj imiona oddzielone spacja: ")
                zadanie4 = Zadanie4LR(szkolenie, zadanie, imiona)
            elif zadanie == 5:
                zdanie = input("Wpisz zdanie: ")
                sprawdzenie = ["i", "w", "na", "pod", "dla"]
                zadanie5 = Zadanie5LR(szkolenie, zadanie, zdanie, sprawdzenie)

        elif szkolenie == 9:
            szkolenie = str(szkolenie) + ": PodstawyPetleRozszerzenie"
            if zadanie == 1:
                zadanie1 = Zadanie1PPR(szkolenie, zadanie)
            elif zadanie == 2:
                wyraz = input("Podaj wyraz, który chcesz sprawdzić czy palindromem: ")
                zadanie2 = Zadanie2PPR(szkolenie, zadanie, wyraz)
            elif zadanie == 3:
                osoby = "Adam, Stanisław, Joanna, Kornelia, Kacper"
                zadanie3 = Zadanie3PPR(szkolenie, zadanie, osoby)
            elif zadanie == 4:
                zakres_min = 1000
                zakres_max = 10000
                zadanie4 = Zadanie4PPR(szkolenie, zadanie, zakres_min, zakres_max)
            elif zadanie == 5:
                zamowienia = {"Klient_1335": {"nazwa_potrawy": "rosół", "ocena": 5, "rachunek": 20.0},
                              "Klient_222": {"nazwa_deseru": "lody waniliowe", "rachunek": 5.0}}
                zadanie5 = Zadanie5PPR(szkolenie, zadanie, zamowienia)
            elif zadanie == 6:
                try:
                    liczba = int(input("Wprowadź liczbę: "))
                except ValueError:
                    print("Nie psuj")

                zadanie6 = Zadanie6PPR(szkolenie, zadanie, liczba)
            elif zadanie == 7:
                try:
                    n = int(input("Podaj ile pierwszych wyrazu ciągu chcesz wyznaczyć: "))
                except ValueError:
                    print("Nie psuj")
                fibo = [0, 1]
                zadanie7 = Zadanie7PPR(szkolenie, zadanie, n, fibo)

        elif szkolenie == 10:
            szkolenie = str(szkolenie) + ": PodstawyStrukturyDanychRozszerzenie"
            if zadanie == 1:
                lista1 = input("Wprowadź elementy oddzielone spacją listy1: ")
                lista2 = input("Wprowadź elementy oddzielone spacją listy2: ")
                zadanie1 = Zadanie1PSDR(szkolenie, zadanie, lista1, lista2)
            elif zadanie == 2:
                ile_elementow = 15
                przedzial_min = 5
                przedzial_max = 120
                zadanie2 = Zadanie2PSDR(szkolenie, zadanie, ile_elementow, przedzial_min, przedzial_max)
            elif zadanie == 3:
                slownik = {"a": 3, "b": 1, "c": 10, "d": 15, "e": 20}
                zadanie3 = Zadanie3SPDR(szkolenie, zadanie, slownik)
            elif zadanie == 4:
                zadanie4 = Zadanie4PSDR(szkolenie, zadanie)
            elif zadanie == 5:
                lista = [
                    ['Tom', 'Calamari', 6.00],
                    ['Tom', 'American Hot', 11.50],
                    ['Tom', 'Chocolate Fudge Cake', 4.45],
                    ['Clare', 'Bruschetta Originale', 5.35],
                    ['Clare', 'Fiorentina', 10.65],
                    ['Clare', 'Tiramisu', 4.90],
                    ['Rich', 'Bruschetta Originale', 5.35],
                    ['Rich', 'La Reine', 10.65],
                    ['Rich', 'Honeycomb Cream Slice', 4.90],
                    ['Rosie', 'Garlic Bread', 4.35],
                    ['Rosie', 'Veneziana', 9.40],
                    ['Rosie', 'Tiramisu', 4.90],
                ]
                zadanie5 = Zadanie5PSDR(szkolenie, zadanie, lista)
            elif zadanie == 6:
                dane = {
                    "data": [1, 2, 'asd', [2, 3, 4, 5]],
                    'nested_analysis': {
                        'analysis_1': [1, 10, 15, 120.2, '120'],
                        'analysis_2': [10, 100, "test", 200, 300],
                    },
                    'probes': [['probe_1', 'probe_2'], 'probe_3']
                }
                zadanie6 = Zadanie6PSDR(szkolenie, zadanie, dane)
                # TODO

        elif szkolenie == 11:
            szkolenie = str(szkolenie) + ": PodstawySzkolenie7"
            if zadanie == 1:
                nums = [4, 6, 8, 24, 12, 2]
                zadanie1 = Zadanie1PS7(szkolenie, zadanie, nums)
                print(f"Index największego elementy to : {zadanie1.index}")
            if zadanie == 2:
                print("Odpwoiedź w classie Zadanie2PS7 dodana jako komentarz")
            elif zadanie == 3:
                try:
                    liczba = int(input("Podaj liczbe: "))
                except ValueError:
                    print("Nie psuj")
                zadanie3 = Zadanie3PS7(szkolenie, zadanie, liczba)
                print(zadanie3.wynik)
            elif zadanie == 4:
                zadanie4 = Zadanie4PS7(szkolenie, zadanie)
                print(f"{zadanie4.iloczyn(1, 2, 3, 4, 5, 6)}")
            elif zadanie == 5:
                lista_parzyste = [2, 4, 6, 8, 10]
                lista_nieparzyste = [1, 3, 5, 7, 9]
                zadanie5 = Zadanie5PS7(szkolenie, zadanie, lista_parzyste, lista_nieparzyste)
                print(zadanie5.wynik)
            elif zadanie == 6:
                lista = []
                for _ in range(10):
                    lista.append(random.randint(0, 20))
                print(lista)
                zadanie6 = Zadanie6PS7(szkolenie, zadanie, lista)
                print(zadanie6.wynik)
            elif zadanie == 7:
                zadanie7 = Zadanie7PS7(szkolenie, zadanie)
            elif zadanie == 8:
                godzina_minuta = datetime.datetime.now()
                godzina = godzina_minuta.hour
                minuta = godzina_minuta.minute
                zadanie8 = Zadanie8PS7(szkolenie, zadanie, godzina, minuta)
                print(f"Aktualna godzina: {godzina}\n"
                      f"Aktualna minuta: {minuta}\n"
                      f"Kąt między nimi: {zadanie8.kat}")

        elif szkolenie == 12:
            if zadanie == 1:
                zadanie1 = Zadanie1PS8(szkolenie, zadanie)
                zadanie1.rozwiazanie()
            elif zadanie == 2:
                zadanie2 = Zadanie2PS8(szkolenie, zadanie)
                zadanie2.rozwiazanie()
            elif zadanie == 3:
                zadanie3 = Zadanie3PS8(szkolenie, zadanie)
                zadanie3.rozwiazanie()
            elif zadanie == 4:
                zadanie4 = Zadanie4PS8(szkolenie, zadanie)
                zadanie4.rozwiazanie()
            elif zadanie == 5:
                zadanie5 = Zadanie5PS8(szkolenie, zadanie)
                zadanie5.rozwiazanie()
            elif zadanie == 6:
                zadanie6 = Zadanie6PS8(szkolenie, zadanie)
                zadanie6.rozwiazanie()
            elif zadanie == 7:
                zadanie7 = Zadanie7PS8(szkolenie, zadanie)
                # zadanie7.rozwiazanie()
                zadanie7.rozwiazanie_OrderDict()
            elif zadanie == 9:
                zadanie9 = Zadanie9PS8(szkolenie, zadanie)
                zadanie9.rozwiazanie()
            elif zadanie == 8:
                zadanie8 = Zadanie8PS8(szkolenie, zadanie)
                zadanie8.rozwiazanie()

        elif szkolenie == 13:
            if zadanie == 1:
                zadanie1 = Zadanie1PS9(szkolenie, zadanie, "Adam", "Włosik",
                                       6273, "Infomratyka")
                zadanie1.rozwiazanie()
            elif zadanie == 2:
                zadanie2 = Zadanie2PS9(szkolenie, zadanie, 100.12)
                zadanie2.rozwiazanie()
            elif zadanie == 3:
                zadanie3 = Zadanie3PS9(szkolenie, zadanie, 10, 5)
                zadanie3.rozwiazanie()
            elif zadanie == 4:
                zadanie4 = Zadanie4PS9(szkolenie, zadanie, 1111, "Adam", 100)
                zadanie4.rozwiazanie()
            elif zadanie == 5:
                zadanie5 = Zadanie5PS9(szkolenie, zadanie)
                zadanie5.rozwiazanie()
                # TODO
                # pytanie do zadania w klasie
            elif zadanie == 6:
                zadanie6 = Zadanie6PS9(szkolenie, zadanie)
                zadanie6.rozwiazanie()
            elif zadanie == 8:
                zadanie8 = Zadanie8PS9(szkolenie, zadanie)
                zadanie8.rozwiazanie()
            elif zadanie == 7:
                zadanie7 = Zadanie7PS9(szkolenie, zadanie)
                zadanie7.rozwiazanie()
            elif zadanie == 9:
                zadanie9 = Zadanie9PS9(szkolenie, zadanie)
                zadanie9.rozwiazanie()
        elif szkolenie == 14:
            if zadanie == 1:
                zadanie1 = Zadanie1PS10(szkolenie, zadanie)
                zadanie1.rozwiazanie()
            elif zadanie == 2:
                zadanie2 = Zadanie2PS10(szkolenie, zadanie)
                zadanie2.rozwiazanie()


if __name__ == "__main__":
    main()
