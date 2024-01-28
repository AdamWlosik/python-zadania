from PodstawySzkolenie.c_PodstawyPetle import Szkolenie4
from PodstawySzkolenie.a_PodstawySzkolenie import Szkolenie1
from PodstawySzkolenie.b_PodstawySzkolenie3_1StringiRozszerzenie import Szkolenie2
from PodstawySzkolenie.c_PodstawyInstrukcjeWarunkowe import Szkolenie3
from PodstawySzkolenie.d_Podstawy_Krotki_i_Zbiory_Rozszerzenie import Zadanie1KZ, Zadanie2KZ, Zadanie3KZ, Zadanie4KZ
from PodstawySzkolenie.e_Podstawy_Słowniki_Rozszerzenie import Zadanie1S, Zadanie3S, Zadanie4S


def main():
    while True:
        try:
            szkolenie = int(input("Aby zakończyć wybierz 0 lub wprowadź numer szkolenia: "))
            if szkolenie == 0:
                break
            zadanie = int(input("Wprowadź numer zadania: "))
        except ValueError:
            print("Prosze nie psuć!")
            continue

        if szkolenie == 1:
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
                except ValueError:
                    print("nie psuj!")
                bmi = szkolenie1.zad7(wzrost, waga)
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
                moj_zbior = {'niebieski', 'czerwony', 'zolty', 'zielony'}
                zadanie3 = Zadanie3KZ(szkolenie, zadanie, moj_zbior)
                zbior = zadanie3.utworz_zbior()
                if zadanie3.czy_jednakowe():
                    print("Kolory są jednakowe")
                else:
                    print(f"Kolory wybrane przez dwie osoby: {zadanie3.wspolne_kolory(zbior)}")
                    print(f"Kolory wybrane tylko przez użytkownika: "
                          f"{zadanie3.kolowy_wybrane_tylko_przez_uzytkownika(zbior, moj_zbior)}")
                    print(f"Kolory wybranie tylko przez autora: "
                          f"{zadanie3.kolowy_wybrane_tylko_przez_uzytkownika(moj_zbior, zbior)}")
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

        elif szkolenie == 6:
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


if __name__ == "__main__":
    main()
