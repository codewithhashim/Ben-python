number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter the symbol for the operation: ")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0 or b == 0:
        return "You canoottttt use 0"
    return a / b

if( operator == "+"):
    print(add(number1, number2))
elif ( operator == "-"):
    print(sub(number1, number2))
elif ( operator == "*"):
    print(mul(number1, number2))
elif ( operator == "/"):
    print(div(number1, number2))
else:
    print("The operator is invalid is invalid")