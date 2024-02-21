import tkinter
from pprint import pprint

from ciphering_rot47_rot13.functionality.file_handler import FileHandler
from ciphering_rot47_rot13.functionality.rot13_chiper import Rot13Cipher
from ciphering_rot47_rot13.functionality.rot47_cipher import Rot47Cipher


class MenuApp:
    memory: list = []

    def __init__(self, root):
        self.root = root
        self.root.title = "Ciphering App"
        self.menu_button()
        self.encrypt_button = None
        self.save_button = None
        self.exit_button = None
        self.print_button = None
        self.decrypt_button = None
        self.encrypted_text = None
        # TODO
        # instancje class w init

    def menu_button(self) -> None:
        """Metoda tworząca gui menu"""
        #TODO
        # metody znikają buttony wywołują metody z manager
        self.encrypt_button = tkinter.Button(
            self.root,
            text="Encrypt plain text (ROT47)",
            command=self.encrypt_text_rot47,
        )
        self.encrypt_button.pack(pady=10)

        self.encrypt_button = tkinter.Button(
            self.root,
            text="Encrypt plain text (ROT13)",
            command=self.encrypt_text_rot13,
        )
        self.encrypt_button.pack(pady=10)

        self.save_button = tkinter.Button(
            self.root, text="Save encrypted texts to file", command=self.save_to_file)
        self.save_button.pack(pady=10)

        self.decrypt_button = tkinter.Button(
            self.root,
            text="Decrypt encrypted text from file (ROT47)",
            command=self.decrypt_from_file_rot47,
        )
        self.decrypt_button.pack(pady=10)

        self.decrypt_button = tkinter.Button(
            self.root,
            text="Decrypt encrypted text from file (ROT13)",
            command=self.decrypt_from_file_rot13,
        )
        self.decrypt_button.pack(pady=10)

        self.print_button = tkinter.Button(
            self.root,
            text="Print encrypted words stored in memory",
            command=self.print_encrypted_words,
        )
        self.print_button.pack(pady=10)

        self.exit_button = tkinter.Button(
            self.root, text="Exit", command=self.root.quit
        )
        self.exit_button.pack(pady=10)

    def encrypt_text_rot47(self) -> None:
        """Metoda uruchamiająca szyfrowanie rot 47"""
        text = "ROT47 is the easiest and yet powerful cipher!"
        # text = input("Podaj tekst do zaszyfrowania")
        rot47_cipher = Rot47Cipher()
        self.encrypted_text = rot47_cipher.encrypt(text)
        print(self.encrypted_text)
        self.memory.append(
            [{"encryption rot47 text": text}, {"encrypted": self.encrypted_text}]
        )

    def encrypt_text_rot13(self) -> None:
        """Metoda uruchamiająca szyfrowanie rot 13"""
        text = "rot13 is the easiest and yet powerful cipher!"
        # text = input("Podaj tekst do zaszyfrowania")
        rot13_cipher = Rot13Cipher()
        self.encrypted_text = rot13_cipher.encrypt(text)
        print(self.encrypted_text)
        self.memory.append(
            [{"encryption rot13 text": text}, {"encrypted": self.encrypted_text}]
        )

    def save_to_file(self) -> None:
        """Metoda uruchamiająca zapis do pliku"""
        if self.encrypted_text is None:
            print("Brak zaszyfrowanego tekst do zapsiu")
        else:
            file_handler = FileHandler("test_file.txt")
            file_handler.save_to_file(self.encrypted_text, append=False)
        self.memory.append("saved to file")

    def decrypt_from_file_rot47(self) -> None:
        """Metoda uruchamiająca deszyfrowanie rot47"""
        # text = "#~%cf :D E96 62D:6DE 2?5 J6E A@H6C7F= 4:A96CP"
        filename = "test_file.txt"
        file_handler = FileHandler(filename)
        text = file_handler.read_from_file()
        rot47_cipher = Rot47Cipher()
        decrypted_text = rot47_cipher.decrypt(text)
        print(decrypted_text)
        self.memory.append(
            [{"decryption rot47 text": text}, {"decrypted": decrypted_text}]
        )

    def decrypt_from_file_rot13(self) -> None:
        """Metoda uruchamiająca deszyfrowanie rot13"""
        # text = "ebg13 vf gur rnfvrfg naq lrg cbjreshy pvcure!"
        filename = "test_file.txt"
        file_handler = FileHandler(filename)
        text = file_handler.read_from_file()
        rot13_cipher = Rot13Cipher()
        decrypted_text = rot13_cipher.decrypt(text)
        print(decrypted_text)
        self.memory.append(
            [{"decryption rot13 text": text}, {"decrypted": decrypted_text}]
        )

    def print_encrypted_words(self) -> None:
        """Metoda wyświetlająca dziennik operacji"""
        pprint(self.memory)


if __name__ == "__main__":
    tkinter_root = tkinter.Tk()
    app = MenuApp(tkinter_root)
    app.root.mainloop()
