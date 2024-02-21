import pytest

from python_zaawansowany.zadania.testy_jednostkowe.Zad2.functionality.fizz_buzz import fizz_buzz


# Pytest-bdd marker to link steps to scenarios
@pytest.mark.parametrize("number, expected_output", [(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")])
def test_fizz_buzz(number, expected_output):
    assert fizz_buzz(number) == expected_output
