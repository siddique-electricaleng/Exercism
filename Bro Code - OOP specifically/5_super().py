"""
super():
A method used in ----> child class(subclass).
Calls methods from --> parent class(superclass).
Allows the child class to extend the functionality of inherited methods.
"""
# Parent class


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(
            f"It is a {self.color} {self.__class__.__name__} and {'filled' if self.is_filled else 'not filled'}")

# Children Class


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    # Method overriding happens - happens by overriding the parent below
    """ 
    def describe(self):
        print(
            f"It is a circle with an area of {3.14*self.radius**2:.1f} cm\u00b2")
    """
    # Here we are extending the functionality using super() as opposed to above

    def describe(self):
        print(
            f"It is a circle with an area of {3.14*self.radius**2:.1f} cm\u00b2")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle(color="Red", is_filled=True, radius=4)
circle.describe()
