"use strict";

class PageFilterCrafting extends PageFilter {
	static _getToolDisplayText (tool) {
		if (tool === "anyArtisansTool") return "Any Artisan's Tool";
		return tool.toTitleCase();
	}

	static _getSkillDisplayText (skills) {
		return skills;
	}

	constructor () {
		super();

		this._skillFilter = new Filter({header: "Skills", displayFn: PageFilterCrafting._getSkillDisplayText.bind(PageFilterCrafting)});
		this._toolFilter = new Filter({header: "Tool", displayFn: PageFilterCrafting._getToolDisplayText.bind(PageFilterCrafting)});
	}

	static mutateForFilters (c) {
		c._fSources = SourceFilter.getCompleteFilterSources(c);
		const skillsDisplay = Renderer.crafting.getSkillsSummary(c.skills, true, c._fSkills = []);
		const toolDisplay = Renderer.crafting.getToolSummary(c.tool, true, c._fTools = []);
		c._fMisc = [];
		c._skillsDisplay = skillsDisplay;
		c._toolDisplay = toolDisplay;
	}

	addToFilters (c, isExcluded) {
		if (isExcluded) return;

		if (c._fSources !== "") {
			this._sourceFilter.addItem(c._fSources);
		}
		c._fSkills.forEach(skill => {
			this._skillFilter.addItem(skill);
		});
		if (c._fTools !== "") {
			this._toolFilter.addItem(c._fTools);
		}
	}

	async _pPopulateBoxOptions (opts) {
		opts.filters = [
			this._sourceFilter,
			this._skillFilter,
			this._toolFilter,
		];
	}

	toDisplay (values, c) {
		return this._filterBox.toDisplay(
			values,
			c._fSources,
			c._fSkills,
			c._fTools,
		);
	}
}