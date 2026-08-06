# # oops is on the basic of class and object
class Student:
    name = "John"

s1 = Student()
print(s1.name)  # Output: John

class Car:
    color = "Red"
    model = "Toyota"

car2 = Car()
print(car2.color)  # Output: Red
print(car2.model)  # Output: Toyota


# constructor is a special method in python class which is used
#  to initialize the object of the class. It is called when an object
#  of the class is created. The constructor method is defined 
# using the __init__() method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("mohit",30)  
print(p1.name)  # Output: mohit
print(p1.age)   # Output: 30
p1.display()