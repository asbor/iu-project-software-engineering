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
                <button @click="importRecipe">Import</button>
            </div>
        </div>


        <!-- Display unique fermentables separately -->
        <div v-if="uniqueFermentables.length > 0">
            <h2>Unique Fermentables:</h2>
            <ul> <!-- Render BeerXMLFermentableCard for selected recipes -->

                <li v-for="(fermentable, index) in uniqueFermentables" :key="index">
                    {{ fermentable }}
                </li>


            </ul>
        </div>
        <main class="grid w-full gap-4">
            <div class="grid gap-4 lg:grid-cols-4">
                <BeerXMLFermentableCard v-for="(fermentable, index) in uniqueFermentables" :key="index"
                    :card="fermentable" />
            </div>

        </main>

    </div>
</template>

<script>
import { version } from 'vue';

export default {
    data() {
        return {
            xmlData: null,
            recipe: [],
            selectedRecipe: [],
            uniqueFermentables: [] // Store unique fermentables
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
            const fermentables = new Set(); // Use Set to store unique fermentables
            for (let i = 0; i < recipeNodes.length; i++) {
                const recipeNode = recipeNodes[i];
                // Extract other recipe details...

                // Extract fermentables
                const fermentableNodes = recipeNode.getElementsByTagName("FERMENTABLE");
                for (let j = 0; j < fermentableNodes.length; j++) {
                    const fermentableNode = fermentableNodes[j];
                    const fermentableName = fermentableNode.getElementsByTagName("NAME")[0].textContent;
                    // Extract all attributes for the fermentable
                    const fermentableAttributes = {
                        name: fermentableName,
                        // Add more attributes here as needed
                        /*
                        <NAME>Pale Malt (2 Row) UK</NAME>
                        <VERSION>1</VERSION>
                        <TYPE>Grain</TYPE>
                        <AMOUNT>3.628736</AMOUNT>
                        <YIELD>78.0</YIELD>
                        <COLOR>2.5</COLOR>
                        <ADD_AFTER_BOIL>FALSE</ADD_AFTER_BOIL>
                        <ORIGIN>United Kingdom</ORIGIN>
                        <SUPPLIER/>
                        <NOTES>
                        Base malt for all English beer styles Lower diastatic power than American 2 Row Pale Malt
                        </NOTES>
                        <COARSE_FINE_DIFF>1.5</COARSE_FINE_DIFF>
                        <MOISTURE>4.0</MOISTURE>
                        <DIASTATIC_POWER>45.0</DIASTATIC_POWER>
                        <PROTEIN>10.1</PROTEIN>
                        <MAX_IN_BATCH>100.0</MAX_IN_BATCH>
                        <RECOMMEND_MASH>FALSE</RECOMMEND_MASH>
                        <IBU_GAL_PER_LB>0.000</IBU_GAL_PER_LB>
                        <DISPLAY_AMOUNT>8.00 lb</DISPLAY_AMOUNT>
                        <INVENTORY>8.00 lb</INVENTORY>
                        <POTENTIAL>1.036</POTENTIAL>
                        <DISPLAY_COLOR>2.5 SRM</DISPLAY_COLOR>
                        */

                        version: fermentableNode.getElementsByTagName("VERSION")[0].textContent,
                        type: fermentableNode.getElementsByTagName("TYPE")[0].textContent,
                        amount: fermentableNode.getElementsByTagName("AMOUNT")[0].textContent,
                        yield: fermentableNode.getElementsByTagName("YIELD")[0].textContent,
                        color: fermentableNode.getElementsByTagName("COLOR")[0].textContent,
                        origin: fermentableNode.getElementsByTagName("ORIGIN")[0].textContent,
                        supplier: fermentableNode.getElementsByTagName("SUPPLIER")[0].textContent,
                        notes: fermentableNode.getElementsByTagName("NOTES")[0].textContent,

                        // Add more attributes here as needed
                    };
                    fermentables.add(fermentableAttributes); // Add fermentable to Set
                }

                // Extract other ingredients...

                // Build recipe object...
            }
            this.recipe = recipe;
            this.uniqueFermentables = Array.from(fermentables); // Convert Set to array for rendering
        },
        async importRecipe() {
            try {
                // Import recipe logic...
            } catch (error) {
                console.error(error);
                alert("Failed to import recipe.");
            }
        }
    }
};
</script>
