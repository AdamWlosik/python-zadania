from datetime import timezone, datetime

import pytest

from python_zaawansowany.zadania.testy_jednostkowe.Zad5.functionality.calc_diff import *


class TestCalcDiff:

    def test_calc_diff_with_end_time(self):
        start_time = datetime(2021, 11, 3, 9, 22, 28, tzinfo=timezone.utc)
        end_time = datetime(2022, 2, 17, 12, 0, 0, tzinfo=timezone.utc)
        case = {'start_time': start_time.isoformat(), 'end_time': end_time.isoformat()}
        expect = (end_time - start_time).total_seconds()

        assert calc_diff(case) == expect

    @pytest.fixture
    def current_time(self):
        # Ustawiamy czas teraźniejszy na określoną wartość
        return datetime(2022, 2, 17, 12, 0, 0, tzinfo=timezone.utc)

    def test_calc_diff_with_end_time_none(self, current_time, mocker):
        # Ustawiamy przypadkową datę startową
        start_time = datetime(2021, 11, 3, 9, 22, 28, tzinfo=timezone.utc)
        case = {'start_time': start_time.isoformat(), 'end_time': None}

        # Mockujemy datetime.now(), aby zwrócić określony czas
        mocker.patch('python_zaawansowany.zadania.testy_jednostkowe.Zad5.functionality.calc_diff.calc_diff.datetime')
        datetime.now.return_value = current_time

        # Wywołujemy funkcję calc_diff
        result = calc_diff(case)

        # Sprawdzamy poprawność obliczenia różnicy czasowej
        assert result == (current_time - start_time).total_seconds()