from ciphering_rot47_rot13.functionality.main import MenuApp


class TestMenuApp:
    menu_app = MenuApp

    # TODO
    # sprawdzic testy

    def test_encrypt_text_rot47(self, mocker):
        expect = "encrypted txt"
        mocker.patch(
            "ciphering_rot47_rot13.functionality.main.MenuApp.encrypt_text_rot47",
            return_value=expect,
        )

        assert self.menu_app.encrypt_text_rot47() == expect

    def test_encrypt_text_rot13(self, mocker):
        expect = "encrypted txt"
        mocker.patch(
            "ciphering_rot47_rot13.functionality.main.MenuApp.encrypt_text_rot13",
            return_value=expect,
        )
        assert self.menu_app.encrypt_text_rot13() == expect

    def test_save_to_file(self):
        pass

    def test_decrypt_from_file_rot47(self, mocker):
        expect = "decrypted text"
        mocker.patch(
            "ciphering_rot47_rot13.functionality.file_handler.FileHandler.read_from_file",
            return_value="encrypted text",
        )
        mocker.patch(
            "ciphering_rot47_rot13.functionality.main.MenuApp.decrypt_from_file_rot47",
            return_value=expect,
        )

        assert self.menu_app.decrypt_from_file_rot47() == expect

    def test_decrypt_from_file_rot13(self, mocker):
        expect = "decrypted text"
        mocker.patch(
            "ciphering_rot47_rot13.functionality.file_handler.FileHandler.read_from_file",
            return_value="encrypted text",
        )
        mocker.patch(
            "ciphering_rot47_rot13.functionality.main.MenuApp.decrypt_from_file_rot13",
            return_value=expect,
        )

        assert self.menu_app.decrypt_from_file_rot13() == expect

    def test_print_encrypted_words(self, capsys):
        # TODO
        # nie działa
        self.menu_app.memory = [{"test": "test"}]
        self.menu_app.print_encrypted_words()
        captured = capsys.readouterr()
        assert captured.out.strip() == '[{"test": "test"}]'
