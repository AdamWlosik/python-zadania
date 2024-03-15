from ciphering_rot47_rot13.functionality.rot47_cipher import Rot47Cipher


class TestRot47Ciper:

    def test_encrypt(self):
        """Test metody szyfrującej rot47"""
        expect: str = "#~%cf :D E96 62D:6DE 2?5 J6E A@H6C7F= 4:A96CP"
        text: str = "ROT47 is the easiest and yet powerful cipher!"
        rot47_cipher = Rot47Cipher()
        assert rot47_cipher.encrypt(text) == expect

    def test_decrypt(self):
        """Test metody deszyfrującej rot47"""
        text: str = "#~%cf :D E96 62D:6DE 2?5 J6E A@H6C7F= 4:A96CP"
        expect: str = "ROT47 is the easiest and yet powerful cipher!"
        rot47_cipher = Rot47Cipher()
        assert rot47_cipher.encrypt(text) == expect
