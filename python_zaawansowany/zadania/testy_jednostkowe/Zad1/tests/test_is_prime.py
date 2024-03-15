import pytest

from python_zaawansowany.zadania.testy_jednostkowe.Zad1.functionality.is_prime import (
    is_prime,
)


class TestIsPrime:
    """Zad. 1
    Stwórz funkcję sprawdzającą, czy liczba jest pierwsza.
    Otestuj ją, pamiętając równocześnie o otestowaniu każdego edge-case’a
    (np. 1 nie jest liczbą pierwszą).
    Spróbuj stworzone testy umieścić w klasie.
    """

    @pytest.mark.parametrize(
        "number, expect",
        [
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
            (10, False),
            (-1, False),
            (0, False),
        ],
    )
    def test_number_negative_1_to_10(self, number, expect):
        assert is_prime(number) == expect

    """def test_negative_number(self):
        number = -1
        assert not is_prime(number)

    def test_0(self):
        number = 0
        assert not is_prime(number)
"""

    def test_float_number(self):
        number = 0.5
        assert not is_prime(number)
