import io
import pytest

from python_zaawansowany.zadania.testy_jednostkowe.Zad8.functionality.show_message import show_message


def test_show_message(mocker):
    message = "fake_msg"
    fake_stdout = io.StringIO()
    mocker.patch("sys.stdout", new=fake_stdout)
    show_message(message)
    assert fake_stdout.getvalue().strip() == f"Your message: {message}"
