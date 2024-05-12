class Person:    
    def __init__(self, my_name, age, nationality, car):
        self.my_name = my_name
        self.age = age
        self.nationality = nationality
        self.car = car
    
    def attr(self):
        print(f"Hi my name is {self.my_name} and I am {self.age}, and I am a {self.nationality} and my fav car is {self.car}")


alex = Person("Alex", 12, "Chinese", "Mustang") 
# alex.attr()

ben = Person("Ben", 14, "Ethiopean", "Mercedez") 
# ben.attr()

# jade = Person() 


# def check_age(parameter):
#     pass

# check_age("argument")


# var = "Some kind of value"

# print(f"hi there {var}")


# Inheritance
# When a subclass inherits properties from a superclass.

# OR
# when one class (child class) inherit some properties (attributes) from another class (parent class).

class Vehicle:
    def __init__(self, name_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
    
    def start(self):
        pass
    
    def stop(self):
        pass


class Car(Vehicle):
    def __init__(self, name_of_vehicle, brand):
        super().__init__(name_of_vehicle)
        self.brand = brand
        print(f"this car is {self.name_of_vehicle} and the brand is {self.brand}")
        
class Bus(Vehicle):
    def __init__(self, name_of_vehicle):
        super().__init__(name_of_vehicle)
        print(f"this bus is {self.name_of_vehicle}")


bmw = Car("BMW", "BMW Brand")

youtong = Bus("Youtong")