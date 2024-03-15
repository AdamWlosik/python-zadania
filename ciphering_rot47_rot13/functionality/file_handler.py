class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def save_to_file(self, text: str, append: bool = False) -> None:
        """Metoda zapusjąca tesks do pliku istniejącego lub tworząxa nowy"""
        mode = "a" if append else "w"
        with open(self.filename, mode) as file:
            file.write(text + "\n")

    def read_from_file(self) -> str:
        """Metoda odczytująca z pliku"""
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Plik {self.filename} nie istnieje")
