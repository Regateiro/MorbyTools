"use strict";

class RenderItems {
	static _getRenderedSeeAlso (
		{
			item,
			prop,
			tag,
		},
	) {
		if (!item[prop]) return "";

		return `<div>${Renderer.get().render(`{@note See also: ${item[prop].map(it => `{@${tag} ${it}}`).join(", ")}.}`)}</div>`;
	}

	static $getRenderedItem (item) {
		const [damage, damageType, propertiesTxt] = Renderer.item.getDamageAndPropertiesText(item);
		const [typeRarityText, subTypeText, tierText] = Renderer.item.getTypeRarityAndAttunementText(item);

		let renderedText = Renderer.item.getRenderedEntries(item);
		renderedText += this._getRenderedSeeAlso({item, prop: "seeAlsoDeck", tag: "deck"});
		renderedText += this._getRenderedSeeAlso({item, prop: "seeAlsoVehicle", tag: "vehicle"});

		let itemSource = "Uncraftable"
		let craftMaterial = null
		let craftIngredients = null
		if (item.crafted) {
			let materialArr = []
			item.crafted.material?.forEach(function(mat) {
				if(mat.includes("Steel") || mat.includes("Mithral") || mat.includes("Adamantite") || mat.includes("Ingot")) {
					mat = `{@item Crafting Ingot|Ishiir|${mat}}`
				}
				else if(mat.includes("Wood") || mat.includes("Ironbark") || mat.includes("Livewood") || mat.includes("Mystoak")) {
					mat = `{@item Crafting Wood|Ishiir|${mat}}`
				}
				else if(mat.includes("Hide")) {
					mat = `{@item Crafting Hide|Ishiir|${mat}}`
				}
				else if(mat.includes("Draconic Scale")) {
					mat = `{@item Draconic Scales|Ishiir|${mat}}`
				}
				else if(mat.includes("Scale")) {
					mat = `{@item Crafting Scale|Ishiir|${mat}}`
				}
				materialArr.push(Renderer.get().render(`${mat}`))
			})
			craftMaterial = materialArr.join("<br>")

			let ingredientArr = []
			item.crafted.ingredient?.forEach(function(ing) {
				ingredientArr.push(Renderer.get().render(`{@item ${ing}|Ishiir}`))
			})
			craftIngredients = ingredientArr.join("<br>") || "&mdash;"
			
			itemSource = `${item.crafted.skill.join("/")} (+${item.crafted.dc || 0} DC)`
		}

		let brewMasteries = null
		if (item.brewMastery) {
			let masteryArr = []
			item.brewMastery.forEach(function(mastery) {
				masteryArr.push(Renderer.get().render(`{@optfeature ${mastery}|Ishiir}`))
			})
			brewMasteries = masteryArr.join(", ")
		}

		let ingSource = null
		if (item.ingredient) {
			let count = item.ingredient.harvestCount ? `${item.ingredient.harvestCount} × ${item.ingredient?.harvestSizeScaling || false ? "size" : "creature"}` : "\u2014"
			ingSource = `${item.ingredient.source} (${count})`
		}

		const textLeft = [Parser.itemValueToFullMultiCurrency(item), Parser.itemWeightToFull(item)].filter(Boolean).join(", ").uppercaseFirst();
		const textRight = [damage, damageType, propertiesTxt].filter(Boolean).join(" ");

		return $$`
			${Renderer.utils.getBorderTr()}
			${Renderer.utils.getExcludedTr({isExcluded: Renderer.item.isExcluded(item)})}
			${Renderer.utils.getNameTr(item, {page: UrlUtil.PG_ITEMS})}

			<tr><td class="rd-item__type-rarity-attunement" colspan="6">${Renderer.item.getTypeRarityAndAttunementHtml(typeRarityText, subTypeText, tierText)}</td></tr>

			${brewMasteries ? `<tr><td class="rd-item__type-masteries" colspan="6">Masteries: ${brewMasteries}</td></tr>` : ""}

			${ingSource ? `<tr><td class="rd-item__type-crafting" colspan="6">${ingSource}</td></tr>` : ""}
			${itemSource ? `<tr><td class="rd-item__type-crafting" colspan="6">${itemSource}</td></tr>` : ""}

			${craftMaterial && craftIngredients ? `<tr>
				<td colspan="3" style="vertical-align:top">${craftIngredients}</td>
				<td class="text-right" colspan="3" style="vertical-align:top">${craftMaterial}</td>
			</tr>` : craftMaterial || craftIngredients ? `<tr><td colspan="6" style="vertical-align:top" class="${craftMaterial ? "text-right" : ""}">${craftIngredients || craftMaterial}</td></tr>` : ""}

			${textLeft && textRight ? `<tr>
				<td colspan="2">${textLeft}</td>
				<td class="text-right" colspan="4">${textRight}</td>
			</tr>` : `<tr><td colspan="6" class="${textRight ? "text-right" : ""}">${textLeft || textRight}</td></tr>`}

			${renderedText ? `<tr><td class="divider" colspan="6"><div/></td></tr>
			<tr class="text"><td colspan="6">${renderedText}</td></tr>` : ""}
			${Renderer.utils.getPageTr(item, {tag: "item", fnUnpackUid: (uid) => DataUtil.proxy.unpackUid("item", uid, "item")})}
			${Renderer.utils.getBorderTr()}
		`;
	}
}
