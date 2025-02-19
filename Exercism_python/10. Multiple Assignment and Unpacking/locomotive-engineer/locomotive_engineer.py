"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # args is a tuple so we are converting into a list using List packing and avoiding list() constructor
    *wagon_list, = args
    return wagon_list

# print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    new_1_id, new_2_id, loco_id, *remaining_ids = each_wagons_id
    *arranged_list, = loco_id, *missing_wagons, *remaining_ids, new_1_id, new_2_id
    return arranged_list
    
# print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))


# This one is difficult but important in that one line. We need to understand how the * is used to unpack dictionary views too

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    
    # Note: kwargs.values() produces a dict.values([the values]) view inside the list brackets - not what we want
    # Therefore, we unpack this view using * (used for unpacking tuples,lists and views like dicts.keys() or .values() or .items())
    # *kwargs.values() will not unpack without a list or tuple. Since, there are multiple values to unpack and python won't know where to place them without being in an iterable
    
    route = {**route, "stops":[*kwargs.values()]}
    return route

# print(add_missing_stops({"from": "New York", "to": "Miami"},
#                       stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                       stop_4="Jacksonville", stop_5="Orlando")
# )

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    
    return {**route, **more_route_information}

# print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50", "temp":90}))

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # Asked to return a list with 3 rows
    # What is Fixed: Each color has 3 wagons (sub-lists' length is always 3)
    # What is not fixed: Colors (broadly speaking, number of colors or number of sub-lists in our input or no. of columns in our return)
    
    # get each of the 3 items in each sublist and throw them inside their corresponding columns

    # My solution 
    # depot_arrangement_1 = []
    # depot_arrangement_2 = []
    # depot_arrangement_3 = []
    # for color_item in wagons_rows:
    #     item_1, item_2, item_3 = color_item
    #     depot_arrangement_1.append(item_1)
    #     depot_arrangement_2.append(item_2)
    #     depot_arrangement_3.append(item_3)
    
    # *depot_arrangement, = depot_arrangement_1, depot_arrangement_2, depot_arrangement_3

    # ChatGPT's extremely intelligent solution
    # zip() performs the transpose operation and returns sub-tuples but we need sub-lists

    *depot_arrangement, = zip(*wagons_rows)
    
    return [[*column] for column in depot_arrangement]

# print(fix_wagon_depot([
#                     [(2, "red"), (4, "red"), (8, "red")],
#                     [(5, "blue"), (9, "blue"), (13,"blue")],
#                     [(3, "orange"), (7, "orange"), (11, "orange")],
#                     ]))