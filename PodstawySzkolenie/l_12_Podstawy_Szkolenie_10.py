from pprint import pprint, pformat

from PodstawySzkolenie.Szkolenie import Szkolenie
from helpers import print_doc


class Zadanie1PS10(Szkolenie):
    """Zad 1.
        Stwórz klasę Shape i jej podklasę Square. Square ma posiadać konstruktor, który przyjmie length jako argument.
        Obie klasy mają posiadać metodę obliczającą pole figury. Domyślnie Shape ma zwracać wartość 0.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        square = Square(5)
        print("Pole kwadratu: ", square.calculate_area())


class Shape:

    def __init__(self):
        pass

    def calculate_area(self):
        return 0


class Square(Shape):
    def __init__(self, lenght):
        super().__init__()
        self.length = lenght

    def calculate_area(self):
        return self.length ** 2


class Zadanie2PS10(Szkolenie):
    """Zad 2.
        Zaprojektuj z użyciem koncepcji dziedziczenia hierarchię klas opisujących pojazdy komunikacji
        miejskiej. Wyraź w tej hierarchii następujące fakty:

        1. wszystkie pojazdy komunikacji miejskiej (k. m.) są pojazdami,
        2. komunikacja miejska używa tramwajów i autobusów,
        3. pojazdy są garażowane w zajezdniach, odpowiednio tramwajowych i autobusowych,
        4. każdy pojazd zna swoją szybkość maksymalną,
        5. każdy pojazd k. m. zna swój numer,
        6. każdy pojazd k. m. zna swoją zajezdnię,
        7. każdy tramwaj jest zestawem 1 do 3 wagonów (i wie, z ilu wagonów się składa),
        8. każdy autobus wie, ile zużył paliwa w bieżącym miesiącu,
        9. każda zajezdnia wie, jakie pojazdy do niej należą,
        10. każda zajezdnia ma nazwę.

        Każdy pojazd powinien mieć możliwość podawania swojego opisu w postaci napisu.
        Opis ma zawierać wszystkie informacje, które zna dany pojazd (np. numer, czy szybkość maksymalną).
        Opis zajezdni to nazwa zajezdni, jej typ i opisy poszczególnych pojazdów.
        Zajezdnia autobusowa podaje dodatkowo sumaryczne zużycie paliwa w bieżącym miesiącu,
        a tramwajowa ogólną liczbę wagonów.
        Do prezentowania informacji o obiekcie, wykorzystaj metodę specjalną __str__().

        Napisz program, który utworzy kilka obiektów reprezentujących wszystkie pojazdy i dwie zajezdnie
        (autobusową i tramwajową), przydzieli pojazdy do zajezdni, a następnie wypisze opis obu zajezdni.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        tramwaj1 = Tramwaj(100, 1, 3)
        tramwaj2 = Tramwaj(96, 2, 1)
        tramwaj3 = Tramwaj(85, 3, 2)
        autobus1 = Autobus(50, 1, 200)
        autobus2 = Autobus(50, 2, 220)
        autobus3 = Autobus(50, 3, 250)
        zajezdnia_autobusowa = ZajezdniaAutobusowa("Zajezdnia Autobusowa")
        zajezdnia_autobusowa.dodaj_pojazd(autobus1)
        zajezdnia_autobusowa.dodaj_pojazd(autobus2)
        zajezdnia_autobusowa.dodaj_pojazd(autobus3)
        print(zajezdnia_autobusowa)
        zajezdnia_tramwajowa = ZajezdniaTramwajowa("Zajezdnia Tramwajowa")
        zajezdnia_tramwajowa.dodaj_poojazd(tramwaj1)
        zajezdnia_tramwajowa.dodaj_poojazd(tramwaj2)
        zajezdnia_tramwajowa.dodaj_poojazd(tramwaj3)
        print(zajezdnia_tramwajowa)


class Pojazdy:

    def __init__(self, szybkosz_maksymalna):
        self.szybkosc_maksymalna = szybkosz_maksymalna


class Zajezdnia:

    def __init__(self, nazwa):
        self.nazwa = nazwa


class ZajezdniaTramwajowa(Zajezdnia):

    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.pojazdy = []

    def dodaj_poojazd(self, pojazd):
        """Metoda dodająca pojazd do listy pojazdów"""
        self.pojazdy.append(pojazd)

    def sumuj_wagony(self):
        """Metoda sumująca wagony, wszystkich tramwajów z listy """
        suma_wagonow = sum(pojazd.ilosc_wagonow for pojazd in self.pojazdy if isinstance(pojazd, Tramwaj))
        return suma_wagonow

    def __str__(self):
        """Metoda zmieniająca instancje klasy zapisane na liście w czytelnego stringa i drukująca dane
            Celowo nie zmieniałem metody na repr, żeby mieć zapisane dwa rozwiązania """
        opis_pojazdow = [str(pojazd) for pojazd in self.pojazdy]
        return (f"Nazwa zajezdni: {self.nazwa}, Typ: {type(self).__name__}, "
                f"Opis pojazdów: {', '.join(opis_pojazdow)}, \nSumaryczne zużycie paliwa: {self.sumuj_wagony()}")


class ZajezdniaAutobusowa(Zajezdnia):

    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.pojazdy = []

    def dodaj_pojazd(self, pojazd):
        """Metoda dodająca pojazd do listy"""
        self.pojazdy.append(pojazd)

    def sumuj_paliwo(self):
        """Metoda sumująca ilość paliwa wszystkich autobusów z listy"""
        suma_paliwa = sum(pojazd.zuzycie_paliwa for pojazd in self.pojazdy if isinstance(pojazd, Autobus))
        return suma_paliwa

    def __repr__(self):
        """Meotda drukująca dane"""
        return f"Nazwa zajezdni: {self.nazwa}, Typ: {type(self).__name__}, " \
               f"Opis pojazdów: {self.pojazdy}, \nSumaryczne zużycie paliwa: {self.sumuj_paliwo()}"


class KompnikacjaMiejska(Pojazdy):

    def __init__(self, szybkosc_maksymalna, numer):
        super().__init__(szybkosc_maksymalna)
        self.numer = numer


class Autobus(KompnikacjaMiejska):

    def __init__(self, szybkosc_maksymalna, numer, zuzycie_paliwa):
        super().__init__(szybkosc_maksymalna, numer)
        self.zuzycie_paliwa = zuzycie_paliwa

    def __repr__(self):
        """Metoda drukująca dane o pojeździe"""
        return (f"\n Pojazd: {type(self).__name__}, Szybkość maksymalna: {self.szybkosc_maksymalna}, "
                f"Numer: {self.numer}, Zużycie paliwa: {self.zuzycie_paliwa}")


class Tramwaj(KompnikacjaMiejska):

    def __init__(self, szybkosc_maksymalna, numer, ilosc_wagonow):
        super().__init__(szybkosc_maksymalna, numer)
        self.ilosc_wagonow = ilosc_wagonow

    def __str__(self):
        """Metoda drukująca dane o pojeździe"""
        return (f"\n Pojazd: {type(self).__name__}, Szybkość maksymalna: {self.szybkosc_maksymalna}, "
                f"Numer: {self.numer}, Ilość wagonów: {self.ilosc_wagonow}")


class Zadanie4PS10(Szkolenie):
    """Zad 4.
        Napisz program, który będzie wyświetlał Menu z następującymi opcjami:
        1.	Dodaj notatkę
        2.	Dodaj wizytówkę (Card)
        3.	Wyświetl wszystkie notatki
        4.	Wyświetl wszystkie wizytówki
        5.	Wyjdź


        Program ma być podzielony na następujące klasy:
        Manager (który zawierać będzie komponent: Menu, NotesSubManager, CardsSubManager).

        Metody w Manager:
        1.	start - metoda wywoływana jako pierwsza z poziomu main
        2.	show_menu (wtedy metoda odwołuje się do obiektu Menu
            i wywołuje z niej odpowiednią metodą wyświetlającą Menu)
        3.	execute (metoda pobierająca od użytkownika wybór
            i wywołująca odpowiednią metodę z NotesSubManager/CardSubManager)
        4.	show_notes/show_cards (wywołujące metodę show z odpowiedniego SubManagera)

        Metody w Menu:
        1.	show (wyświetlanie menu)
        2.	get_choice (pobieranie wyboru z menu od użytkownika)

        Pola w SubManagerach:
        1.	lista na obiekty reprezentujące dodane Notatki/Wizytówki

        Metody w SubManagerach:
        1.	add (dodawanie odpowiednio notatki lub karty)
        2.	show (wyświetlanie wszystkich notatek lub kart z listy)
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        manager = Manager()
        manager.start()


class Manager:

    def __init__(self):
        self.menu = Menu()
        self.notes_sub_manager = NotesSubManager()
        self.cards_sub_manager = CardsSubManager()

    def start(self):
        """Metoda startowa uruchamiająca metody menu, get_choice i execute"""
        while True:
            self.show_menu()
            choice = self.menu.get_choice()
            self.execute(choice)

    def show_menu(self):
        """Metoda wyświetlająca menu"""
        self.menu.show()

    def execute(self, choice):
        """Metoda przyjmująca wybór użytkownika jako argument"""
        match choice:
            case 1:
                self.notes_sub_manager.add()
            case 2:
                self.cards_sub_manager.add()
            case 3:
                self.notes_sub_manager.show()
            case 4:
                self.cards_sub_manager.show()
            case 5:
                exit()
            case _:
                print("Nieprawidłowy wybór")


class Menu:

    def __init__(self):
        pass

    def show(self):
        """Metoda wyświetlająca opcje z mennu"""
        print("\nMenu:")
        print("1. Dodaj notatkę")
        print("2. Dodaj wizytówkę")
        print("3. Wyświetl wszystkie notatki")
        print("4. Wyświetl wszystkie wizytówki")
        print("5. Wyjdź")

    def get_choice(self):
        """Metoda wczytująca od użtykownika wybraną opcje z menu i zwracająca ten wybór"""
        try:
            choice = int(input("Wybierz opcję: "))
        except ValueError:
            print('Nie psuj')
            exit()
        return choice


class NotesSubManager:

    def __init__(self):
        self.notes_list = []

    def add(self):
        """Metoda służąca do dodania notatki do listy"""
        note = input("Wprowadź notatkę: ")
        self.notes_list.append(note)

    def show(self):
        """Metodaa wyświetlająca liste notatek"""
        print(self.notes_list)


class CardsSubManager:

    def __init__(self):
        self.cards_list = []

    def add(self):
        """Metoda służąca do dodania wizytówki do listy"""
        card = input("Podaj wizytówkę: ")
        self.cards_list.append(card)

    def show(self):
        """Metodaa wyświetlająca liste wizytówek"""
        print(self.cards_list)


class Zadanie3PS10(Szkolenie):
    """Part I: Members, Students and Instructors
        You're starting your own web development school called Codebar!
        Everybody at Codebar - whether they are attending workshops or teaching them - is a Member:

        Each member has a full_name.
        Each member should be able to introduce themselves (e.g., "Hi, my name is Kevin!").
        Each Member is also either a Student or an Instructor:

        Each Student has a reason for attending Codebar (e.g., "I've always wanted to make websites!").
        Each Instructor a bio (e.g., "I've been coding in Python for 5 years and want to share the love!").
        Each Instructor also has a set of skills (e.g., ["Python", "Javascript", "C++"]).
        An Instructor can gain a new skill using add_skill.
        Part II: Workshops
        Codebar also has Workshops. Each Workshop has:

        A date.
        A subject.
        A group of instructors.
        A roster of students.
        An add_participant method that accepts a member as an argument.
        If the Member is an Instructor, add them to the instructors list.
        If a Member is a Student, add them to the students list.
        Create another method print_details that outputs the details of the workshop.

        Bonus
        The print_details method currently does a number of different things,
        like printing out workshop details, the list of Students and the list of Coaches.

        Create separate methods to print the workshop details (date and classroom),
        a method to print out the students and one to print out the coaches.
        Call these from print_details instead of having all the code there."""

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
        workshop = Workshop("12/03/2014", "Shutl")

        jane = Student("Jane Doe", "I am trying to learn programming and need some help")
        lena = Student("Lena Smith", "I am really excited about learning to program!")
        vicky = Instructor("Vicky Python", "I want to help people learn coding.")
        vicky.add_skill("HTML")
        vicky.add_skill("JavaScript")
        nicole = Instructor("Nicole McMillan",
                            "I have been programming for 5 years in Python and want to spread the love")
        nicole.add_skill("Python")

        workshop.add_participant(jane)
        workshop.add_participant(lena)
        workshop.add_participant(vicky)
        workshop.add_participant(nicole)
        workshop.print_details()


class Member:

    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        """Metoda wyświetlająca przywitanie + full_name"""
        print(f"Hi my name is {self.full_name}!")


class Student(Member):

    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason


class Instructor(Member):

    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, skill):
        """Metoda przyjmująca skill i dodająca go do listy"""
        self.skills.append(skill)
        # print(self.skills)


class Workshop:

    def __init__(self, data, subject):
        self.data = data
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, member):
        """Metoda dodająca do listy w zależności od classy"""
        if member.__class__.__name__ == "Instructor":
            self.instructors.append(member)
        elif member.__class__.__name__ == "Student":
            self.students.append(member)

    def print_details(self):
        """Metoda wyświetlająca"""
        print(f"Date: {self.data}, Subject: {self.subject}")
        print("Instructors: ")
        for instrucktor in self.instructors:
            print(f"Name: {instrucktor.full_name}, bio: {instrucktor.bio}")
            for skill in instrucktor.skills:
                print(f"Skills: {skill}")
        print("Students: ")
        for student in self.students:
            print(f"Name: {student.full_name}, Reason: {student.reason}")
