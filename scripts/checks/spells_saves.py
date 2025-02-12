import json

def load_data(file: str) -> dict:
    with open(file, "r", encoding="utf-8") as df:
        return json.load(df)

def sort_by_name(e):
    return e['name']

def sort_by_level(e):
    return e['level']

spells = load_data("homebrew/ishiir-spells.json")

spells["spell"].sort(key = sort_by_name)
#spells["spell"].sort(key = sort_by_level)

saves = ["strength", "constitution", "dexterity", "intelligence", "wisdom", "charisma"]

possible_matches = {}
for spell in spells["spell"]:
    for save in saves:
        if save in str(spell["entries"]).lower() and "saving throw" in str(spell["entries"]).lower() and save not in spell.get("savingThrow", []):
            possible_matches[spell["name"]] = possible_matches.get(spell["name"], [])
            possible_matches[spell["name"]].append(save)

print(json.dumps(possible_matches))
