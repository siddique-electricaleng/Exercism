"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    # Idea: count occurrences of each item inside the tuple and store the name : occurrences in a temporary dictionary
    # Check if the the key inside temporary dictionary exists inside the current inventory
    #  If key exists, add the occurrences from temp_cart to current inventory
    # If doesn't exist, add the key:Occurrences wholly to the current inventory
    temp_cart = dict()
    for item in items_to_add:
        # The condition below, helps avoid existing items from being rewritten
        if item not in temp_cart:
            # Add the key : occurrences into the temp_cart
            temp_cart[item] = items_to_add.count(item)

    # Now check if key from temp_cart exists inside current inventory
    for temp_item in temp_cart.keys():
        current_items = current_cart.keys()

        if temp_item not in current_items:
            current_cart[temp_item] = temp_cart[temp_item]

        elif temp_item in current_items:
            current_cart[temp_item] = current_cart[temp_item] + temp_cart[temp_item]
    return current_cart

# print(add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
#               ['Banana', 'Orange', 'Blueberries', 'Banana']))   

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    user_shopping_cart = dict()
    return user_shopping_cart.fromkeys(notes, 1)

# print(read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple']))

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    # Assuming the outermost iterable for recipe_updates is either a list or a tuple - not a dictionary. For dictionaries looping and accessing as below won't work, need to user next and iter functions then
    recipe_updates_dict = dict()

    # The outermost loop returns the inner iterable either a list of a tuple - but generally a tuple I can say, following their examples.
    #  Therefore, item is a tuple. To get the recipe name, use item[0]
    for item in recipe_updates:
        recipe_updates_dict[item[0]] = item[1]
    
    ideas.update(recipe_updates_dict)
 
    return ideas

# print(update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#                     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
# (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))
# )

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))

# print(sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1}))

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    # return a dict with each item having values as a list [quantity, location, refrigeration needed or not] 
    cart_items = cart.keys()
    map_items = aisle_mapping.keys()
    fulfillment_dict = dict()

    for single_map_item in map_items:
        if single_map_item in cart_items:
            fulfillment_dict[single_map_item] = [cart[single_map_item], aisle_mapping[single_map_item][0], aisle_mapping[single_map_item][1]]
    
    return dict(reversed(sorted(fulfillment_dict.items())))
    # needs to be sorted in reverse alphabetical order

# print(send_to_store(
    # user's cart
    # {'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
    # mapping contains each key from user's cart as a dictionary with values being a list [location refrigeration information]
    # {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    fulfillment_cart_item_names = fulfillment_cart.keys()
    store_inventory_item_names = store_inventory.keys()
    for single_fulfillment_item in fulfillment_cart_item_names:
        if single_fulfillment_item in store_inventory_item_names:
            if (store_inventory[single_fulfillment_item][0] > 0) and (store_inventory[single_fulfillment_item][0] > fulfillment_cart[single_fulfillment_item][0]):
                store_inventory[single_fulfillment_item][0] = store_inventory[single_fulfillment_item][0] - fulfillment_cart[single_fulfillment_item][0]
            elif store_inventory[single_fulfillment_item][0] <= 0 or (store_inventory[single_fulfillment_item][0] == fulfillment_cart[single_fulfillment_item][0]):
                store_inventory[single_fulfillment_item][0] = 'Out of Stock'
        else:
            # Out of Stock
            store_inventory[single_fulfillment_item] = 'Out of Stock'
    
    return store_inventory

# print(
#     update_store_inventory(
#             {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
#             {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}
#         )
#     )