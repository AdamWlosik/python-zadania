from ciphering_rot47_rot13.functionality.rot_chiper import Rot


class Rot13Cipher(Rot):
    SHIFT: int = 13

    def shift(self, char: str, shift_value: int) -> str:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            return chr((ord(char) - ascii_offset + shift_value) % 26 + ascii_offset)
        return char

    def encrypt(self, text: str) -> str:
        """Metoda szyfrująca text rot13"""
        return "".join(self.shift(char, self.SHIFT) for char in text)

    def decrypt(self, text: str) -> str:
        """Metoda deszyfrująca text rot 13"""
        return "".join(self.shift(char, 26 - self.SHIFT) for char in text)
