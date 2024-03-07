from pytest_bdd import given, then, when

from python_zaawansowany.zadania.testy_jednostkowe.Zad2.functionality.fizz_buzz import (
    fizz_buzz,
)


@given("a number is divisible by 3")
def number_divisible_by_3():
    return 3


@given("a number is divisible by 5")
def number_divisible_by_5():
    return 5


@given("a number is divisible by both 3 and 5")
def number_divisible_by_both_3_and_5():
    return 15


@when("the number is checked with FizzBuzz game")
def check_number_with_fizzbuzz(number):
    return fizz_buzz(number)


@then("it should return <expected_output>")
def check_expected_output(expected_output, check_number_with_fizzbuzz):
    assert check_number_with_fizzbuzz == expected_output
