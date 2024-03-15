import random

import pytest


@pytest.fixture
def get_list_of_random_nums():
    return [random.randint(1, 100) for i in range(10)]


def test_check_if_size_equals_to_10(get_list_of_random_nums):
    assert len(get_list_of_random_nums) == 10


def test_check_if_numbers_are_in_range_from_1_to_100(get_list_of_random_nums):
    is_valid = True
    for elem in get_list_of_random_nums:
        if elem > 100 or elem < 1:
            is_valid = False

    assert is_valid
