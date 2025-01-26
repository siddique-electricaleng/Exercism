"""Functions to automate Conda airlines ticketing system."""
import math
def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ["A", "B", "C", "D"]
    for num in range(number):
        yield seats[num % 4]
        
def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = ["A", "B", "C", "D"]
    row = 1
    seats_generated = 0

    while seats_generated < number:
        if (row == 13):
            row += 1
            continue

        for seat in seat_letters:
            yield f"{row}{seat}"
            seats_generated += 1
            if (seats_generated == number):
                return
        
        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    # Initiated generator object, using above function generate_seats() which generates the seat labels based on how many rows there are
    pass_seat = generate_seats(len(passengers))
    seating_plan = dict()

    # Looping through passenger names and getting them their designated seats with labels
    for person in passengers:
        seating_plan.update({person:next(pass_seat)})
    return seating_plan

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        rem_char = 12 - len(seat) - len(flight_id)
        if (rem_char > 0):
            ticket_suffix = "0"*rem_char
            res_string = f"{seat}{flight_id}{ticket_suffix}"
            yield res_string[:12]
        else:
            ticket_suffix = ""
            res_string = f"{seat}{flight_id}"
            yield res_string[:12]
        