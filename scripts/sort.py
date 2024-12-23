import utils
import sys
import json

SORT_KEY = ""

def sort_by(e):
    global SORT_KEY
    return e[SORT_KEY]

items = utils.load_data(sys.argv[1])

for key in sys.argv[3:]:
    SORT_KEY = key
    items[sys.argv[2]].sort(key = sort_by)

utils.save_data(items, sys.argv[1], True)