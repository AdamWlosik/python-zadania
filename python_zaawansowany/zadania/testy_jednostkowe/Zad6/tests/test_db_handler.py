import pytest
from pytest_mock import MockerFixture



# TODO
# problme z from decouple import config w programie do przetestowania
# @pytest.fixture
# def mocked_config(mocker: MockerFixture):
#     """Fixture zwracająca zamockowaną klasę Config."""
#     mocked_config = mocker.MagicMock()
#     mocked_config.DB_URL = 'mocked_db_url'
#     mocked_config.DB_USERNAME = 'mocked_db_username'
#     mocked_config.DB_PASSWORD = 'mocked_db_password'
#     mocked_config.OK_MSG = 'mocked_ok_msg'
#     mocked_config.NOK_MSG = 'mocked_nok_msg'
#     mocker.patch("python_zaawansowany.zadania.testy_jednostkowe.Zad6.functionality.db_handler.Config", mocked_config)


def test_connect_to_database(mocker: MockerFixture):
    """Test metody connect_to_database klasy DbHandler. Sprawdza, czy metoda zwraca oczekiwany napis."""
    mocked_config = mocker.patch("decouple.config")
    mocked_config.return_value = "pytest1"
    from python_zaawansowany.zadania.testy_jednostkowe.Zad6.functionality.db_handler import DbHandler
    db_handler = DbHandler()
    expect = "I am connecting to pytest1 as pytest1 with pass: pytest1..."
    assert db_handler.connect_to_database() == expect
    assert db_handler.get_test() == "pytest1"
