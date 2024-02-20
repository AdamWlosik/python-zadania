import pytest

from python_zaawansowany.zadania.testy_jednostkowe.Zad6.functionality.db_handler import DbHandler

# TODO
# problme z from decouple import config w programie do przetestowania
@pytest.fixture
def mocked_config(mocker):
    """Fixture zwracająca zamockowaną klasę Config."""
    mocked_config = mocker.MagicMock()
    mocked_config.DB_URL = 'mocked_db_ulr'
    mocked_config.DB_USERNAME = 'mocked_db_username'
    mocked_config.DB_PASSWORD = 'mocked_db_password'
    mocked_config.OK_MSG = 'mocked_ok_msg'
    mocked_config.NOK_MSG = 'mocked_nok_msg'
    mocker.path("python_zaawansowany.zadania.testy_jednostkowe.Zad6.functionality.db_handler.Config", mocked_config)


def test_connect_to_database(mocked_config):
    """Test metody connect_to_database klasy DbHandler. Sprawdza, czy metoda zwraca oczekiwany napis."""
    db_handler = DbHandler()
    expect = "I am connecting to mocked_db_url as mocked_db_username with pass: mocked_db_password..."
    assert db_handler.connect_to_database() == expect
