"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(num_layers):
    """Calculate the total preparation time before baking. Each layer takes 2 mins (PREPARATION_TIME)

    :param num_layers: int - number of layers of the cake.
    :return: int - total prepartion time (in minutes) using 'PREPARATION_TIME'.

    Function that takes the total layers prepared for the lasagna as
    an argument and returns how many minutes it took to prepare all layers
    based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME*num_layers


def elapsed_time_in_minutes(num_layers,elapsed_bake_time):
    """Calculate the total cooking time (Preparation + Baking)

    :param num_layers: int - number of layers of the cake.
    :param elapsed_bake_time: int - time passed since the baking begun.
    :return: int - total cooking time (in minutes).

    Function that takes the number of layers for cake and how long it has been baking as
    argument and returns how many minutes it took to cook the lasagna.
    """
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time
