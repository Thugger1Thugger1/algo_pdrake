from src.factorial import getFactorial, getAdd


def test_5():
    assert getFactorial (5) == 120

def test_getAdd():
    assert getAdd(5) == 15