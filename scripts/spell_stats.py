import utils
import sys

def sort_by_name(e):
    return e['name']

def sort_by_level(e):
    return e.get('level', 0)

spells = utils.load_data("homebrew/ishiir-spells.json")

spell_levels = [0] * 10
spell_schools = {
    "V": [0] * 10,
    "T": [0] * 10,
    "C": [0] * 10,
    "A": [0] * 10,
    "E": [0] * 10,
    "N": [0] * 10,
    "D": [0] * 10,
    "I": [0] * 10,
}
spell_dmgtypes = {
    "fire": [0] * 10,
    "radiant": [0] * 10,
    "cold": [0] * 10,
    "force": [0] * 10,
    "necrotic": [0] * 10,
    "bludgeoning": [0] * 10,
    "psychic": [0] * 10,
    "acid": [0] * 10,
    "lightning": [0] * 10,
    "thunder": [0] * 10,
    "poison": [0] * 10,
    "piercing": [0] * 10,
    "slashing": [0] * 10
}
spell_saves = {
    "strength": [0] * 10,
    "dexterity": [0] * 10,
    "constitution": [0] * 10,
    "intelligence": [0] * 10,
    "wisdom": [0] * 10,
    "charisma": [0] * 10
}
spell_conditions = {
    "blinded": [0] * 10,
    "restrained": [0] * 10,
    "prone": [0] * 10,
    "charmed": [0] * 10,
    "incapacitated": [0] * 10,
    "dazed": [0] * 10,
    "frightened": [0] * 10,
    "frozen": [0] * 10,
    "deafened": [0] * 10,
    "stunned": [0] * 10,
    "unconscious": [0] * 10,
    "invisible": [0] * 10,
    "petrified": [0] * 10,
    "paralyzed": [0] * 10,
    "exhaustion": [0] * 10,
    "lacerated": [0] * 10,
    "poisoned": [0] * 10,
    "grappled": [0] * 10
}


def parse(word) -> str:
    if word == "V":
        return "Evocation"
    if word == "T":
        return "Transmutation"
    if word == "C":
        return "Conjuration"
    if word == "A":
        return "Abjuration"
    if word == "E":
        return "Enchantment"
    if word == "N":
        return "Necromancy"
    if word == "D":
        return "Divination"
    if word == "I":
        return "Illusion"
    return word.capitalize()


for spell in spells["spell"]:
    spell_levels[spell["level"]] = spell_levels[spell["level"]] + 1
    spell_schools[spell["school"]][spell["level"]] = spell_schools[spell["school"]][spell["level"]] + 1
    for dmgtype in spell.get("damageInflict", []):
        spell_dmgtypes[dmgtype][spell["level"]] = spell_dmgtypes[dmgtype][spell["level"]] + 1
    for save in spell.get("savingThrow", []):
        spell_saves[save][spell["level"]] = spell_saves[save][spell["level"]] + 1
    for condition in spell.get("conditionInflict", []):
        spell_conditions[condition][spell["level"]] = spell_conditions[condition][spell["level"]] + 1


print("*** Number of Spells ***")
print(','.join(["#"] + [str(x) for x in spell_levels]))
print()
print("*** Spells per School of Magic ***")
for school in spell_schools:
    print(','.join([parse(school)] + [str(x) for x in spell_schools[school]]))
print()
print("*** Spells per Damage Type ***")
for dmgtype in spell_dmgtypes:
    print(','.join([parse(dmgtype)] + [str(x) for x in spell_dmgtypes[dmgtype]]))
print()
print("*** Spells by Save ***")
for save in spell_saves:
    print(','.join([parse(save)] + [str(x) for x in spell_saves[save]]))
print()
print("*** Spells by Condition ***")
for condition in spell_conditions:
    print(','.join([parse(condition)] + [str(x) for x in spell_conditions[condition]]))
