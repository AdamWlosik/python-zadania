import re

from Szkolenie import Szkolenie
from helpers import print_doc


class Task1Regex(Szkolenie):
    """Zad. 1
        Napisz program, który sprawdzi, czy string zawiera tylko
        i wyłącznie zbiór następujących znaków: (a-z, A-Z i 0-9).
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def rozwiazanie(self):
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


class Task2Regex(Szkolenie):
    """Zad. 2
        Sprawdź, czy string rozpoczyna się pojedynczą cyfrą: 0 lub literą ‘b’.
        """

    def __init__(self, szkolenie, zadanie):
        super().__init__(szkolenie, zadanie)

    @print_doc
    def rozwiazanie(self):
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


class Task3Regex(Szkolenie):
    """Zad. 3
        Sprawdzaj, czy podany string zawiera ciąg dowolnych małych liter rozdzielonych znakiem _, np. aab_cbbbc
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def rozwiazanie(self):
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


class Task4Regex(Szkolenie):
    """Zad. 4
        Znajdź słowa, które kończą się co najmniej dwiema literami ‘s’, np.
        -	hiss
        -	hisssss
        -	His
        """

    def __init__(self, training, task):
        super().__init__(training, task)

    @print_doc
    def rozwiazanie(self):
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


class Task5Regex(Szkolenie):
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
    def rozwiazanie(self):
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
