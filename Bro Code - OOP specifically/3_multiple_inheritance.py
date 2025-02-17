"""
------  multiple inheritance: inherit from more than 1 parent class
        e.g. class Child (Parent1, Parent2)

------  multi-level inheritance: inherit from a parent which inherits from another parent
        e.g. class Child (Parent2) <- class Parent2(Parent1) <- class Parent1 
"""

# Multiple Inheritance
# Parent

""" 
class Prey:
    def flee(self):
        print(f"This animal is fleeing")


class Predator:
    def hunt(self):
        print(f"This animal is hunting")

# Children:


class Rabbit(Prey):
    pass


class Hawk (Predator):
    pass


class Fish (Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

hawk.hunt()
fish.flee()
rabbit.flee()
fish.hunt()
"""
# Multi-level inheritance
# Rabbit inherits everything from Prey and Animal


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk (Predator):
    pass


class Fish (Prey, Predator):
    pass


rabbit = Rabbit("Bugs Bunny")
hawk = Hawk("Henery Hawk")
fish = Fish("Nemo")

hawk.hunt()
fish.flee()
rabbit.flee()
fish.hunt()
fish.sleep()
