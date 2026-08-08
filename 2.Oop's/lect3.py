# abstraction and encupsulation

# abstractions 
# hidding the implementation details of the class only showing 
# the essential features of the class to the user
# Example1

class Vehicle:
    def __init__(self):
        self.engine = False
        self.brk = False

    def start_engine(self):
        self.engine = True
        self.brk = True
        print("engine started")

car1 = Vehicle()
car1.start_engine()


# Example2
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

car1 = Car()
car1.start_engine()


# Encapsulation:
# wrapping the data and methods that operate on the data into a single unit




class BankAccount:
    def __init__(self, name, balance):
        self.name = name  # public attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def getBalance(self):
        return self.__balance

acc = BankAccount("Mohit", 1000)
acc.deposit(500)
print(acc.getBalance())  # Output: 1500
# print(acc.__balance)  # This will raise an AttributeError 
# because __balance is private

      
        
    
        

    
