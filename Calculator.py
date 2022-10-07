import sys
import re

print("Welcome to the simple math expression calculator.")
print("Type quit to exit\n")
s = list(range(0,10))
Integer = ' '.join(map(str, s))

def errorCheck(string):
    index = 0
    if string[0] == ('+' and '-' and '*') or string[len(string)-1] == ('+' and '-' and '*'):
        return False
    if string[0] not in Integer or string[len(string)-1] not in Integer:
        return False
    for index in range(len(string)):
        if string[index] in Integer or string[index] == ('+' and '-' and '*'):
               return True
        elif string[index] == ('+' and '-' and '*') and string[index+1] == ('+' and '-' and '*'):
            return False
    return False

def calculate(string):
    input = string.split()
    for i in range(len(string)):
        try:
            if "*" in input:
                operator = input.index("*")
                number = int(input[operator - 1]) * int(input[operator + 1])
                removeAt(input, operator, number)
            elif "-" in input:
                operator = input.index("-")
                number = int(input[operator - 1]) - int(input[operator + 1])
                removeAt(input, operator, number)
            elif "+" in input:
                operator = input.index("+")
                number = int(input[operator - 1]) + int(input[operator + 1])
                removeAt(input, operator, number)
        except:
                print("Invalid Input. Wrong Expression!")
    result = int(input[0])
    return result

def removeAt(input, operator, number):
    input[operator + 1] = str(number)
    del input[operator]
    del input[operator - 1]
    return

def main():
    while True:
        equ = input("Enter equation : ") 
        res = re.sub('(\d+(\.\d+)?)', r' \1 ', equ)
        res = res.strip()
        check = errorCheck(res)
        if equ == 'quit':
           print("GoodBye, Hope you enjoy the calculation.")
           break
        elif check==True:
           answer = calculate(res)
           print(answer)
        else:
           print("Wrong Expression! Please enter the correct format.") 

if __name__ == "__main__":
    main()