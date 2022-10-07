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

def test_subtraction():
    assert calculate("23-23") == 0
    assert calculate("23-23-1") == -1
    assert calculate("-23-3") == -26
    assert calculate("23-23*2") == -23
    assert calculate("23+2-5") == 20

def test_multiplication():
    assert calculate("234*2") == 468
    assert calculate("2*34*2") == 136
    assert calculate("2+234*2") == 470
    assert calculate("2-234*2") == -466
    assert calculate("20*0") == 0

def test_calculate():
    assert calculate("2+2") == 4
    assert calculate("4-2") == 2
    assert calculate("2*3") == 6
    assert calculate("2+3-4") == 1
    assert calculate("2+2-3*3") == -5
    assert calculate("15-12*2") == -9
    assert calculate("23*3-5") == 64
    assert calculate("200-100*0") == 200

def test_Calculator():
    assert Calculator("abcd") == "Sorry, this input is invalid"
    assert Calculator("9+10") == "The answer is 19"
    assert Calculator("10-9+2*23") == "The answer is 47"
    assert Calculator("10/2") == "Sorry, this input is invalid"
    assert Calculator("") == "Sorry, this input is invalid"