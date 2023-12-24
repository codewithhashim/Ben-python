time = "now"
for letter in time:
    if letter == "w":
        break
    print(letter)


# len() count the number of characters in a string
print(len("Hellooo therev#"))

# it will not work like len()
# print(count("asd"))

# count() counts the repeatition of a word in a string
my_name = "food guy eats more food than any body else who eats food"
# count_my_name = my_name.count("food")
count_my_name = my_name.count("o")

print(count_my_name)

# format
vehicle = "bike"
name_of_bike = "Yamaha"
stroke = 4
length = 100
bike = "Hello there my {} is {} and my bike has a {} stroke engine".format(
    vehicle, name_of_bike, stroke)
print(bike)


# substring()
greetings = "Congratulations"
subgreet = greetings[4]
print(subgreet)


# in (whether one string is in another string or not) - return a boolean value
print("h" in "hello")

# not in ("if it is not in that string") - return a boolean value
print("h" not in "hello")
