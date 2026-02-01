.PHONY: sort actions sort-backgrounds sort-bestiary sort-conditions sort-deities sort-feats sort-items sort-languages sort-optionalfeatures sort-races sort-spells sort-variantrules

sort-actions:
	@python3 ./scripts/sort.py homebrew/ishiir-actions.json action name

sort-backgrounds:
	@python3 ./scripts/sort.py homebrew/ishiir-backgrounds.json background name

sort-bestiary:
	@python3 ./scripts/sort.py homebrew/ishiir-bestiary.json monster name

sort-conditions:
	@python3 ./scripts/sort.py homebrew/ishiir-conditions.json condition name

sort-deities:
	@python3 ./scripts/sort.py homebrew/ishiir-deities.json deity name pantheon

sort-feats:
	@python3 ./scripts/sort.py homebrew/ishiir-feats.json feat name

sort-items:
	@python3 ./scripts/sort.py homebrew/ishiir-items-base.json baseitem name type
	@python3 ./scripts/sort.py homebrew/ishiir-items.json item name value crafted

sort-languages:
	@python3 ./scripts/sort.py homebrew/ishiir-languages.json language name type

sort-optionalfeatures:
	@python3 ./scripts/sort.py homebrew/ishiir-optionalfeatures.json optionalfeature name featureType

sort-races:
	@python3 ./scripts/sort.py homebrew/ishiir-races.json race name

sort-spells:
	@python3 ./scripts/sort.py homebrew/ishiir-spells.json spell name

sort-variantrules:
	@python3 ./scripts/sort.py homebrew/ishiir-variantrules.json variantrule name

sort: actions sort-backgrounds sort-bestiary sort-conditions sort-deities sort-feats sort-items sort-languages sort-optionalfeatures sort-races sort-spells sort-variantrules
