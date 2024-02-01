import os.path


def print_doc(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        print(self.__class__.__doc__)
        nazwa_pliku = os.path.basename(self.__class__.__module__)
        nazwa_klasy = self.__class__.__name__
        print(f"Nazwa pliku: {nazwa_pliku}, Klasa: {nazwa_klasy}")
        print("\nRozwiązanie: \n")
        return function(*args, **kwargs)

    return wrapper
