import json
import sys

def load_data(file: str) -> dict:
    with open(file, "r", encoding="utf-8") as df:
        return json.load(df)

def sort_by_name(e):
    return e['name']

def sort_by_level(e):
    return e['level']

spells = load_data("homebrew/ishiir-spells.json")

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
