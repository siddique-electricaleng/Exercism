"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory_dict = dict()
    
    for item in items:
        if item not in inventory_dict.keys():
            inventory_dict[item] = items.count(item)
    return inventory_dict

# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    # inventory argument is the return from create_inventory function
    # modify it and return it

    for item in items:
        if item in inventory.keys():
            inventory[item] += 1
        elif item not in inventory.keys():
            inventory[item] = 1
        else:
            print(f"Invalid key: {item}")
    return inventory

# Test:
# print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in inventory.keys() and inventory[item] > 0:            
            inventory[item] -= 1
        else:
            continue
    return inventory

# Test
# print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory.keys():
        inventory.pop(item)
    
    return inventory

# print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = list()
    for key, value in inventory.items():
        if value > 0:
            inventory_list.append((key,value))
    return inventory_list

print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))

