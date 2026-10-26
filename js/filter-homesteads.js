"use strict";

class PageFilterHomesteads extends PageFilter {
	static mutateForFilters (h) {
		h._fSources = SourceFilter.getCompleteFilterSources(h);
	}

	addToFilters (h, isExcluded) {
		if (isExcluded) return;

		this._sourceFilter.addItem(h._fSources);
	}

	async _pPopulateBoxOptions (opts) {
		opts.filters = [
			this._sourceFilter,
		];
	}

	toDisplay (values, h) {
		return this._filterBox.toDisplay(
			values,
			h._fSources,
		);
	}
}

globalThis.PageFilterHomesteads = PageFilterHomesteads;
