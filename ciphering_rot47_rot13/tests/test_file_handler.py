from ciphering_rot47_rot13.functionality.file_handler import FileHandler


class TestFileHandler:

    def test_save_to_file_overwrite(self, mocker):
        """Test metody zapisującej do pliku w przypadku nadpisania"""
        # Zastępuje wbudowaną funkcję open mockowaną w module builtins
        # (czyli moduł zawierający podstawowe wbudowane funkcje Pythona
        mocked_open = mocker.patch("builtins.open", mocker.mock_open())
        text = "rot13 is the easiest and yet powerful cipher!"
        file_path = "test_file.txt"
        file_handler = FileHandler(file_path)

        file_handler.save_to_file(text, append=True)
        mocked_open.assert_called_once_with(file_path, "a")
        mocked_open.return_value.write.assert_called_once_with(text + "\n")
