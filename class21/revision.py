# we need an environment to start
# Python (Executable program) + code editor (VS Code)

# Computer language -> Python programming language


# variables -> named memory location is what we call variables.

# syntax -> rules of writing code in a programming language.

# asdkf asdfajk = adsfkjad f90909

# Syntax of variable
# temprature is the name of the variable
# = assignment operator
temprature = 45

# Keywords: Words that are reserved by the language and that have a predefined meaning.
# Identifiers: Names that we will define in our code.
# Content: Anything else that will help carry the logic of the code is content


fav_meal = input("What do you like? ")

print("you like ", fav_meal)

# error
# adsf adsf = 54

# error
# 232adf = 56
# sdfs56dfgdf =sdfsdf


# Data type
# Ben 13 5.8 True (Bool data type)

sky = "Sky is orange color"
sky_orange = True

# concatenation
print("Adsfad" + "adsfasdfa")

# TypeError
# print (7 + "seven")

# syntax error
# asdfa adf = 67

if 3 > 5:
    print("adfads")
elif 56 > 89:
    print()
else:
    print("Welll hello I gotta go! ")


count = 1
while (count < 10):
    print(count)
    if count == 5:
        break
    count = count + 1


for i in range(3):
    print(i)



# function
# a,b represents parameters
def addNumbers(a, b):
    # function body 
    # return statement
    return a + b

# function call
# 5, 6 represents arguments
print(addNumbers(5, 6))
