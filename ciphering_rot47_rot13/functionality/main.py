import tkinter

from ciphering_rot47_rot13.functionality.rot13_chiper import Rot13Cipher
from ciphering_rot47_rot13.functionality.rot47_cipher import Rot47Cipher


class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title = "Ciphering App"
        self.menu_button()
        self.encrypt_button = None
        self.save_button = None
        self.exit_button = None
        self.print_button = None
        self.decrypt_button = None

    def menu_button(self):
        """Metoda tworząca gui menu"""
        self.encrypt_button = tkinter.Button(self.root, text="Encrypt plain text (ROT47)",
                                             command=self.encrypt_text_rot47)
        self.encrypt_button.pack(pady=10)

        self.encrypt_button = tkinter.Button(self.root, text="Encrypt plain text (ROT13)",
                                             command=self.encrypt_text_rot13)
        self.encrypt_button.pack(pady=10)

        self.save_button = tkinter.Button(self.root, text="Save encrypted texts to file",
                                          command=self.save_to_file)
        self.save_button.pack(pady=10)

        self.decrypt_button = tkinter.Button(self.root, text="Decrypt encrypted text from file (ROT47)",
                                             command=self.decrypt_from_file_rot47)
        self.decrypt_button.pack(pady=10)

        self.decrypt_button = tkinter.Button(self.root, text="Decrypt encrypted text from file (ROT13)",
                                             command=self.decrypt_from_file_rot13)
        self.decrypt_button.pack(pady=10)

        self.print_button = tkinter.Button(self.root, text="Print encrypted words stored in memory",
                                           command=self.print_encrypted_words)
        self.print_button.pack(pady=10)

        self.exit_button = tkinter.Button(self.root, text="Exit",
                                          command=self.root.quit)
        self.exit_button.pack(pady=10)

    @staticmethod
    def encrypt_text_rot47():
        """Metoda uruchamiająca szyfrowanie rot 47"""
        text = "ROT47 is the easiest and yet powerful cipher!"
        encrypt = Rot47Cipher()
        print(encrypt.encrypt(text))

    def encrypt_text_rot13(self):
        """Metoda uruchamiająca szyfrowanie rot 13"""
        text = "rot13 is the easiest and yet powerful cipher!"
        encrypt = Rot13Cipher()
        print(encrypt.encrypt(text))

    def save_to_file(self):
        """Metoda uruchamiająca zapis do pliku"""
        pass

    @staticmethod
    def decrypt_from_file_rot47():
        """Metoda uruchamiająca deszyfrowanie rot47"""
        text = "#~%cf :D E96 62D:6DE 2?5 J6E A@H6C7F= 4:A96CP"
        decrypt = Rot47Cipher()
        print(decrypt.decrypt(text))

    def decrypt_from_file_rot13(self):
        """Metoda uruchamiająca deszyfrowanie rot13"""
        text = "ebg13 vf gur rnfvrfg naq lrg cbjreshy pvcure!"
        decrypt = Rot13Cipher()
        print(decrypt.decrypt(text))

    def print_encrypted_words(self):
        """Metoda uruchamiająca wyświetlanie zaszyfrowanych słów"""
        pass


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MenuApp(root)
    root.mainloop()
