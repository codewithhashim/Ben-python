# list

# alex_list = [45, 4, "Hi 👋"]
# print(alex_list[1])


# set in unordered and unique collection of elements

# A set
bens_set = {34, 8, 1, 999, 1}  # 1 is not unique

alex_set = {999, 34, 8, 1}
alex_set.add(45)
alex_set.add(456)


print(alex_set)
# print(alex_set[2]) -> it will raise an error: TypeError: 'set' object is not subscriptable

# membership test
if 999 in alex_set:
    print("Yes it is in the set.")

# iterate over a set / loop over a set

# for item in alex_set:
#     print(item)

# subset and superset

set_of_bills = {1, 2, 20, 100}
set_of_small_bills = {1, 2}
is_subset = set_of_small_bills.issubset(set_of_bills)
# print(is_subset)


is_supperset = set_of_bills.issuperset(set_of_small_bills)
# print(is_supperset)


# for loop is use to iterate over a sequence. List, tuple, dictionary (to be covered soon) etc

alex_list = [45, 4, "Hi 👋"]
for pizza in alex_list:
    print(pizza)

# loop on a string
for characters in "Oregon":
    print(characters)

# for loop with range() function
for xy in range(5):
    print(xy)