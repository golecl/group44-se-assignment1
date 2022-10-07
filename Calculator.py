import re

print("Welcome to the simple math expression calculator")
print("Type quit to exit\n")
s = list(range(0,10))
Integer = ' '.join(map(str, s))
length = len(Integer)

def checkIfValid(string):
    # checks if the string is not blank
    if len(string) < 1:
        return False
    # checks if beginning or end of string is an operator (except for a minus because negative integers are allowed)
    if (string[0] == '+') or (string[0] == '*') or (string[len(string)-1] == '+') or (string[len(string)-1] == '-') or (string[len(string)-1] == '-'):
        return False
    for index in range(len(string)):
        # checks if all characters are either digits or the accepted operators
        if (string[index] not in Integer) and (string[index] != '+') and (string[index] != '-') and (string[index] != '*'):
            return False
        # checks that there are no double operators
        elif ((string[index] == '+') or (string[index] == '-') or (string[index] == '*')) and ((string[index+1] == '+') or (string[index+1] == '-') or (string[index+1] == '*')):
            return False
    # if all of the above checks pass, it passes
    return True

def calculate(string):
    spacedString = re.sub(r'(\d+(\.\d+)?)', r' \1 ', string)
    spacedString = spacedString.strip()
    input = spacedString.split()
    while True:
        if "*" in input:
            operator = input.index("*")
            number = int(input[operator - 1]) * int(input[operator + 1])
            removeAt(input, operator, number)
        elif "-" in input:
            operator = input.index("-")
            if operator == 0:
                number = (int(input[operator + 1])*(-1))
                input[operator] = number
                del input[operator + 1]
            else:
                number = int(input[operator - 1]) - int(input[operator + 1])
                removeAt(input, operator, number)
        elif "+" in input:
            operator = input.index("+")
            number = int(input[operator - 1]) + int(input[operator + 1])
            removeAt(input, operator, number)
        else:
            break
    result = int(input[0])
    return result

def removeAt(input, operator, number):
    input[operator + 1] = str(number)
    del input[operator]
    del input[operator - 1]
    return

def Calculator(string):
    if checkIfValid(string):
        answer = calculate(string)
        print("The answer is {}".format(answer))
        # returns the message for test purposes
        return "The answer is {}".format(answer)
    else:
        print("Sorry, this input is invalid")
        # returns the message for test purposes
        return "Sorry, this input is invalid"

def main():
    while True:
        equ = input("Enter equation : ") 
        if equ == 'quit':
           print("GoodBye, Hope you enjoy the calculation.")
           break
        else:
            Calculator(equ)

if __name__ == "__main__":
    main()