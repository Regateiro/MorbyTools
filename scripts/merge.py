import json
import sys
import os

HOMEBREW_FOLDER = str(sys.argv[1])
HOMEBREW_PREFIX = str(sys.argv[2])

data = {
     "_meta": {
        "sources": [
            {
                "json": "Ishiir",
                "abbreviation": "Ishiir",
                "full": "Ishiir",
                "color": "#337ab7",
                "authors": [
                    "Sieg"
                ],
                "convertedBy": [
                    "Morb"
                ]
            }
        ]
    },
    "action": [],
    "background": [],
    "class": [],
    "classFeature": [],
    "condition": [],
    "feat": [],
    "optionalfeature": [],
    "spell": [],
    "subclass": [],
    "subclassFeature": [],
}

for filename in os.listdir(HOMEBREW_FOLDER):
    if not filename.startswith(HOMEBREW_PREFIX) or filename.endswith("-old.json") or filename.endswith("-merged.json"):
        continue

    with open(file=os.path.join(HOMEBREW_FOLDER, filename), mode="r", encoding="utf-8") as file:
        filedata: dict = json.load(file)
        data["action"].extend(filedata.get("action", []))
        data["background"].extend(filedata.get("background", []))
        data["class"].extend(filedata.get("class", []))
        data["classFeature"].extend(filedata.get("classFeature", []))
        data["condition"].extend(filedata.get("condition", []))
        data["feat"].extend(filedata.get("feat", []))
        data["optionalfeature"].extend(filedata.get("optionalfeature", []))
        data["spell"].extend(filedata.get("spell", []))
        data["subclass"].extend(filedata.get("subclass", []))
        data["subclassFeature"].extend(filedata.get("subclassFeature", []))

with open(file=os.path.join(HOMEBREW_FOLDER, f"{HOMEBREW_PREFIX}-merged.json"), mode="w", encoding="utf-8") as file:
    json.dump(data, file)
