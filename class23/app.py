# lambda function is a continuation of the functions that we have covered previously.

# lambda function is a small anonymous function.

# syntax of lambda function:
# name_of_function = lambda arguments: expression 
fun = lambda x, y: x+y
print(fun(2, 3))

funTwo = lambda x: x**2

funThree = lambda g,h,k: g+h+k


# regular function
# def add(a,b):
#     return a+b
# print(add(2, 3))

# lambda with normal funciton
def normal():
    return lambda x: x**2
print(normal()(4))


# lambda with normal funciton second example
def normalTwo():
    return lambda x, y: x+y

a_var = normalTwo()
print(a_var(5, 5))
