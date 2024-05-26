# Project 1-5 -> functions based

# def add():
#     pass

# project 6-7 -> OOP based

# example project 

# calculator based on OOP approach

class Calculator:
    
    # no constructor here
    def add(self, a, b):
        # a = input("Enter the first number")
        # b = input("Enter the second number")
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        # if b == 0 or a==0:
        if b == 0:
            return "Cannot divide by zero "
        elif a == 0:
            return "Zero cannot be divided, well kinda!"
        return a / b
    
# no constructor, so there are no parameters
calc = Calculator()

print("The sum is: ", calc.add(5, 3))

print("The answer is: ", calc.subtract(5, 3))


print("The answer is: ", calc.multiply(5, 3))

print("Division: ", calc.divide(0, 5))



# Not operator
# ! you are the best