# range() in python.

# 0 is inclusive, while the last value which in this case is 5, is exclusive.
# for number in range(5):
#     print(number)

# the starting number is inclusive, and the last is exclusive
# for number in range(5, 17):
#     print(number)


# Step to print number
# add 5 to every iteration
# for number in range(5, 50, 5):
#     print(number)


# print even numbers
# for number in range(2,20,2):
#     print(number)

# print the numbers in reverse order, but you will have switch the big number with the smaller one.
# for number in range(20,2,-2):
#     print(number)

# While loop with a list
# in a list the index starts at 0
# number of elements in list_here list is 6.
# the max index number thou is 5.
# 0(1), 1(2), 2(4), 3(5),4(6),5(45)
list_here = [1, 2, 4, 5, 6, 45]

# while loop
# while condition:
# code here

index_number = 0
while index_number < len(list_here):
    # print(list_here[index_number])
    index_number = index_number + 1



str_list = ["hello", "hi"]
ij = 0
while ij < len(str_list):
    print(str_list[ij])
    ij = ij + 1

# increment -> increasing
# decrement -> decreasing
    

# Tuples in Python
# ordered and immutable collection of elements.

# mutable -> If it can be changed, this means it is mutable
# immutable -> something that cannot be changed.
