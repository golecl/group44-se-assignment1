from Calculator import testFunction

def test_subtraction():
    assert calculate("23-23") == 0
    assert calculate("23-23-1") == -1
    assert calculate("-23-3") == -26
    assert calculate("23-23*2") == -23
    assert calculate("23+2-5") == 20
