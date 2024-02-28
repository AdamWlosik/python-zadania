import pytest


@pytest.makr.odd_nums
@pytest.mark.parametrize("input_list_1, input_list_2, input_list_3", [([1, 3, 5, 9], [1, 1, 1], [11]), ([], [], [])])
def test_check_if_contains_only_odd_nums_for_list(input_list_1, input_list_2, input_list_3):
    is_valid = True
    for elem in input_list_1, input_list_2, input_list_3:
        if not elem or not elem % 2:
            is_valid = False

    assert is_valid
