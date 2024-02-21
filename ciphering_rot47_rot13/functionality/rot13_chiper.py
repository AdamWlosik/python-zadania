import string


class Rot13Cipher:
    #TODO klasa abstrakcyjna ROT(SHIFT: int=NONE), metody encrypt i decrypt, S
    # translator do inita
    #SHIFT: int = 13 stała na cała klase

    @staticmethod
    def translator() -> dict:
        """Metoda przygotowująca szyfrator"""
        lowercase: str = string.ascii_lowercase
        uppercase: str = string.ascii_uppercase
        shift: int = 13
        shift_lowercase: str = lowercase[shift:] + lowercase[:shift]
        shift_uppercase: str = uppercase[shift:] + lowercase[:shift]
        translator: dict = str.maketrans(
            lowercase + uppercase, shift_lowercase + shift_uppercase
        )
        return translator

    def encrypt(self, text: str) -> str:
        """Metoda szyfrująca text rot13"""
        table: dict = self.translator()
        return text.translate(table)

    def decrypt(self, text: str) -> str:
        """Metoda deszyfrująca text rot 13"""
        table: dict = self.translator()
        return text.translate(table)
