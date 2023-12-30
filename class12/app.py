
str1 = "Hello"
# 0 1 2 3 4
# print(str1[4])

# in operator
# print ("hi" in "hi there")

# not in operator
# print ("hi" not in "hi there")

# List (non-tech simple definition): Collection of data that can be different combined together under one name.

# syntax
# name_of_list = [item1, 2, 3 .......]

# index in list (index starts at 0) (0, 1,2 3, 4....)
bunch_of_items = [55, "pillows", False, "evening"]
# number of elements (1, 2, 3, 4, 5.....)

#  A list is a data-type like we have string, number (int), booleans, floats

# List: a mutable data type which can store multiple data types under one identifier name.
# mutable means something that can be changed or altered.

# How do we access an item in a list?
# the list items can be called as elements but you can keep it simple to call as list items.
mylist = ["hi", "hello", 45, 88]
# print the entire list
# print(mylist)
# access element (individual)
# print(mylist[3])

# modifying an element
mylist[1] = "Hello there"
# print(mylist)

# error index out of range (this error will arise if there is nothing on that specific index number.)
# mylist[4] = "ptint this"
# print(mylist)


# list methods: (built-in function) for list

# adding element to an existing listing
mylist.append("appended element")
mylist.append(67)
# print(mylist)

# removing an element from a list using the remove method
mylist.remove(67)
print(mylist)

# counting the item in a list
print(len(mylist))

# pop() method remove the last item but if an index number has been provided it will remove that specific item on that index number
# mylist.pop()
mylist.pop(1)
print(mylist)