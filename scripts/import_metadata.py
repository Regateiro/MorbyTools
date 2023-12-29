import os
import sys
from utils import save_data, load_data

# Constants
HOMEBREW_FOLDER = './homebrew'
HOMEBREW_SPELLS = 'ishiir-spells.json'
SPELLS_FOLDER = './data/spells'


# Load Homebrew Metadata
HOMEBREW_METADATA = load_data(
    os.path.join(HOMEBREW_FOLDER, 'ishiir-metadata.json')
)


# Apply Spell Metadata
def apply_metadata_spells(source: dict, target: dict) -> None:
    for s_spell in source['spell']:
        # Handle Spell Renamings
        s_spell['name'] = HOMEBREW_METADATA['spell_renames'].get(s_spell['name'], s_spell['name'])
        # Search for the Homebrew Spell
        for t_spell in [s for s in target['spell'] if s['name'] == s_spell['name']]:
            # Update metadata
            for key in HOMEBREW_METADATA['spell_metadata_keys']:
                if s_spell.get(key):
                    if key == "miscTags":
                        t_miscTags = t_spell.get(key, [])
                        for tag in [t for t in s_spell.get(key) if t not in t_miscTags]:
                            t_miscTags.append(tag)
                        t_spell[key] = t_miscTags
                    else:
                        t_spell[key] = s_spell[key]


# Apply Homebrew Spell Metadata
def apply_homebrew_metadata_spells(data: dict) -> None:
    # For each spell
    for spell in data['spell']:
        # Check if there is homebrew metadata to apply
        metadata = HOMEBREW_METADATA['spell_metadata'].get(spell['name'], None)
        if metadata is not None:
            # Apply each key in the metadata to the spell
            for key in metadata.keys():
                spell[key] = metadata[key]
                # Remove the entry if it is empty
                if not spell[key]:
                    del spell[key]
            
            # Tag the spell as a setting exclusive version
            spellTags = spell.get('miscTags', [])
            if 'SAD' not in spellTags:
                spellTags.append('SAD')
                spell['miscTags'] = spellTags


# Import All Spell Related Files
def import_spells() -> None:
    # Construct the path of the file to update
    homebrew_filepath = os.path.join(HOMEBREW_FOLDER, HOMEBREW_SPELLS)
    # Read Files
    homebrew_data = load_data(homebrew_filepath)
    official_data = []
    for filename in os.listdir(SPELLS_FOLDER):
        path = os.path.join(SPELLS_FOLDER, filename)
        # check if it is a main release file
        if os.path.isfile(path) and filename.startswith('spells') and not filename.startswith('spells-ua'):
            official_data.append(load_data(path))

    # Process Data
    for data in official_data:
        apply_metadata_spells(data, homebrew_data)

    # Reapply homebrew spell changes
    apply_homebrew_metadata_spells(homebrew_data)

    # Save the Processed Data
    save_data(homebrew_data, homebrew_filepath, True)


# Main function
def main() -> None:
    target = sys.argv[1]

    if target == 'spells':
        import_spells()


# Call the main function if the script was called directly
if __name__ == '__main__':
    main()
