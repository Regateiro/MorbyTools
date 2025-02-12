import utils
import sys

def sort_by_name(e):
    return e['name']

def sort_by_level(e):
    return e.get('level', 0)

spells = utils.load_data("homebrew/ishiir-spells.json")

spells["spell"].sort(key = sort_by_name)
spells["spell"].sort(key = sort_by_level)

level = -1
count = 0
for spell in spells["spell"]:
    for _class in spell.get("classes", {}).get("fromClassList", []):
        if _class["name"].lower() == sys.argv[1].lower():
            if spell["level"] != level:
                level = spell["level"]
                print("\n" + str(level))

            count = count + 1
            print(spell["name"])

print(f"\nTotal: {count}")
