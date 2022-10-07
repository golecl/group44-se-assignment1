from Calculator import *

def test_validity():
    assert checkIfValid("345+23-123*63463-23123") == True
    assert checkIfValid("-123-1") == True
    assert checkIfValid("973498-234+234*234") == True
    assert checkIfValid("9738-234") == True
    assert checkIfValid("324+234") == True
    assert checkIfValid("2344*3432") == True
    assert checkIfValid("-1231+3423") == True
    assert checkIfValid("-1231*3423") == True

    assert checkIfValid("123-") == False
    assert checkIfValid("123/234") == False
    assert checkIfValid("*23") == False
    assert checkIfValid("-+234234") == False
    assert checkIfValid("abc-2343") == False
    assert checkIfValid("") == False
    assert checkIfValid("2334**234") == False
    assert checkIfValid("/4523") == False
    assert checkIfValid("2334**234") == False
    assert checkIfValid("+--34") == False
    assert checkIfValid("+") == False
    assert checkIfValid("abc") == False
    assert checkIfValid("234.222+2342") == False
    assert checkIfValid("238974_234+234)))234(2342)") == False
    assert checkIfValid("(342*35345)-34234") == False

def test_addition():
    assert calculate("2+2") == 4
    assert calculate("324234+234+123") == 324591
    assert calculate("23+12*2") == 47
    assert calculate("23-12+3") == 14
