from python_zaawansowany.math_operation.functionality.operations import *


def test_should_return_correct_value_for_positive_exp():
    base = 5
    exp = 3

    assert calc_power(base, exp) == 125


def test_should_return_correct_value_for_negative_exp():
    base = 5
    exp = -3

    assert calc_power(base, exp) == 0.008


def test_should_return_correct_value_for_negative_base():
    base = -5
    exp = 3

    assert calc_power(base, exp) == -125


def test_should_return_correct_value_for_negative_base_and_negative_exp():
    base = -5
    exp = -3

    assert calc_power(base, exp) == -0.008


def test_should_return_1_for_0_exp():
    base1 = 5
    base2 = 10
    exp = 0

    assert calc_power(base1, exp) == 1
    assert calc_power(base2, exp) == 1


def test_should_return_0_for_0_base():
    base = 0
    exp1 = 10
    exp2 = 2

    assert calc_power(base, exp1) == 0
    assert calc_power(base, exp2) == 0


def test_should_return_correct_float_for_fractional_exp():
    base = 100
    exp = 0.5

    assert calc_power(base, exp) == 10
