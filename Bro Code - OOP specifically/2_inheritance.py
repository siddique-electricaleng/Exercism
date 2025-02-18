"""
Inheritance:
A child class inherits
attributes & 
methods
from a parent class

Inheritance is 'is-a' relationship

class Child (Parent)
Child/Subclass inherit from Parent/SuperClass
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof Woof Waawwwf biyach!!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow")


class Mouse(Animal):
    def speak(self):
        print(f"{self.name} says squeak")


dog = Dog("Nolan")
cat = Cat("Tom")
mouse = Mouse("Mickey")
print(dog.name)
print(dog.is_alive)

dog.speak()
cat.speak()
cat.eat()
cat.sleep()
mouse.speak()
