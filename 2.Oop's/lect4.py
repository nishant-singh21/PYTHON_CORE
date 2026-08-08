# inherited class 
# class  Parent :
#     def speak(self):
#         print("speaking from parent class ")

# class Child(Parent):
#     pass

# c = Child()
# c. speak()


# class Animal:
#     def speak(self):
#         print("Animal speaks ")

# class Dog(Animal):
#     def speak(self):
#         print("Dog bark")

# class Cat(Animal):
#     def  speak(self):
#         print("Cat meows")

# d = Dog()
# c = Cat()
# d.speak() # output :Dog barks
# c.speak()


# polymorphism  one method use in multiple form 

# class Bird:
#     def make_sound(self):
#         print("chrip")

# class Cat:
#     def make_sound(self):
#         print("meow")


# for animal in [Bird() , Cat()]:
#     animal.make_sound()


class Employee:
    def work(self):
        print("Employee is working ")

class Devloper(Employee):
    def work(self):
        print("Devloper is coding")

class Manger(Employee):
    def work(self):
        print("Manager is managing")

for emp in [ Devloper() , Manger() ]:
    emp.work()




