import utils
import json

def sort_by_name(e):
    return e['name']

def sort_by_level(e):
    return e.get('level', 0)

spells = utils.load_data("homebrew/ishiir-spells.json")

spells["spell"].sort(key = sort_by_name)
spells["spell"].sort(key = sort_by_level)

dmg_types = ["fire", "force", "radiant", "cold", "psychic", "necrotic", "bludgeoning", "lightning", "acid", "thunder", "poison", "piercing", "slashing"]

possible_matches = {}
for spell in spells["spell"]:
    for dmg_type in dmg_types:
        if dmg_type in str(spell["entries"]).lower() and "damage" in str(spell["entries"]).lower() and dmg_type not in spell.get("damageInflict", []):
            possible_matches[spell["name"]] = possible_matches.get(spell["name"], [])
            possible_matches[spell["name"]].append(dmg_type)

print(json.dumps(possible_matches))
