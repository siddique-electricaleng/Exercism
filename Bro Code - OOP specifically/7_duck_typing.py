"""
Duck typing:
Another way to achieve polymorphism besides Inheritance
Object must have the minimum necessary attributes/methods
If it looks like a duck and quacks like a duck. it must be a duck.
"""


class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("MEOW")

# Here car used duck typing to achieve polymorphism:
# Recall: If it looks like a duck & quacks like a duck - it must be a duck
# Meaning, car has the necessary attributes and methods to say that it is an Animal, just like Dog and Cat
# Therefore, Car has the forms:
# 1. Car
# 2. Animal


class Car:
    alive = False

    def speak(self):
        print("Honk")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
