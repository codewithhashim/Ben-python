# error: flaw or mistake in a code that prevents the program to run /work properly.
# syntax errors (Issues that violates the rules of a programming language syntax)
# symantic errors: mistake or error that is related to logical structure or design.

# I am eating an apple. - Correct grammar (correct syntax) and it make sense.
# An apple is eating me. - Incorrect logic but correct grammar (syntax)

# What is a tuple in Python?
# "hello" is a string data type.
my_tuple = (4, 6, "hello", 56, 56.3, True)

# tuple is ordered.
# tuple is an immutable data type.
# you cannot change the elements of a tuple after it is created.

# method: a buil-in function that does something.
# built-in: refers to features or functionalities that are inherently  included as a part of a programming language.

numbers = (4, 7, 8, 4, 1, 2, 4, 3, 2, 4, 4)
print(numbers)

# count() method - counts the number of times an element has been used in a tuple or a list.
print(numbers.count(4))

# index -index of the element that is passed.
print(numbers.index(7))

# len()
# it will generate an AttributeError:
# print(number.len())
print(len(numbers))

# sorted method: A method that returns the sorted list from the elements of the tuple.
my_sorted_tuple = sorted(numbers)
print(my_sorted_tuple)

# min and max:
print(min(numbers)) # output -> 1
print(max(numbers)) # output -> 8
