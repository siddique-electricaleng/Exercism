"""
Abstract Classes: Cannot be instantiated on its own and are meant to be subclassed.

Contains: abstract methods - declared, no implementations

Benefits of abstract classes:
1. Prevents instantiation of the class
2. Requires children to use inherited abstract methods
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    # using the decorator, is same as:
    # go = abstractmethod(go)
