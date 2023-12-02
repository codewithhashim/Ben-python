print(10 * 10 ** 2 / 10)  # (PEMDAS)
# 10 power 2 = 100
# 10 * 100 = 1000
# 1000 /10 = 100

my_rent = 0
is_cloudy = False

my_asset = 1
is_hot_temp = True

# because 23 is not greater than 45 this will return False
# comparison operator
print(23 > 45)

# Boolean Expression: Expressions that evaluate to either true or false.
print(1 > 4)

# Logical Operators: used to perform logical operations between boolean values.

# Assignment operator: (=)
my_age = 67  # assigning a value of 67 to the variable my_age

# equality operator: (==): checks whether the two values on left and right are equal or not
# True because 2 is equal to 2
print(2 == 2)
#  False
print(1 == 3)
# True
print(10 * 3 == 15 * 2)

# Not equal
# because 1 is not equal to 3 this will return True
print(1 != 3)

# is operator compares the memory location and not the value to see if that is equal
a = [1, 3, 4]  # list
b = a  # set the variable b equal to a
print(a is b)


# is not operator compares the memory location and not the value to see if that is not equal
a = [1, 3, 4]
b = 45
print(a is not b)


# and operator will check two different equations and it will return true if both of those equations / expressions are true.
# checks the first comparison and then second and if both of them returns true only then the and operator will return True.
print(10 > 3 and 30 > 4)
