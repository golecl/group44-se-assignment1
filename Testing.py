from Calculator import testFunction

def test_Calculator():
    assert Calculator("abcd") == "Sorry, this input is invalid"
    assert Calculator("9+10") == "The answer is 19"
    assert Calculator("10-9+2*23") == "The answer is 47"
    assert Calculator("10/2") == "Sorry, this input is invalid"
    assert Calculator("") == "Sorry, this input is invalid"
