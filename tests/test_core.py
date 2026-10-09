from calculator import core


def test_tambah():
    assert core.tambah(2, 3) == 5
    assert core.tambah(-1, 1) == 0
    assert core.tambah(0, 0) == 0


def test_kurang():
    assert core.kurang(5, 3) == 2
    assert core.kurang(0, 5) == -5


def test_kali():
    assert core.kali(3, 4) == 12
    assert core.kali(-2, 5) == -10


def test_bagi():
    assert core.bagi(10, 4) == 2.5
    assert core.bagi(9, 3) == 3.0


def test_bagi_oleh_nol():
    import pytest
    with pytest.raises(ValueError):
        core.bagi(10, 0)
