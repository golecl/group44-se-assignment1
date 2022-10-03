
from Calculator import testFunction

def test_calculate():
    assert calculate("2+2") == 4
    assert calculate("4-2") == 2
    assert calculate("2*3") == 6
    assert calculate("2+3-4") == 1
    assert calculate("2+2-3*3") == -5
    assert calculate("15-12*2") == 6
    assert calculate("23*3-5") == 64
    assert calculate("200-100*0") == 200
