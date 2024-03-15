import pytest

from python_zaawansowany.zadania.testy_jednostkowe.Zad4.functionality.src import (
    add_todo,
    check_pos,
    edit_todo,
    remove_all,
    remove_todo,
    todos,
)


class TestSrc:
    """Zad. 4
    Poniższy kod realizuje funkcjonalność prostego notatnika
    Możemy do niego dodawać dowolne notatki, usuwać niektóre oraz czyścić całą listę.
    Umieść go w pliku src.py i otestuj każdą z funkcji. Zapewnij sprawdzenie przypadków,
    w których zostanie rzucony wyjątek.

    """

    @pytest.fixture
    def set_check_pos_mock(self, mocker):
        mocker.patch(
            "python_zaawansowany.zadania.testy_jednostkowe.Zad4.functionality.src.check_pos",
            side_effect=Exception("No such item number!"),
        )

    @pytest.mark.parametrize("pos", [5, -1])
    def test_check_pos_raises_exception_for(self, pos, set_check_pos_mock):
        with pytest.raises(Exception, match="No such item number!"):
            check_pos(pos)

    def test_add_todo(self):
        note = "New note"
        add_todo(note)
        assert len(todos) == 5
        assert todos[-1] == note

    def test_remove_todo(self):
        with pytest.raises(Exception, match="No such item number!"):
            remove_todo(10)
        expect = todos[1]
        remove_todo(0)
        assert len(todos) == 4
        assert todos[0] == expect

    def test_edit_todo(self):
        content = "Edited note"
        with pytest.raises(Exception, match="No such item number!"):
            edit_todo(10, content)
        edit_todo(1, content)
        assert todos[1] == content

    def test_remove_all(self):
        remove_all()
        assert len(todos) == 0
