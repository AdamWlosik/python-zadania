import pytest

from python_zaawansowany.zadania.testy_jednostkowe.Zad2.functionality.fizz_buzz import (
    fizz_buzz,
)


class TestFizzBuzz:
    """Zad. 2
    Napisz funkcję, która zwracać będzie “Fizz”,
    gdy prześlesz do niej wartość podzielną przez 3, “Buzz”,
    gdy podzielną przez 5, a “FizzBuzz”, gdy liczba będzie podzielna przez obie te wartości.
    Napisz do niej testy jednostkowe.
    """

    @pytest.mark.parametrize(
        "number, expect",
        [
            (3, "Fizz"),
            (5, "Buzz"),
            (15, "FizzBuzz"),
            (1, None),
        ],
    )
    def test_when_number_is(self, number, expect):
        assert fizz_buzz(number) == expect

    """  def test_when_number_is_5(self):
          number = 5
          assert fizz_buzz(number) == "Buzz"

      def test_when_number_is_15(self):
          number = 15
          assert fizz_buzz(number) == "FizzBuzz"

      def test_when_number_is_1(self):
          number = 1
          assert fizz_buzz(number) is None
  """

    def test_when_number_is_float(self):
        number = 0.5
        assert fizz_buzz(number) is None

    def test_when_number_is_str_should_raise_exception(self):
        number = "a"
        with pytest.raises(TypeError):
            fizz_buzz(number)
