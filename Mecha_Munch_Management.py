"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for key in items_to_add:
        if key in current_cart.keys():
            current_cart[key] += 1
        if key not in current_cart.keys():
            current_cart.setdefault(key, 1)
    return current_cart


def read_notes(notes):
    new_dict = dict.fromkeys(notes, 1)
    return new_dict


def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, isle_mapping):
    send_store = dict(sorted(cart.items(), reverse=True))
    for key, value in send_store.items():
        send_store[key] = [send_store[key], isle_mapping[key][0], isle_mapping[key][1]]
    return send_store


def update_store_inventory(fulfillment_cart, store_inventory):
    for product, details in fulfillment_cart.items():
        ordered_quantity = details[0]
        if product in store_inventory:
            store_inventory[product][0] -= ordered_quantity
            if store_inventory[product][0] <= 0:
                store_inventory[product][0] = 'Out of Stock'
    return store_inventory



