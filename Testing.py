from Calculator import testFunction

def test_multiplication():
    assert caclulate("234*2") == 468
    assert caclulate("2*34*2") == 136
    assert caclulate("2+234*2") == 470
    assert caclulate("2-234*2") == -466
    assert caclulate("20*0") == 0
