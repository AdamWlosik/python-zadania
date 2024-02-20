from ciphering_rot47_rot13.functionality.rot47_cipher import Rot47Cipher


class TestRot47Ciper:

    def test_encrypt(self):
        """Test metody szyfrującej rot47"""
        expect = "#~%cf :D E96 62D:6DE 2?5 J6E A@H6C7F= 4:A96CP"
        text = "ROT47 is the easiest and yet powerful cipher!"
        encrypt = Rot47Cipher()
        assert encrypt.encrypt(text) == expect

    def test_decrypt(self):
        """Test metody deszyfrującej rot47"""
        text = "#~%cf :D E96 62D:6DE 2?5 J6E A@H6C7F= 4:A96CP"
        expect = "ROT47 is the easiest and yet powerful cipher!"
        encrypt = Rot47Cipher()
        assert encrypt.encrypt(text) == expect
