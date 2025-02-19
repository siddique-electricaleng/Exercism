"""
@property : Property Decorator, allows us to define a method as a property - the method can be accessed like an attribute

Benefit: Add additional logic when read(getter), write(setter) or delete(deleter) attributes
Gives getter, setter and deleter methods
"""

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # Using @property we are making these getter methods to read the attributes in the custom way
    @property
    def width(self):
        return f"{self.__width:.2f} cm"
    
    @property
    def height(self):
        return f"{self.__height:.2f} cm"
    
    # Setter methods: Done using decorators
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if (new_height)>0:
            self.__height = new_height
        else:
            print("Height must be greater than zero")


    # Deleter method, uses del keyword with objects:
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle1 = Rectangle(3,4)

# Using the setter method
rectangle1.width = 5
rectangle1.height = 5

# Using deleter method to delete these attributes
del rectangle1.width
del rectangle1.height

# Here we are actually obtaining the width & height through getter methods.
# The single underscore, _ is a convention used to show that the attributes are meant to be protected
print(rectangle1.width)
print(rectangle1.height)