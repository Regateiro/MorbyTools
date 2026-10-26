"use strict";

class HomesteadsSublistManager extends SublistManager {
	constructor () {
		super({
			sublistClass: "subhomesteads",
		});
	}

	static get _ROW_TEMPLATE () {
		return [
			new SublistCellTemplate({
				name: "Name",
				css: "bold col-9 pl-0",
				colStyle: "",
			}),
			new SublistCellTemplate({
				name: "Source",
				css: "ve-text-center col-3 pr-0",
				colStyle: "text-center",
			}),
		];
	}

	pGetSublistItem (it, hash) {
		const source = Parser.sourceJsonToAbv(it.source);
		const cellsText = [it.name, source];

		const $ele = $(`<div class="lst__row lst__row--sublist ve-flex-col">
			<a href="#${hash}" class="lst--border lst__row-inner">
				${this.constructor._getRowCellsHtml({values: cellsText})}
			</a>
		</div>`)
			.contextmenu(evt => this._handleSublistItemContextMenu(evt, listItem))
			.click(evt => this._listSub.doSelect(listItem, evt));

		const listItem = new ListItem(
			hash,
			$ele,
			it.name,
			{
				hash,
				source,
			},
			{
				entity: it,
				mdRow: [...cellsText],
			},
		);
		return listItem;
	}
}

class HomesteadsPage extends ListPage {
	constructor () {
		const pageFilter = new PageFilterHomesteads();
		super({
			dataSource: "data/homesteads.json",

			pageFilter,

			listClass: "homesteads",

			dataProps: ["homestead"],

			isPreviewable: false,
		});
	}

	getListItem (it, hI, isExcluded) {
		this._pageFilter.mutateAndAddToFilters(it, isExcluded);

		const eleLi = document.createElement("div");
		eleLi.className = `lst__row ve-flex-col ${isExcluded ? "lst__row--blocklisted" : ""}`;

		const source = Parser.sourceJsonToAbv(it.source);
		const hash = UrlUtil.autoEncodeHash(it);

		eleLi.innerHTML = `<a href="#${hash}" class="lst--border lst__row-inner">
			<span class="bold col-8 pl-0">${it.name}</span>
			<span class="col-4 ve-text-center ${Parser.sourceJsonToColor(it.source)} pr-0" title="${Parser.sourceJsonToFull(it.source)}" ${BrewUtil2.sourceJsonToStyle(it.source)}>${source}</span>
		</a>`;

		const listItem = new ListItem(
			hI,
			eleLi,
			it.name,
			{
				hash,
				source,
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
		this._$pgContent.empty().append(RenderHomesteads.$getRenderedHomestead(ent));
	}
}

const homesteadsPage = new HomesteadsPage();
homesteadsPage.sublistManager = new HomesteadsSublistManager();
window.addEventListener("load", () => homesteadsPage.pOnLoad());
