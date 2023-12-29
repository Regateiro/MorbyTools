import utils

def sort_by_name(e):
    return e['name']

def sort_by_value(e):
    return e.get('value', 0)

def sort_by_crafting(e):
    return e.get('crafted', {}).get('skill', [])

items = utils.load_data("homebrew/ishiir-items.json")

items["item"].sort(key = sort_by_name)
items["item"].sort(key = sort_by_value)
items["item"].sort(key = sort_by_crafting)

utils.save_data(items, "homebrew/ishiir-items.json", True)