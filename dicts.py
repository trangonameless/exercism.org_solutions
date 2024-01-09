"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for key in items:
        if key not in inventory:
            inventory[key] = 1
        elif key in inventory:
            inventory[key] += 1
    return inventory


def add_items(inventory, items):
    for key in items:
        if key not in inventory:
            inventory[key] = 1
        elif key in inventory:
            inventory[key] += 1
    return inventory


def decrement_items(inventory, items):
    for key in items:
        if inventory[key] != 0:
            inventory[key] -= 1
    return inventory


def remove_item(inventory, item):
    inventory.pop(item, "Unknown")
    return inventory
        

def list_inventory(inventory):
    new_inventory = {}
    for key, value in inventory.items():
        if value != 0:
            new_inventory[key] = value
    inventory_list = list(new_inventory.items())
    return inventory_list
