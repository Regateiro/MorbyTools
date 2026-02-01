.PHONY: sort sort-feats sort-spells

sort-feats:
	@python3 ./scripts/sort.py homebrew/ishiir-feats.json feat name

sort-spells:
	@python3 ./scripts/sort.py homebrew/ishiir-spells.json spell name

sort: sort-feats sort-spells
