from ciphering_rot47_rot13.functionality.rot13_chiper import Rot13Cipher


class TestRot13Ciper:

    def test_encrypt(self):
        """Test metody szyfrującej rot47"""
        expect: str = "ebg13 vf gur rnfvrfg naq lrg cbjreshy pvcure!"
        text: str = "rot13 is the easiest and yet powerful cipher!"
        rot13_cipher = Rot13Cipher()
        assert rot13_cipher.encrypt(text) == expect

    def test_decrypt(self):
        """Test metody deszyfrującej rot47"""
        text: str = "ebg13 vf gur rnfvrfg naq lrg cbjreshy pvcure!"
        expect: str = "rot13 is the easiest and yet powerful cipher!"
        rot13_cipher = Rot13Cipher()
        assert rot13_cipher.encrypt(text) == expect
