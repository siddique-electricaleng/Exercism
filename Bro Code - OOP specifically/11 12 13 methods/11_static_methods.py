"""
Static Method: Belongs to a class, rather than any object from that class (instance)

It is used for general utility functions.

-- Instance Methods = Best for operations on instances of the class (objects)

-- Static Methods = Best for utlity functions within a class, that do not need access to class data.
We don't need to rely on any objects to use the static method
"""


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # This is an instance method
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


# This is how we use the static method. Since it belongs to the class. Not to any object created from the class
is_valid_pos = Employee.is_valid_position("Rocket Scientist")
print(is_valid_pos)

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

print(employee3.is_valid_position(employee3.position))
