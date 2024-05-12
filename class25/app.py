class Person:    
    def __init__(self, my_name, age, nationality, car):
        self.my_name = my_name
        self.age = age
        self.nationality = nationality
        self.car = car
    
    def attr(self):
        print(f"Hi my name is {self.my_name} and I am {self.age}, and I am a {self.nationality} and my fav car is {self.car}")


alex = Person("Alex", 12, "Chinese", "Mustang") 
alex.attr()

ben = Person("Ben", 14, "Ethiopean", "Mercedez") 
ben.attr()

jade = Person() 


# def check_age(parameter):
#     pass

# check_age("argument")


# var = "Some kind of value"

# print(f"hi there {var}")