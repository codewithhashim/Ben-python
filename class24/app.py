# Class is a blueprint or template that defines the structure and behaviour of objects.

# 1) Properties / Attributes 
# 2) Methods
# 3) Instantiation 
# 4) Constructor 
# 5) Inheritance (We are not going to talk about this today)

# class is a keyword
# Car is the name of the class, and it is just conventional to start the name of class with a capital letter.

class Car:
    name_of_car = "BMW C200" #attribute
    
    # Constructor: A constructor is a special method (Function) that is automatically called when an object is instantiated (an object is being created).
    
    # self is a parameter. The self parameter reference the current instance (object)
    
    # The first parameter in a method is always self. This is how the class will know which object it is operating on.
    
    
    def __init__(self):
        pass
    
    # method -> A method is a function that is defined within a class. A method describe the behaviour or actions that the object can perform.
    def drive(self):
        print()
    
    def turn(self):
        print()
    
    def parking_assist(self):
        print()
    
# Instantiation
bmw = Car()
mercedez = Car()
toyota = Car()