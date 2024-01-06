# count method for list

bens_numbers = [3, 4, 5, '3', '3', 6, 7, 8, '3', '3']
# print(bens_numbers.count('3'))

# sort()
bens_numbers_int = [3, 4, 5, 6, 7, 8, 2, 56, 7]
# bens_numbers_int.sort()  # ascending order by default
# bens_numbers_int.sort(reverse=True) -> descending order

# print(bens_numbers_int)

# bens_numbers_int.reverse()
# print(bens_numbers_int)

# for element in bens_numbers_int:
#     print(element)

# this array has 9 elements
index_number = 0
while index_number < len(bens_numbers_int):
    # print(bens_numbers_int[3])
    print(bens_numbers_int[index_number])
    index_number = index_number + 1


# index_number = 0
# while index_number < len(bens_numbers_int):
#     # we will see an index error, because it will print the number tat is higher than the index of the list, so that is why we will see an indexError
#     index_number = index_number + 1
#     print(bens_numbers_int[index_number])
