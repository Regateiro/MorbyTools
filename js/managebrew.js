"use strict";

class ManageBrew {
	static async pInitialise () {
		return ManageBrew.pRender();
	}

	static async pRender () {
		const manager = new ManageBrewUi();
		return manager.pRender($(`#brewmanager`).empty());
	}
}

window.addEventListener("load", async () => {
	ExcludeUtil.pInitialise(); // don't await, as this is only used for search
	await ManageBrew.pInitialise();

	window.dispatchEvent(new Event("toolsLoaded"));
});
