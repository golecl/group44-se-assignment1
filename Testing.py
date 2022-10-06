from Calculator import *

def test_multiplication():
    assert calculate("234*2") == 468
    assert calculate("2*34*2") == 136
    assert calculate("2+234*2") == 470
    assert calculate("2-234*2") == -466
    assert calculate("20*0") == 0
