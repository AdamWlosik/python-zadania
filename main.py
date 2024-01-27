from PodstawySzkolenie.PodstawyPetle import Szkolenie4
from PodstawySzkolenie.PodstawySzkolenie import Szkolenie1
from PodstawySzkolenie.PodstawySzkolenie3_1StringiRozszerzenie import Szkolenie2
from PodstawySzkolenie.PodstawyInstrukcjeWarunkowe import Szkolenie3


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


if __name__ == "__main__":
    main()
