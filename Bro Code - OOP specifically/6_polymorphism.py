"""
Polymorphism - greek word for many forms or faces
Poly = Many
Morphe = Form

2 ways to achieve polymorphism:
1. Inheritance = An object could be treated of the same type as a parent class
2. Duct typing = Object must have necessary attributes/methods
"""
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# Children
# Each children has multiple forms:
# e.g. Circle has the forms:
# 1. Circle
# 2. Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.height = height
        self.base = base

    def area(self):
        return self.base * self.height * 0.5

# We can create subclass of the Circle Subclass
# Our pizza has 3 forms:
# Pizza
# Circle
# Shape


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(3), Square(4), Triangle(2, 3), Pizza("Pepperoni", 12)]
for shape in shapes:
    print(f"{shape.area():>10.2f} cm\u00b2")
