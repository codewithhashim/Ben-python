
def call_code():
    print("Call that code")
    # rest of the code

# call_code()

def add():
    print(2+3)

# add()

def multiply():
    print(2*3)

# multiply()
# multiply()
# multiply()
# multiply()
# multiply()

def names():
    # ben
    return "Ben & Abby"
    # Any code that you write after the return statment, it wont run. So that is why the line of code below is faded. It only applies to the code that is inside the block of that specific function.
    print("Cooool after return")

print(names())
# print("ahdkfhaldsjflak")

# globally defined variable so that is why we say that this variable has a global scope.
global_car_color = "White"

def scopy():
    # print(global_car_color)
    # local scope -> this variable is defined inside a function so it is not accessable outside of this function.
    my_car_color = "beige"
    # print(my_car_color)

scopy()
# this is error, because we are printing a local scope variable.
# print(my_car_color)

# print(global_car_color)

# parameters (a,b)
#default parameter (c, because it has been initialzed in the function definition and there is no need of an argument for c.)
def division(a,b, c=100):
    print(a/b * c)

# arguments
division(130,5)