from ciphering_rot47_rot13.functionality.rot_chiper import Rot


class Rot47Cipher(Rot):

    @staticmethod
    def encrypt(text: str) -> str:
        """Metoda szyfrująca text rot47"""
        encrypted_text = []
        for char in range(len(text)):
            j = ord(text[char])
            if 33 <= j <= 126:
                encrypted_text.append(chr(33 + ((j + 14) % 94)))
            else:
                encrypted_text.append(text[char])
        return "".join(encrypted_text)

    def decrypt(self, text: str) -> str:
        """Metoda deszyfrująca text rot47"""
        return self.encrypt(text)
