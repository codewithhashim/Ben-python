# pass statement
# pass statement is used as a placeholder for the future code.

if 10 > 4:
    pass

# for loop
# in python for loop is used to iterate over a sequence of elements.

# Syntax
# for element in sequence:
#     pass

greetings = "Hello"
for letter in greetings:
    if letter == "l":
        continue
    # print(letter)

# combining pass, break, continue
names = "David bloom"
for letter in names:
    if letter == "m":
        break
    elif letter == " ":
        continue
    elif letter == "o":
        pass
    # print(letter)


# String
string_one = 'Hello first string'
string_two = "Hello there second string"
string_three = ''' Hello the third string
I am multi-line string
and I carry a different way of writing
 
 
 
 
 '''
print(string_three)