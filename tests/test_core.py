from calculator import core


def test_add():
    assert core.add(2, 3) == 5
    assert core.add(-1, 1) == 0
    assert core.add(0, 0) == 0


def test_subtract():
    assert core.subtract(5, 3) == 2
    assert core.subtract(0, 5) == -5


def test_multiply():
    assert core.multiply(3, 4) == 12
    assert core.multiply(-2, 5) == -10


def test_divide():
    assert core.divide(10, 4) == 2.5
    assert core.divide(9, 3) == 3.0


def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        core.divide(10, 0)
