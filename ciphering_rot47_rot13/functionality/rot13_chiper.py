import string

from ciphering_rot47_rot13.functionality.rot_chiper import Rot


class Rot13Cipher(Rot):
    # TODO klasa abstrakcyjna ROT(SHIFT: int=NONE), metody encrypt i decrypt, S
    # translator do inita
    # SHIFT: int = 13 stała na cała klase
    def __init__(self, SHIFT=13):
        super().__init__(SHIFT)
        lowercase: str = string.ascii_lowercase
        uppercase: str = string.ascii_uppercase
        # SHIFT: int = 13
        shift_lowercase: str = lowercase[SHIFT:] + lowercase[:SHIFT]
        shift_uppercase: str = uppercase[SHIFT:] + lowercase[:SHIFT]
        self.translator: dict = str.maketrans(
            lowercase + uppercase, shift_lowercase + shift_uppercase
        )

    def encrypt(self, text: str) -> str:
        """Metoda szyfrująca text rot13"""
        table: dict = self.translator
        return text.translate(table)

    def decrypt(self, text: str) -> str:
        """Metoda deszyfrująca text rot 13"""
        table: dict = self.translator
        return text.translate(table)
