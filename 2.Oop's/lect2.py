# # classes and instances
# # instance or object both same thing 

from turtle import color


class Car:
    car_company = "Toyota"  # class variable
    def __init__(self, model, color):
        self.model = model  # instance variable
        self.color = color  # instance variable 
        print("Car created")

s1 = Car("Nexon", "Red")
print(s1.model, s1.color)  # Output: Nexon Red

s2 = Car("Fortuner", "Black")
print(s2.model, s2.color)  # Output: Fortuner Black
print(s1.car_company)  # Output: Toyota



# methods in python class
# methods are the functions that belong to the obejcts

# dyanmic method: methods that can be called on an object of a class and 
# can access
#  the instance variables of the object.

class Student: 
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Helllo", self.name)



s1 = Student("John")
print(s1.name)  # Output: John'
s1.hello()  # Output: Hello John


# Static methos: methods that not use  self parameter 

class Student:
    @staticmethod #decorator
    def hello():
        print ("Hello")

Student.hello() # Output: Hello



