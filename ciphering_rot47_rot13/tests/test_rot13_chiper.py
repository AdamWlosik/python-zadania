from ciphering_rot47_rot13.functionality.rot13_chiper import Rot13Cipher


class TestRot13Ciper:

    def test_encrypt(self):
        """Test metody szyfrującej rot47"""
        expect = "ebg13 vf gur rnfvrfg naq lrg cbjreshy pvcure!"
        text = "rot13 is the easiest and yet powerful cipher!"
        encrypt = Rot13Cipher()
        assert encrypt.encrypt(text) == expect

    def test_decrypt(self):
        """Test metody deszyfrującej rot47"""
        text = "ebg13 vf gur rnfvrfg naq lrg cbjreshy pvcure!"
        expect = "rot13 is the easiest and yet powerful cipher!"
        encrypt = Rot13Cipher()
        assert encrypt.encrypt(text) == expect
