import json
import re

# Load a JSON file into memory
def load_data(file: str) -> dict:
    with open(file) as df:
        return json.load(df)


# Save a JSON file into storage
def save_data(data: dict, file: str, pretty: bool = False) -> None:
    with open(file, 'w') as df:
        json.dump(data, df, indent=4 if pretty else None)


def _join_entries(entries: list) -> list:
    ret = []
    
    for entry in entries:
        _builder = []
        i = 0
        while True:
            # Go through the fields to produce an entry
            for field in entry:
                _builder.append(field[i if i < len(field) else -1])
            _entry = ' '.join(_builder)

            # Break the cycle if the same entry is produced twice
            if ret and ret[-1] == _entry:
                break

            # Add the new entry and prepare for the next
            ret.append(_entry)
            _builder.clear()
            i = i + 1

    return ret


def _process_craft_list(line: str) -> list:
    REPLACERS = {
        'P': 'Piercing',
        'B': 'Bludgeoning',
        'S': 'Slashing'
    }
    
    # If the line is not empty
    if line and line != '-':
        # Remove references
        if '@' in line:
            regex = r'\{@item ([^|}]*)\|?([^|}]*)?\|?([^|}]*)?\}'
            display_name = re.sub(regex, '\\3', line).strip()
            line = display_name if display_name else re.sub(regex, '\\1', line).strip()

        # Split the line into entries
        entries = line.split('//')
        for entry in entries:
            # Split each entry by whilespaces into fields
            fields = entry.split()
            for field in fields:
                # Split each field by a slash into subfields
                subfields = field.strip().split('/')
                # Clean up the subfields and replace where needed
                subfields = [REPLACERS.get(s.strip(), s.strip()) for s in subfields]
                # Save the processed subfields
                fields[fields.index(field)] = subfields
            # Save the processed fields
            entries[entries.index(entry)] = fields
        
        # Rejoin the fields
        line = _join_entries(entries)
    else:
        line = []

    return line


def parse_crafting_row(row: list) -> dict:
    # Parse item reference
    regex = r'\{@item ([^|}]*)\|?([^|}]*)?\|?([^|}]*)?\}'
    name = re.sub(regex, '\\1', row[0]).strip()
    source = re.sub(regex, '\\2', row[0]).strip()
    display_name = re.sub(regex, '\\3', row[0]).strip()
    
    # Parse the other fields
    dc = int(row[1]) if row[1] != '-' else None
    materials = []
    requirements = []
    if len(row) == 4:
        ingredients = row[2]
        value = row[3]
    elif len(row) == 5:
        ingredients = row[2]
        value = row[4]
    elif len(row) == 6:
        materials = row[2]
        ingredients = row[3]
        requirements = row[4]
        value = row[5]

    materials = _process_craft_list(materials)
    ingredients = _process_craft_list(ingredients)
    requirements = _process_craft_list(requirements)
    value = int(value.replace('.', '').split()[0].strip()) * 100
    
    return {
        'name': name,
        'source': source,
        'display': display_name,
        'dc': dc,
        'materials': materials,
        'ingredients': ingredients,
        'requirements': requirements,
        'value': value
    }