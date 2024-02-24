#
# Dictionary is an unordered collection of items.

#  each item is stored as a key value pair.
# key -> value
# Key:
# Key should be unique
# Key cannot be changed
# Value:
# Value of a key can be any type of data and it ca be changed

# syntax
my_dictionary = {
    "key": "value"
}

# empty dictionary
items_collection = {}

# dictionary with some elements
anatomy = {
    "bones": 206,
    "fingers": 10,
    "is_complex": True,
    "name": "XYZ",
    "eyes_color": "brown",
    'age': 23
}

# print the dictionary
# print(anatomy)

# Accessing an element
# print(anatomy["name"])
# print(anatomy.get("is_complex"))

# update an element
anatomy["name"] = "ABC"
# print("After the update: ", anatomy["name"])

# add elements to a dictionary

anatomy["new_key"] = "New key new value"
# print(anatomy["new_key"])


# deleting an item
del anatomy["new_key"]
# print(anatomy)

# dictionary methods / functions
# returning all the keys
print(anatomy.keys())


# returning all the values
print(anatomy.values())

# returning all the item
print(anatomy.items())

# remove all the items
# print(anatomy.clear())

# remove an item of the passed key to the pop method
poppped_anatomy = anatomy.pop("age")
print(poppped_anatomy)
