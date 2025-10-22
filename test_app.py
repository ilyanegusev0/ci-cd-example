import app


def test_is_positive():
    assert app.is_positive(1) is True
    assert app.is_positive(-1) is False
    assert app.is_positive(0) is False


def test_is_negative():
    assert app.is_negative(-2) is True
    assert app.is_negative(2) is False
    assert app.is_negative(0) is False
