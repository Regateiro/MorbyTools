import utils

def sort_by_name(e):
    return e['name']

def sort_by_level(e):
    return e.get('level', 0)

spells = utils.load_data("homebrew/ishiir-spells.json")

spells["spell"].sort(key = sort_by_name)
spells["spell"].sort(key = sort_by_level)

level = 0
print(level)
for spell in spells["spell"]:
    for _class in spell.get("classes", {}).get("fromClassList", []):
        if _class["name"] == "Summoner":
            if spell["level"] != level:
                level = spell["level"]
                print()
                print(level)
            print(spell["name"])
