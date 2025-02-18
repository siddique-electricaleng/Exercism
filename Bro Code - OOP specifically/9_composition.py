"""
Composition:
The composed object directly owns its components,
it cannot exist independently

Composition is 'owns-a' relationship

Basically 1 object acts as a container (the whole), containing other objects (the parts)
"""


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Wheel:
    def __init__(self, size):
        self.size = size

# Composed object is Car - it directly owns Wheel and Engine Objects in the constructor and cannot exist without them


class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        # This is how composition works. Car owns the Engine & wheel objects
        self.engine = Engine(horse_power)
        # cars have 4 wheels so write a list comprehension to create 4 Wheel objects for us
        self.wheel = [Wheel(wheel_size) for wheel in range(4)]

    def __str__(self):
        return f"{self.make} {self.model} {self.engine.horsepower} (hp) {self.wheel[0].size} inch"


car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

print(car1)
print(car2)
