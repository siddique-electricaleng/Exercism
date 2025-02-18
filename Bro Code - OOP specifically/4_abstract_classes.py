"""
Abstract Classes: Cannot be instantiated on its own and are meant to be subclassed.

Contains: abstract methods - declared, no implementations

Benefits of abstract classes:
1. Prevents instantiation of the class itself. Therefore, no objects from this class.
2. Requires children to use inherited abstract methods and define the abstract methods.
"""
from abc import ABC as abstract_base_class, abstractmethod


class Vehicle(abstract_base_class):

    # using the decorator, is same as:
    # def go(self)
    # ......
    # go = abstractmethod(go)
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Need to implement the abstract methods inside the child class - otherwise python won't let us to instantiate

# Children Classes from the Abstract class vehicle


class Car(Vehicle):

    def go(self):
        print("You start the car")

    def stop(self):
        print("You stop the car")


class MotorCycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


class Boat(Vehicle):
    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")


car = Car()
car.go()
car.stop()

motorcycle = MotorCycle()
motorcycle.go()
motorcycle.stop()

boat = Boat()
boat.go()
boat.stop()
