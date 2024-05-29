<template>
    <div class="w-full">
        <div class="flex">
            <div>
                <input type="file" @change="handleFileUpload">
            </div>
            <div>
                <div v-if="recipe && recipe.length">
                    <h2>Recipe:</h2>
                    <ul>
                        <li v-for="(recipe, index) in recipe" :key="index">
                            <label>
                                <input type="checkbox" v-model="selectedRecipe" :value="recipe">
                                {{ recipe.name }}
                            </label>
                        </li>
                    </ul>
                </div>
                <div v-else>
                    <p>No recipe found.</p>
                </div>
            </div>
            <div>
                <p>Import selected recipe:</p>
                <Button @click="importRecipe">Import</button>
            </div>
        </div>
        <div v-if="selectedRecipe.length > 0" class="grid gap-4 lg:grid-cols-3">
            <XMLBeerCard v-for='( recipe, index ) in selectedRecipe' :card="recipe" :key='index' />
        </div>
    </div>

</template>


<script>
export default {
    data() {
        return {
            xmlData: null,
            recipe: [],
            selectedRecipe: []
        };
    },
    methods: {
        async handleFileUpload(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const xmlContent = e.target.result;
                    this.xmlData = xmlContent;
                    this.parseXMLData();
                };
                reader.readAsText(file);
            }
        },
        async parseXMLData() {
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(this.xmlData, "text/xml");
            const recipeNodes = xmlDoc.getElementsByTagName("RECIPE");
            const recipe = [];
            for (let i = 0; i < recipeNodes.length; i++) {
                const recipeNode = recipeNodes[i];
                const name = recipeNode.getElementsByTagName("NAME")[0].textContent;
                const type = recipeNode.getElementsByTagName("TYPE")[0].textContent;
                const brewer = recipeNode.getElementsByTagName("BREWER")[0].textContent;
                const batchSize = recipeNode.getElementsByTagName("BATCH_SIZE")[0].textContent;
                // Extract other recipe details as needed

                // Extract hop
                const hop = [];
                const hopNodes = recipeNode.getElementsByTagName("HOP");
                for (let j = 0; j < hopNodes.length; j++) {
                    const hopNode = hopNodes[j];
                    const hopName = hopNode.getElementsByTagName("NAME")[0].textContent;
                    const hopAmount = hopNode.getElementsByTagName("AMOUNT")[0].textContent;
                    const hopUse = hopNode.getElementsByTagName("USE")[0].textContent;
                    const hopTime = hopNode.getElementsByTagName("TIME")[0].textContent;
                    // Extract other hop details as needed
                    hop.push({ name: hopName, amount: hopAmount, use: hopUse, time: hopTime });
                }

                const fermentable = [];
                const fermentableNodes = recipeNode.getElementsByTagName("FERMENTABLE");
                for (let j = 0; j < fermentableNodes.length; j++) {
                    const fermentableNode = fermentableNodes[j];
                    const fermentableName = fermentableNode.getElementsByTagName("NAME")[0].textContent;
                    const fermentableAmount = fermentableNode.getElementsByTagName("TYPE")[0].textContent;
                    const fermentableUse = fermentableNode.getElementsByTagName("NOTES")[0].textContent;
                    // Extract other fermentable details as needed
                    fermentable.push({ name: fermentableName, amount: fermentableAmount, use: fermentableUse });
                }

                const misc = [];
                const miscNodes = recipeNode.getElementsByTagName("MISC");
                for (let j = 0; j < miscNodes.length; j++) {
                    const miscNode = miscNodes[j];
                    const miscName = miscNode.getElementsByTagName("NAME")[0].textContent;
                    // Extract other misc details as needed
                    misc.push({ name: miscName });
                }

                const yeasts = [];
                const yeastNodes = recipeNode.getElementsByTagName("YEAST");
                for (let j = 0; j < yeastNodes.length; j++) {
                    const yeastNode = yeastNodes[j];
                    const yeastName = yeastNode.getElementsByTagName("NAME")[0].textContent;
                    // Extract other yeast details as needed
                    yeasts.push({ name: yeastName });
                }

                const styles = [];
                const styleNodes = recipeNode.getElementsByTagName("STYLE");
                for (let j = 0; j < styleNodes.length; j++) {
                    const styleNode = styleNodes[j];
                    const styleName = styleNode.getElementsByTagName("NAME")[0].textContent;
                    const OG_min = styleNode.getElementsByTagName("OG_MIN")[0].textContent;
                    const OG_max = styleNode.getElementsByTagName("OG_MAX")[0].textContent;
                    const FG_min = styleNode.getElementsByTagName("FG_MIN")[0].textContent;
                    const FG_max = styleNode.getElementsByTagName("FG_MAX")[0].textContent;
                    const IBU_min = styleNode.getElementsByTagName("IBU_MIN")[0].textContent;
                    const IBU_max = styleNode.getElementsByTagName("IBU_MAX")[0].textContent;
                    const color_min = styleNode.getElementsByTagName("COLOR_MIN")[0].textContent;
                    const color_max = styleNode.getElementsByTagName("COLOR_MAX")[0].textContent;
                    const abv_min = styleNode.getElementsByTagName("ABV_MIN")[0].textContent;
                    const abv_max = styleNode.getElementsByTagName("ABV_MAX")[0].textContent;
                    const notes = styleNode.getElementsByTagName("NOTES")[0].textContent;
                    const profile = styleNode.getElementsByTagName("PROFILE")[0].textContent;

                    // Extract other style details as needed
                    styles.push({
                        name: styleName,
                        OG: `${OG_min} - ${OG_max}`,
                        FG: `${FG_min} - ${FG_max}`,
                        IBU: `${IBU_min} - ${IBU_max}`,
                        color: `${color_min} - ${color_max}`,
                        ABV: `${abv_min} - ${abv_max}`,
                        notes,
                        profile
                    });
                }


                recipe.push({ name, type, brewer, batchSize, hop, fermentable, misc, yeasts, styles });
            }
            this.recipe = recipe;
        },
        async importRecipe() {
            try {
                const response = await fetch("http://localhost:8000/api/recipe/import", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(this.selectedRecipe)
                });
                if (response.ok) {
                    alert("Recipe imported successfully!");
                } else {
                    alert("Failed to import recipe.");
                }
                await this.parseXMLData();
            } catch (error) {
                console.error(error);
                alert("Failed to import recipe.");
            }
        }
    }
};
</script>
