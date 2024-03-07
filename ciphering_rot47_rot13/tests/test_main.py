import tkinter

import pytest
from pytest_mock import MockerFixture

from ciphering_rot47_rot13.functionality.main import MenuApp


class TestMenuApp:
    # TODO
    # nie działa test_button mimo ustawienia
    # fixture button ma dalej wartość none

    @pytest.fixture
    def set_app_mock(self, mocker: MockerFixture):
        tkinter_root = tkinter.Tk()
        main_app = MenuApp(tkinter_root)
        return main_app

    def test_title(self, set_app_mock):
        """Test sprawdzający poprawnośc tytułu"""
        expect: str = "Ciphering App"
        assert set_app_mock.root.title == expect

    def test_buttons_existence(self, set_app_mock):
        """Test sprawdzający utworzenie przycisków"""
        assert set_app_mock.encrypt_button is not None
