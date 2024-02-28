import tkinter
from pprint import pprint

from ciphering_rot47_rot13.functionality.file_handler import FileHandler
from ciphering_rot47_rot13.functionality.manager import Manager
from ciphering_rot47_rot13.functionality.rot13_chiper import Rot13Cipher
from ciphering_rot47_rot13.functionality.rot47_cipher import Rot47Cipher


class MenuApp:

    def __init__(self, root):
        self.manager = Manager()
        self.root = root
        self.root.title = "Ciphering App"
        self.menu_button()
        self.encrypt_button = None
        self.save_button = None
        self.exit_button = None
        self.print_button = None
        self.decrypt_button = None

    def menu_button(self) -> None:
        """Metoda tworząca gui menu"""
        self.encrypt_button = tkinter.Button(
            self.root,
            text="Encrypt plain text (ROT47)",
            command=self.manager.encrypt_text_rot47,
        )
        self.encrypt_button.pack(pady=10)

        self.encrypt_button = tkinter.Button(
            self.root,
            text="Encrypt plain text (ROT13)",
            command=self.manager.encrypt_text_rot13,
        )
        self.encrypt_button.pack(pady=10)

        self.save_button = tkinter.Button(
            self.root, text="Save encrypted texts to file", command=self.manager.save_to_file)
        self.save_button.pack(pady=10)

        self.decrypt_button = tkinter.Button(
            self.root,
            text="Decrypt encrypted text from file (ROT47)",
            command=self.manager.decrypt_from_file_rot47,
        )
        self.decrypt_button.pack(pady=10)

        self.decrypt_button = tkinter.Button(
            self.root,
            text="Decrypt encrypted text from file (ROT13)",
            command=self.manager.decrypt_from_file_rot13,
        )
        self.decrypt_button.pack(pady=10)

        self.print_button = tkinter.Button(
            self.root,
            text="Print encrypted words stored in memory",
            command=self.manager.print_encrypted_words,
        )
        self.print_button.pack(pady=10)

        self.exit_button = tkinter.Button(
            self.root, text="Exit", command=self.root.quit
        )
        self.exit_button.pack(pady=10)


if __name__ == "__main__":
    tkinter_root = tkinter.Tk()
    app = MenuApp(tkinter_root)
    app.root.mainloop()
