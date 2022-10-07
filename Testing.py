from Calculator import *

def test_addition():
    assert calculate("2+2") == 4
    assert calculate("324234+234+123") == 324591
    assert calculate("23+12*2") == 47
    assert calculate("23-12+3") == 14
