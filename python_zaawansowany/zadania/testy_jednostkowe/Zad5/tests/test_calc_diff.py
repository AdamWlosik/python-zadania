from datetime import datetime, timezone

from python_zaawansowany.zadania.testy_jednostkowe.Zad5.functionality.calc_diff import (
    calc_diff,
)


class TestCalcDiff:
    """Rozważ poniższy program:


    Odpowiedzialny jest on za wyliczanie różnicy czasowej (podanej w sekundach) między start_time oraz end_time.

    Napisz test, który będzie sprawdzał poprawne działanie funkcji calc_diff.

    Podpowiedź:
    Tylko tyle, albo aż tyle! Zauważ, że konieczne będzie zamockowanie datetime.now().
    Dlaczego? To już zostawiam Twoim dywagacjom.

    """

    def test_calc_diff_with_end_time(self):
        """Test metody calc_diff z podanym czasem zakończenia"""
        start_time = datetime(2021, 11, 3, 9, 22, 28, tzinfo=timezone.utc)
        end_time = datetime(2022, 2, 17, 12, 0, 0, tzinfo=timezone.utc)
        case = {"start_time": start_time.isoformat(), "end_time": end_time.isoformat()}
        expect = (end_time - start_time).total_seconds()

        assert calc_diff(case) == expect

    def test_calc_diff(self, mocker):
        """Test metody calc_diff z czasem zakończenia None"""
        case = {
            "start_time": "2021-11-03T09:22:28+00:00",
            "end_time": "2021-11-03T10:22:28+00:00",
        }

        mocker.patch(
            "python_zaawansowany.zadania.testy_jednostkowe.Zad5.functionality.calc_diff.datetime",
            return_value=datetime(2021, 11, 3, 10, 0, 0, tzinfo=timezone.utc),
        )
        mocker.patch(
            "python_zaawansowany.zadania.testy_jednostkowe.Zad5.functionality.calc_diff.datetime.fromisoformat",
            side_effect=lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z"),
        )
        assert calc_diff(case) == 3600
