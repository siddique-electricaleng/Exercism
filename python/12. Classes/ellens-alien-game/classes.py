"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
    # Class attributes
    total_aliens_created = 0
    # Constructor function/ Dunder method
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        if (self.health > 0):
            self.health -= 1
        else:
            self.health = 0
        return self.health
    
    def is_alive(self):
        if (self.health > 0):
            return True
        else:
            return False
        
    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        return x_coordinate, y_coordinate
    
    def collision_detection(self, other_obj):
        pass

# Task 7 - Note: You need to see output in the question provided, to understand what the function does and how to make it below
def new_aliens_collection(alien_locations):
    alien_objs = list()
    for alien_location in alien_locations:
        alien_objs.append(Alien(alien_location[0],alien_location[1]))
    return alien_objs

