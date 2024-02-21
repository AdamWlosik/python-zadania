import re
from helpers import print_doc
from python_zaawansowany.training import Training


class Task1Regex(Training):
    """Zad. 1
        Napisz program, który sprawdzi, czy string zawiera tylko
        i wyłącznie zbiór następujących znaków: (a-z, A-Z i 0-9).
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        text = "Nie tylko odpowiednie znaki!!"
        text2 = "Tylkoodpowiednieznaki234"
        print(self.check(text))
        print(self.check_compile(text))
        print(self.check(text2))
        print(self.check_compile(text2))

    @staticmethod
    def check_compile(text):
        """Metoda kompilująca wzorzec, na podstawie którego szukamy dopasowań"""
        pattern = re.compile(r'^[a-zA-Z0-9]+$')
        return bool(pattern.match(text))

    @staticmethod
    def check(text):
        """Metoda szukająca dopasowań """
        match = re.match(r'^[a-zA-Z0-9]+$', text)
        return bool(match)


class Task2Regex(Training):
    """Zad. 2
        Sprawdź, czy string rozpoczyna się pojedynczą cyfrą: 0 lub literą ‘b’.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def solution(self):
        text = "Nie tylko odpowiednie znaki !!"
        text1 = "0Tylkoodpowiednieznaki234"
        text2 = "bTylkoodpowiednieznaki234"
        print(self.check(text))
        print(self.check(text1))
        print(self.check(text2))

    @staticmethod
    def check(text):
        """Metoda sprawdzająca początek str"""
        return bool(re.match(r'^[0b]', text))


class Task3Regex(Training):
    """Zad. 3
        Sprawdzaj, czy podany string zawiera ciąg dowolnych małych liter rozdzielonych znakiem _, np. aab_cbbbc
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        text = "nie tylko odpowiednie znaki !!"
        text1 = "aab_cbbbc"
        text2 = "bylkoodpow_iednieznaki"
        print(self.check(text))
        print(self.check(text1))
        print(self.check(text2))

    @staticmethod
    def check(text):
        """Metoda sprawdzająca, czy ciąg liter jest rozdzielony _"""
        pattern = r'^[a-z]+_+[a-z]+$'
        return bool(re.match(pattern, text))


class Task4Regex(Training):
    """Zad. 4
        Znajdź słowa, które kończą się co najmniej dwiema literami ‘s’, np.
        -	hiss
        -	hisssss
        -	His
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        text = "hiss hisssss His"
        print(self.find_word_findall(text))
        print(self.find_word_search(text))

    @staticmethod
    def find_word_findall(text):
        """Metoda szukająca słów zakończonych ss przy użyciu findall()"""
        pattern = r'\b\w*ss+\b'
        return re.findall(pattern, text)

    @staticmethod
    def find_word_search(text):
        """Metoda szukająca słów zakończonych ss przy użyciu search() oraz inny sposób zapisu patternu"""
        pattern = r'\S{2}s{2}\S{0,}'
        match = re.search(pattern, text)
        return match.group()


class Task5Regex(Training):
    """Zad. 5
        Znajdź stringa, który zawiera co najmniej sześć liter i nie zawiera litery ‘A’, np.

        -	unique New York
        ale niepasujące:
        -	Regular Expressions
        -	ALOHA
        -	Python should match
        """

    def __init__(self, training, taks):
        super().__init__(training, taks)

    @print_doc
    def solution(self):
        lines = ["unique New York", "Regular Expressions", "ALOHA", "Python should match", "new"]
        for line in lines:
            found = self.found(line)
            if found is not None:
                print(found)

    @staticmethod
    def found(txt):
        """Funkcja zwracająca stringa bez A i z minimum 6 znaków"""
        pattern = r'\b(?!(?:.*a){1})[a-zA-Z]{6,}\b'
        match = re.match(pattern, txt)
        if match is not None:
            return txt


class Task6Regex(Training):
    """Zad. 6
        W stringu HTML, wszystkie elementy otoczone są pewnymi znacznikami HTML (<p>Twój tekst</p>,
        <h1>Twój tekst2</h1> itd.).
        Każdy znacznik ma następującą postać: <znacznik>Tekst</znacznik>.

        Twoje zadanie to określić, czy podany tekst jest prawidłowym elementem kodu HTML,
        czyli czy składa się z odpowiednio skonstruowanych znaczników wraz z dowolnym tekstem pomiędzy nimi.
        Trudność, jaką możesz tutaj napotkać, to konieczność ominięcia, tzw. chciwego przeszukiwania,
        które omówiliśmy w szkoleniu.

        Przykłady:
        <span>Yowza! That’s a great regular expression.</span> - powinno wyszukać cały tekst
        <p>Learn about regular expressions here.</p> <p>You\'re going to love them!</p> - powinno wyszukać:
        -	<p>Learn about regular expressions here.</p>
        -	<p>You\'re going to love them!</p>

        Nieprawidłowe przykłady:
        I'm not HTML!!
        <p>Incomplete HTML
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        txt1 = "<span>Yowza! That’s a great regular expression.</span>"
        txt2 = "<p>Learn about regular expressions here.</p> <p>You\'re going to love them!</p> "
        txt3 = "I'm not HTML!! <p>Incomplete HTML "
        print(self.find_html(txt1))
        print(self.find_html(txt2))
        print(self.find_html(txt3))

    @staticmethod
    def find_html(txt):
        """Metoda sprawdzająca czy podany tekst jest w formie html"""
        pattern = r'<[^<>]+>[^<>]*<\/[^<>]+>'
        return re.findall(pattern, txt)


class Task7Regex(Training):
    """Zad 7.
        Zakładając, że masz dostęp do adresu w formacie: username@companyname.com, napisz program,
        który wydrukuje nazwę firmy z takiego adresu. Zarówno nazwa użytkownika jak
        i nazwa firma może składać się tylko i wyłącznie z liter.
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        address1 = "username@companyname.com"
        address2 = "jan_kowalski@bestcompanyever.com"
        address3 = "example@anothercompany.com"
        print(self.find_company_name(address1))
        print(self.find_company_name(address2))
        print(self.find_company_name(address3))

    @staticmethod
    def find_company_name(address):
        """Metoda wyciagająca nazwę firmy z adresu emial"""
        pattern = re.compile(r'@([a-zA-Z]+)\.com$')
        match = pattern.search(address)
        if match:
            return match.group(1)


class Task8Regex(Training):
    """Zad 8.
        Napisz program, który przyjmować będzie dowolny ciąg znaków oddzielonych spacją.
        Wyodrębnij z niego tylko i wyłącznie te wyrazy, które są liczbami.

        Przykładowo dla poniższych danych wejściowych:
        2 cats and 3 dogs

        Zwróć:
        [‘2’, ‘3’]

        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        txt = "2 cats and 3 dogs"
        print(self.found_numbers(txt))

    @staticmethod
    def found_numbers(txt):
        pattern = re.compile(r'\b\d+\b')
        return pattern.findall(txt)


class Task9Regex(Training):
    """Zad. 9
        Napisz wyrażenie, które sprawdza, czy liczba zmiennoprzecinkowa podana przez użytkownika ma poprawny format.
        Na przykład liczba 123,2341515132135 lub -10 są poprawne, ale 18-12 czy 123, (przecinek na końcu) już nie.
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        numbers = ["123.2341515132135", "-10", "18-12", "123,"]
        for number in numbers:
            print(f"{number}: {self.check_number_format(number)}")

    @staticmethod
    def check_number_format(number):
        """Metoda sprawdzająca czy liczba zmienno przecinkowa ma poprawny format"""
        pattern = re.compile(r'^[+-]?\d*\.?\d+$')
        return bool(pattern.match(number))


class Task10Regex(Training):
    """Zad. 10
        Efektem zbierania pomiarów temperatury okazał być się plik tekstowy,
        który zawiera datę pomiaru oraz wartość.
        W jaki sposób możliwe jest wydzielenie tylko dat w takiej sytuacji?
        Poniżej znajduje się fragment przykładowych danych wejściowych.

        "2019-03-11: 23.5, 19/03/12: 12.7, 2019.03.13: 11.1, 2019-marzec-14: 14.3"
        """
    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        txt = "2019-03-11: 23.5, 19/03/12: 12.7, 2019.03.13: 11.1, 2019-marzec-14: 14.3"
        print(self.find_data(txt))

    @staticmethod
    def find_data(txt):
        """Metoda szukajaca dat w podanym str"""
        pattern = re.compile(r'\b(?:\d{4}|\d{2})[-/.]'
                             r'(?:0[1-9]|1[0-2]|styczeń|luty|marzec|kwiecień|maj|czerwiec|lipiec'
                             r'|sierpień|wrzesień|październik|lisopad|grudzień)'
                             r'[-/.](?:0[1-9]|[12][0-9]|3[01]|d{2})\b')
        return pattern.findall(txt)


class Task11Regex(Training):
    """Zad. 11
        Sprawdź, czy podany string jest zapisem koloru w systemie szesnastkowym (HEX).
        -	string musi się zaczynać znakiem #
        -	następnie musi zawierać 3 lub 6 (ale nie 4 lub 5)
            znaki kodu szesnastkowego pisane małą lub wielką literą;

        Przykłady:
        #ab4
        #AB4B72

        Błędne przykłady:
        #ab43
        #aaaaaaaaa
        #ahl
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def solution(self):
        colors = ["#ab4", "#AB4B72", "#ab43", "#aaaaaaaaa", "#ahl"]
        for color in colors:
            print(f"{color}: {self.check_hex(color)}")

    @staticmethod
    def check_hex(color):
        pattern = re.compile(r'^#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})$')
        return bool(pattern.match(color))
