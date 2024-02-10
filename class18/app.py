# function - block of code that we can reuse with a function call

def eat_pizza():
    # print("Lets eat pizza! ")
    pass


eat_pizza()

# example2 about scope and parameters / arguments

# function with basic functionality and no good structure
# Parameters

# big_burger = "big" -> globaly defined function.


def eat_burger(mode_of_payment, delivery_charges):
    big_burger = "2 pounds"
    small_burger = "half pound"
    user_says = input("What is size? ")

    if user_says == "b":
        print("The order is " + big_burger + " it is " + mode_of_payment +
              " and the delivery charges are: " + delivery_charges)

    if user_says == "s":
        print("The order is " + small_burger + " it is " + mode_of_payment +
              " and the delivery charges are: " + delivery_charges)

# eat_burger("COD", "$5")
# eat_burger("Online payment", "$10")


def eat_fries():
    user_says = input("How much fries choose by answering  S, M, L: ")

    def anything_else():
        user_says_anything = input("What else would you like? ")
        print("Thank you for looking out here but we do not provide anything else")

    if user_says == "s" or user_says == "S":
        print("That will be $3.")
        anything_else()

    elif user_says == "m" or user_says == "M":
        print("That will be $5.")
        anything_else()

    elif user_says == "l" or user_says == "L":
        print("That will be $7.")
        anything_else()

    else:
        print("Wrong selection, check again")
        eat_fries()


eat_fries()
