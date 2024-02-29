from python_zaawansowany.training import Training


class FileHandlerEX(Training):
    """Zad. 1
        Przygotuj klasę FileHandler, która symulować będzie funkcjonalność obsługiwania plików w Javie.
        Ma ona przechowywać pola takie jak: file_path, no_connectors, max_file_size.
        Będa one ustawiane z poziomu odpowiednich setterów jak i konstruktora.
        Klasa ta ma dodatkowo przechowywać takie metody jak read_content, save_to_file,
        w których umieścisz, tzw. dummy printy (będziesz drukował dowolny tekst).

        Celem tego zadania nie jest stworzenie odpowiedniej logiki biznesowej dla klasy,
        tylko zaprojektowanie klasy, która będzie zwracała odpowiedni user-defined wyjątek
        w zależności od przekazania do obiektu klasy niewłaściwej danej, np. pustego stringa,
        który będzie miał być umieszczony pod polem file_path.

        Dodatkowe warunki:
        Wartość noConnector nie może przekroczyć wartości 10
        maxFileSize musi być zawsze liczbą czterocyfrową
        """

    def __init__(self, training: int, task: int, file_path, no_connectors, max_file_size):
        super().__init__(training, task)
        self.max_file_size = max_file_size
        self.no_connectors = no_connectors
        self.file_path = file_path
        # TODO
        # dopytać się o settery
        # https://codecouple.pl/2016/03/04/python-gettery-i-settery-property/

    def solution(self):
        pass

    @property
    def file_path(self):
        return self.__file_path

    @property
    def no_connectors(self):
        return self.__no_connectors

    @property
    def max_file_size(self):
        return self.__max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        if max_file_size < 1000:
            raise Exception("max_file_size nie jest liczbą czterocyfrową")
        self.__max_file_size = max_file_size

    @no_connectors.setter
    def no_connectors(self, no_connectors):
        if no_connectors > 10:
            raise Exception("no_connectors > 10")
        self.__no_connectors = no_connectors

    @file_path.setter
    def file_path(self, file_path):
        if not file_path:
            raise Exception("file_path jest pustym srt")
        else:
            self.__file_path = file_path

    def read_content(self):
        pass

    def save_to_file(self):
        pass
