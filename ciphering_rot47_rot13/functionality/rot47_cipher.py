from ciphering_rot47_rot13.functionality.rot_chiper import Rot


class Rot47Cipher(Rot):
    SHIFT: int = 47

    def shift(self, char: str, shift_value: int) -> str:
        ascii_val = ord(char)
        if 33 <= ascii_val <= 126:
            return chr((ascii_val - 33 + shift_value) % 94 + 33)
        return char

    def encrypt(self, text: str) -> str:
        """Metoda szyfrująca text rot47"""
        return "".join(self.shift(char, self.SHIFT) for char in text)

    def decrypt(self, text: str) -> str:
        """Metoda deszyfrująca text rot47"""
        return self.encrypt(text)
