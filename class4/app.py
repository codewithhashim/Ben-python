import keyword
print(keyword.kwlist)

hello = 45

HelloAll = 56

# The rules below are 9 but we can summarize them to 2 only 1) cannot start with a number and it should be alphanumeric ii) No keywords allowed to be used as Identifier name.

# Rules of writing variable names:

#1 Rule: Variable names must begin with letters or underscore (_)
asdf = "Greetings"
_age = 34
# $value = 45 We can use this in PHP but in Python

#2 Rule: Identifiers cannot start with a number.
# 11hello = 454  (NOT valid, because it starts with a number)
# 4ai = asdfad Not valid

#3 Rule: Identifiers can only cotnain alpha-numeric character and underscores
# Alphanumeric -> Alphabets and Numerals
# !heyyyy  = "" NOT valid
# hey! = "" Not valid

#4 Rule: Identifiers are case-sensative
Abc = 34
ABC = 2
AbC = 90

print(ABC)

#5 Rule: Cannot only contains of digits (Numbers)
# 12345 = "Hello" NOT VALID

#6 Rule:Keywords cannot be used as Identifiers (name of the variable)
_mycar = "Camry" # Valid 
# for = "12"  NOT valid, bc I am using a keyword as the name of the variable

#7 No limits on the length of the variable names 
s = "aseddfs"
asdhfaksdhkfjahsdkjfhaskdjfhasdkjhfaksdhfkjahsdkjhfakdshfkajsdhfkjahdjfadf = "value"

#8 Rules: Spaces are not allowed in between the variable name, if the variable names consist more than a single word
# green car = "Prius" NOT VALID, bc of the space between the variable name
#green_car = "Prius" Valid, bc no space.

#9 Rule: We can write the numbers at the end of the Identifier or in the middle of it.

elven11 = "11" #Valid 
amazon11walmart = "Valid"

# When do we need the quotation marks?
# we need the "" when we want to use the English words / any other words other than numbers, we will use "" or '', OR (''' Some kind of words here ''')
# Can we not write it for numbers?
# Yes we can. But if you want to use the numbers for mathematical operation, it is recommended that you would use without the quotes.