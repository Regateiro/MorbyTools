"use strict";

class CraftingSublistManager extends SublistManager {
	constructor () {
		super({
			sublistClass: "subcrafting",
		});
	}

	pGetSublistItem (it, hash) {
		const skills = it._skillsDisplay;
		const tool = it._toolDisplay;

		const $ele = $$`<div class="lst__row lst__row--sublist ve-flex-col">
			<a href="#${hash}" class="lst--border lst__row-inner">
				<span class="bold col-8 pl-0">${it.name}</span>
				<span class="col-4 pr-0">${tool}</span>
				<span class="col-4 pr-0">${skills}</span>
			</a>
		</div>`
			.contextmenu(evt => this._handleSublistItemContextMenu(evt, listItem))
			.click(evt => this._listSub.doSelect(listItem, evt));

		const listItem = new ListItem(
			hash,
			$ele,
			it.name,
			{
				hash,
				source: Parser.sourceJsonToAbv(it.source),
				tool,
				skills,
			},
			{
				entity: it,
			},
		);

		return listItem;
	}
}

class CraftingPage extends ListPage {
	constructor () {
		const pageFilter = new PageFilterCrafting();
		super({
			dataSource: "data/crafting.json",

			pageFilter,

			listClass: "crafting",

			dataProps: ["crafting"],

			isPreviewable: false,
		});
	}

	getListItem (it, anI, isExcluded) {
		this._pageFilter.mutateAndAddToFilters(it, isExcluded);

		const eleLi = document.createElement("div");
		eleLi.className = `lst__row ve-flex-col ${isExcluded ? "lst__row--blacklisted" : ""}`;

		const name = it.name.replace("Variant ", "");
		const hash = UrlUtil.autoEncodeHash(it);
		const source = Parser.sourceJsonToAbv(it.source);

		eleLi.innerHTML = `<a href="#${hash}" class="lst--border lst__row-inner">
			<span class="bold col-4-5 pl-0">${name}</span>
			<span class="col-4-4 text-center">${it._toolDisplay}</span>
			<span class="col-4-2 text-center">${it._skillsDisplay}</span>
			<span class="col-1-4 text-center ${Parser.sourceJsonToColor(it.source)} pr-0" title="${Parser.sourceJsonToFull(it.source)}" ${BrewUtil2.sourceJsonToStyle(it.source)}>${source}</span>
		</a>`;

		const listItem = new ListItem(
			anI,
			eleLi,
			name,
			{
				hash,
				source,
				tool: it._toolDisplay,
				skill: it._skillsDisplay,
			},
			{
				isExcluded,
			},
		);

		eleLi.addEventListener("click", (evt) => this._list.doSelect(listItem, evt));
		eleLi.addEventListener("contextmenu", (evt) => this._openContextMenu(evt, this._list, listItem));

		return listItem;
	}

	handleFilterChange () {
		const f = this._filterBox.getValues();
		this._list.filter(item => this._pageFilter.toDisplay(f, this._dataList[item.ix]));
		FilterBox.selectFirstVisible(this._dataList);
	}

	_renderStats_doBuildStatsTab ({ent}) {
		this._$pgContent.empty().append(RenderCrafting.$getRenderedCrafting(ent));
	}
}

const craftingPage = new CraftingPage();
craftingPage.sublistManager = new CraftingSublistManager();
window.addEventListener("load", () => craftingPage.pOnLoad());
