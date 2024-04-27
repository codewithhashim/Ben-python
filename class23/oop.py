# OOP stands for Object Oriented Programming.
# It is a programming paradigm that focuses on creating objects.

# what is an object?
# An object is a real world entity that has property (defined by variables) and behavior (defined by methods).  A method is simply a function.


# An object is an instance of a class.


# what is an instance of a class means?
# An instance is a specific object created from a class.

# example of a Person class.
# Person class properties:
# Name, Age, Gender, Address, Phone Number, etc.
# Object is obj1 and the properties are Ben, 25, Male, etc.


# class is a blueprint for creating objects.
# A blueprint is a template for creating an object.
# In english blueprint is a sketch of a house, in this case it is a structure on the top of which we define our objects.


class Person:
    name = "Ben"

# create an object 
obj1 = Person()

# creating a second object (instance) of the Person class.
obj2 = Person()