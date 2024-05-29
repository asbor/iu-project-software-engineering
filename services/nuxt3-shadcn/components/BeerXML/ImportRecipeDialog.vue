<script setup>
import { ref } from 'vue';
import { XMLParser } from 'fast-xml-parser';

// Assuming these components are imported correctly
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from '@/components/ui/alert-dialog';

const { loading, open } = useHelpers();
const importedRecipes = ref([]);
let nextId = 1;  // Initialize a counter for IDs

function handleFileChange(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = () => {
    const beerXMLContent = reader.result;
    parseBeerXML(beerXMLContent);
  };
  reader.readAsText(file);
}

function parseBeerXML(beerXMLContent) {
  const parser = new XMLParser();
  const result = parser.parse(beerXMLContent);

  if (!result.RECIPES || !result.RECIPES.RECIPE) {
    console.error('No recipes found in BeerXML');
    return;
  }

  const recipes = result.RECIPES.RECIPE;

  importedRecipes.value = recipes.map((recipe) => {
    // Debug: Log each recipe before mapping
    console.log('Mapping Recipe:', recipe);

    return {
      id: nextId++,  // Use an integer ID
      name: recipe.NAME ? recipe.NAME : '',
      version: recipe.VERSION ? parseInt(recipe.VERSION) : 0,
      type: recipe.TYPE ? recipe.TYPE : '',
      brewer: recipe.BREWER ? recipe.BREWER : '',
      asst_brewer: recipe.ASST_BREWER ? recipe.ASST_BREWER : '',
      batch_size: recipe.BATCH_SIZE ? parseFloat(recipe.BATCH_SIZE) : 0,
      boil_size: recipe.BOIL_SIZE ? parseFloat(recipe.BOIL_SIZE) : 0,
      boil_time: recipe.BOIL_TIME ? parseInt(recipe.BOIL_TIME) : 0,
      efficiency: recipe.EFFICIENCY ? parseFloat(recipe.EFFICIENCY) : 0,
      notes: recipe.NOTES ? recipe.NOTES : '',
      taste_notes: recipe.TASTE_NOTES ? recipe.TASTE_NOTES : '',
      taste_rating: recipe.TASTE_RATING ? parseFloat(recipe.TASTE_RATING) : 0,
      og: recipe.OG ? parseFloat(recipe.OG) : 0,
      fg: recipe.FG ? parseFloat(recipe.FG) : 0,
      fermentation_stages: recipe.FERMENTATION_STAGES ? parseInt(recipe.FERMENTATION_STAGES) : 0,
      primary_age: recipe.PRIMARY_AGE ? parseInt(recipe.PRIMARY_AGE) : 0,
      primary_temp: recipe.PRIMARY_TEMP ? parseFloat(recipe.PRIMARY_TEMP) : 0,
      secondary_age: recipe.SECONDARY_AGE ? parseInt(recipe.SECONDARY_AGE) : 0,
      secondary_temp: recipe.SECONDARY_TEMP ? parseFloat(recipe.SECONDARY_TEMP) : 0,
      tertiary_age: recipe.TERTIARY_AGE ? parseInt(recipe.TERTIARY_AGE) : 0,
      age: recipe.AGE ? parseInt(recipe.AGE) : 0,
      age_temp: recipe.AGE_TEMP ? parseFloat(recipe.AGE_TEMP) : 0,
      carbonation_used: recipe.CARBONATION_USED ? recipe.CARBONATION_USED : '',
      est_og: recipe.EST_OG ? parseFloat(recipe.EST_OG) : 0,
      est_fg: recipe.EST_FG ? parseFloat(recipe.EST_FG) : 0,
      est_color: recipe.EST_COLOR ? parseFloat(recipe.EST_COLOR) : 0,
      ibu: recipe.IBU ? parseFloat(recipe.IBU) : 0,
      ibu_method: recipe.IBU_METHOD ? recipe.IBU_METHOD : '',
      est_abv: recipe.EST_ABV ? parseFloat(recipe.EST_ABV) : 0,
      abv: recipe.ABV ? parseFloat(recipe.ABV) : 0,
      actual_efficiency: recipe.ACTUAL_EFFICIENCY ? parseFloat(recipe.ACTUAL_EFFICIENCY) : 0,
      calories: recipe.CALORIES ? parseFloat(recipe.CALORIES) : 0,
      display_batch_size: recipe.DISPLAY_BATCH_SIZE ? recipe.DISPLAY_BATCH_SIZE : '',
      display_boil_size: recipe.DISPLAY_BOIL_SIZE ? recipe.DISPLAY_BOIL_SIZE : '',
      display_og: recipe.DISPLAY_OG ? recipe.DISPLAY_OG : '',
      display_fg: recipe.DISPLAY_FG ? recipe.DISPLAY_FG : '',
      display_primary_temp: recipe.DISPLAY_PRIMARY_TEMP ? recipe.DISPLAY_PRIMARY_TEMP : '',
      display_secondary_temp: recipe.DISPLAY_SECONDARY_TEMP ? recipe.DISPLAY_SECONDARY_TEMP : '',
      display_tertiary_temp: recipe.DISPLAY_TERTIARY_TEMP ? recipe.DISPLAY_TERTIARY_TEMP : '',
      display_age_temp: recipe.DISPLAY_AGE_TEMP ? recipe.DISPLAY_AGE_TEMP : '',
      hops: recipe.HOPS && Array.isArray(recipe.HOPS) && recipe.HOPS.length > 0 ? recipe.HOPS.HOP.map((hop) => ({
        name: hop.NAME ? hop.NAME : '',
        origin: hop.ORIGIN ? hop.ORIGIN : '',
        alpha: hop.ALPHA ? parseFloat(hop.ALPHA) : 0,
        type: hop.TYPE ? hop.TYPE : '',
        form: hop.FORM ? hop.FORM : '',
        beta: hop.BETA ? parseFloat(hop.BETA) : 0,
        hsi: hop.HSI ? parseFloat(hop.HSI) : 0,
        amount: hop.AMOUNT ? parseFloat(hop.AMOUNT) : 0,
        use: hop.USE ? hop.USE : '',
        time: hop.TIME ? parseInt(hop.TIME) : 0,
        notes: hop.NOTES ? hop.NOTES : '',
        display_amount: hop.DISPLAY_AMOUNT ? hop.DISPLAY_AMOUNT : '',
        inventory: hop.INVENTORY ? hop.INVENTORY : '',
        display_time: hop.DISPLAY_TIME ? hop.DISPLAY_TIME : '',
      })) : [],

      fermentables: recipe.FERMENTABLES && Array.isArray(recipe.FERMENTABLES) && recipe.FERMENTABLES.length > 0 ? recipe.FERMENTABLES.FERMENTABLE.map((fermentable) => ({
        name: fermentable.NAME ? fermentable.NAME : '',
        type: fermentable.TYPE ? fermentable.TYPE : '',
        amount: fermentable.AMOUNT ? parseFloat(fermentable.AMOUNT) : 0,
        yield_: fermentable.YIELD ? parseFloat(fermentable.YIELD) : 0,
        color: fermentable.COLOR ? parseInt(fermentable.COLOR) : 0,
        origin: fermentable.ORIGIN ? fermentable.ORIGIN : '',
        supplier: fermentable.SUPPLIER ? fermentable.SUPPLIER : '',
        notes: fermentable.NOTES ? fermentable.NOTES : '',
        potential: fermentable.POTENTIAL ? parseInt(fermentable.POTENTIAL) : 0,
        cost_per_unit: fermentable.COST_PER_UNIT ? parseFloat(fermentable.COST_PER_UNIT) : 0,
        manufacturing_date: fermentable.MANUFACTURING_DATE ? parseDate(fermentable.MANUFACTURING_DATE) : null,
        expiry_date: fermentable.EXPIRY_DATE ? parseDate(fermentable.EXPIRY_DATE) : null,
        lot_number: fermentable.LOT_NUMBER ? fermentable.LOT_NUMBER : '',
        exclude_from_total: fermentable.EXCLUDE_FROM_TOTAL ? fermentable.EXCLUDE_FROM_TOTAL : 'False',
        not_fermentable: fermentable.NOT_FERMENTABLE ? fermentable.NOT_FERMENTABLE : 'False',
        description: fermentable.DESCRIPTION ? fermentable.DESCRIPTION : '',
        substitutes: fermentable.SUBSTITUTES ? fermentable.SUBSTITUTES : '',
        used_in: fermentable.USED_IN ? fermentable.USED_IN : '',
        recipe_id: fermentable.RECIPE_ID ? parseInt(fermentable.RECIPE_ID) : 0,
        inventory_id: fermentable.INVENTORY_ID ? parseInt(fermentable.INVENTORY_ID) : 0,
        batch_id: fermentable.BATCH_ID ? parseInt(fermentable.BATCH_ID) : 0,
      })) : [],

      yeasts: recipe.YEASTS && Array.isArray(recipe.YEASTS) && recipe.YEASTS.length > 0 ? recipe.YEASTS.map((yeast) => ({
        name: yeast.NAME ? yeast.NAME : '',
        version: yeast.VERSION ? parseInt(yeast.VERSION) : 0,
        type: yeast.TYPE ? yeast.TYPE : '',
        form: yeast.FORM ? yeast.FORM : '',
        amount: yeast.AMOUNT ? parseFloat(yeast.AMOUNT) : 0,
        amount_is_weight: yeast.AMOUNT_IS_WEIGHT ? yeast.AMOUNT_IS_WEIGHT === 'true' : false,
        laboratory: yeast.LABORATORY ? yeast.LABORATORY : '',
        product_id: yeast.PRODUCT_ID ? yeast.PRODUCT_ID : '',
        min_temperature: yeast.MIN_TEMPERATURE ? parseFloat(yeast.MIN_TEMPERATURE) : 0,
        max_temperature: yeast.MAX_TEMPERATURE ? parseFloat(yeast.MAX_TEMPERATURE) : 0,
        flocculation: yeast.FLOCCULATION ? yeast.FLOCCULATION : '',
        attenuation: yeast.ATTENUATION ? parseFloat(yeast.ATTENUATION) : 0,
        notes: yeast.NOTES ? yeast.NOTES : '',
        best_for: yeast.BEST_FOR ? yeast.BEST_FOR : '',
        times_cultured: yeast.TIMES_CULTURED ? parseInt(yeast.TIMES_CULTURED) : 0,
        max_reuse: yeast.MAX_REUSE ? parseInt(yeast.MAX_REUSE) : 0,
        add_to_secondary: yeast.ADD_TO_SECONDARY ? yeast.ADD_TO_SECONDARY : 'False',
        display_amount: yeast.DISPLAY_AMOUNT ? yeast.DISPLAY_AMOUNT : '',
        display_min_temp: yeast.DISP_MIN_TEMP ? yeast.DISP_MIN_TEMP : '',
        display_max_temp: yeast.DISP_MAX_TEMP ? yeast.DISP_MAX_TEMP : '',
        inventory: yeast.INVENTORY ? parseFloat(yeast.INVENTORY) : 0,
        culture_date: yeast.CULTURE_DATE ? parseDate(yeast.CULTURE_DATE) : null,
      })) : [],

      miscs: recipe.MISCS && Array.isArray(recipe.MISCS) && recipe.MISCS.length > 0 ? recipe.MISCS.map((misc) => ({
        name: misc.NAME ? misc.NAME : '',
        version: misc.VERSION ? parseInt(misc.VERSION) : 0,
        type: misc.TYPE ? misc.TYPE : '',
        use: misc.USE ? misc.USE : '',
        time: misc.TIME ? parseInt(misc.TIME) : 0,
        amount: misc.AMOUNT ? parseFloat(misc.AMOUNT) : 0,
        amount_is_weight: misc.AMOUNT_IS_WEIGHT ? misc.AMOUNT_IS_WEIGHT === 'true' : false,
        use_for: misc.USE_FOR ? misc.USE_FOR : '',
        notes: misc.NOTES ? misc.NOTES : '',
        display_amount: misc.DISPLAY_AMOUNT ? misc.DISPLAY_AMOUNT : '',
        inventory: misc.INVENTORY ? parseFloat(misc.INVENTORY) : 0,
        display_time: misc.DISPLAY_TIME ? misc.DISPLAY_TIME : '',
        batch_size: misc.BATCH_SIZE ? parseFloat(misc.BATCH_SIZE) : 0,
      })) : [],

      waters: recipe.WATERS && Array.isArray(recipe.WATERS) && recipe.WATERS.length > 0 ? recipe.WATERS.map((water) => ({
        name: water.NAME ? water.NAME : '',
        version: water.VERSION ? parseInt(water.VERSION) : 0,
        amount: water.AMOUNT ? parseFloat(water.AMOUNT) : 0,
        calcium: water.CALCIUM ? parseFloat(water.CALCIUM) : 0,
        bicarbonate: water.BICARBONATE ? parseFloat(water.BICARBONATE) : 0,
        sulfate: water.SULFATE ? parseFloat(water.SULFATE) : 0,
        chloride: water.CHLORIDE ? parseFloat(water.CHLORIDE) : 0,
        sodium: water.SODIUM ? parseFloat(water.SODIUM) : 0,
        magnesium: water.MAGNESIUM ? parseFloat(water.MAGNESIUM) : 0,
        ph: water.PH ? parseFloat(water.PH) : 0,
        notes: water.NOTES ? water.NOTES : '',
        display_amount: water.DISPLAY_AMOUNT ? water.DISPLAY_AMOUNT : '',
      })) : [],

      mash: recipe.MASH && Array.isArray(recipe.MASH) && recipe.MASH.length > 0 ? recipe.MASH.map((mash) => ({
        name: mash.NAME ? mash.NAME : '',
        version: mash.VERSION ? parseInt(mash.VERSION) : 0,
        grain_temp: mash.GRAIN_TEMP ? parseFloat(mash.GRAIN_TEMP) : 0,
        tun_temp: mash.TUN_TEMP ? parseFloat(mash.TUN_TEMP) : 0,
        sparge_temp: mash.SPARGE_TEMP ? parseFloat(mash.SPARGE_TEMP) : 0,
        ph: mash.PH ? parseFloat(mash.PH) : 0,
        notes: mash.NOTES ? mash.NOTES : '',
        tun_weight: mash.TUN_WEIGHT ? parseFloat(mash.TUN_WEIGHT) : 0,
        tun_specific_heat: mash.TUN_SPECIFIC_HEAT ? parseFloat(mash.TUN_SPECIFIC_HEAT) : 0,
        equip_adjust: mash.EQUIP_ADJUST ? mash.EQUIP_ADJUST : '',
        display_grain_temp: mash.DISPLAY_GRAIN_TEMP ? mash.DISPLAY_GRAIN_TEMP : '',
        display_tun_temp: mash.DISPLAY_TUN_TEMP ? mash.DISPLAY_TUN_TEMP : '',
        display_sparge_temp: mash.DISPLAY_SPARGE_TEMP ? mash.DISPLAY_SPARGE_TEMP : '',
      })) : [],

      fermentations: recipe.FERMENTATION && Array.isArray(recipe.FERMENTATION) && recipe.FERMENTATION.length > 0 ? recipe.FERMENTATION.map((fermentation) => ({
        name: fermentation.NAME ? fermentation.NAME : '',
        version: fermentation.VERSION ? parseInt(fermentation.VERSION) : 0,
        temp: fermentation.TEMP ? parseFloat(fermentation.TEMP) : 0,
        time: fermentation.TIME ? parseInt(fermentation.TIME) : 0,
        notes: fermentation.NOTES ? fermentation.NOTES : '',
        display_temp: fermentation.DISPLAY_TEMP ? fermentation.DISPLAY_TEMP : '',
      })) : [],

      style: recipe.STYLE && Array.isArray(recipe.STYLE) && recipe.STYLE.length > 0 ? {
        name: recipe.STYLE.NAME ? recipe.STYLE.NAME : '',
        version: recipe.STYLE.VERSION ? parseInt(recipe.STYLE.VERSION) : 0,
        category: recipe.STYLE.CATEGORY ? recipe.STYLE.CATEGORY : '',
        category_number: recipe.STYLE.CATEGORY_NUMBER ? parseInt(recipe.STYLE.CATEGORY_NUMBER) : 0,
        style_letter: recipe.STYLE.STYLE_LETTER ? recipe.STYLE.STYLE_LETTER : '',
        style_guide: recipe.STYLE.STYLE_GUIDE ? recipe.STYLE.STYLE_GUIDE : '',
        type: recipe.STYLE.TYPE ? recipe.STYLE.TYPE : '',
        og_min: recipe.STYLE.OG_MIN ? recipe.STYLE.OG_MIN : '',
        og_max: recipe.STYLE.OG_MAX ? recipe.STYLE.OG_MAX : '',
        fg_min: recipe.STYLE.FG_MIN ? recipe.STYLE.FG_MIN : '',
        fg_max: recipe.STYLE.FG_MAX ? recipe.STYLE.FG_MAX : '',
        ibu_min: recipe.STYLE.IBU_MIN ? recipe.STYLE.IBU_MIN : '',
        ibu_max: recipe.STYLE.IBU_MAX ? recipe.STYLE.IBU_MAX : '',
        color_min: recipe.STYLE.COLOR_MIN ? recipe.STYLE.COLOR_MIN : '',
        color_max: recipe.STYLE.COLOR_MAX ? recipe.STYLE.COLOR_MAX : '',
        carb_min: recipe.STYLE.CARB_MIN ? recipe.STYLE.CARB_MIN : '',
        carb_max: recipe.STYLE.CARB_MAX ? recipe.STYLE.CARB_MAX : '',
        abv_max: recipe.STYLE.ABV_MAX ? recipe.STYLE.ABV_MAX : '',
        abv_min: recipe.STYLE.ABV_MIN ? recipe.STYLE.ABV_MIN : '',
        notes: recipe.STYLE.NOTES ? recipe.STYLE.NOTES : '',
        profile: recipe.STYLE.PROFILE ? recipe.STYLE.PROFILE : '',
        ingredients: recipe.STYLE.INGREDIENTS ? recipe.STYLE.INGREDIENTS : '',
        examples: recipe.STYLE.EXAMPLES ? recipe.STYLE.EXAMPLES : '',
        display_og_min: recipe.STYLE.DISPLAY_OG_MIN ? recipe.STYLE.DISPLAY_OG_MIN : '',
        display_og_max: recipe.STYLE.DISPLAY_OG_MAX ? recipe.STYLE.DISPLAY_OG_MAX : '',
        display_fg_min: recipe.STYLE.DISPLAY_FG_MIN ? recipe.STYLE.DISPLAY_FG_MIN : '',
        display_fg_max: recipe.STYLE.DISPLAY_FG_MAX ? recipe.STYLE.DISPLAY_FG_MAX : '',
        display_color_min: recipe.STYLE.DISPLAY_COLOR_MIN ? recipe.STYLE.DISPLAY_COLOR_MIN : '',
        display_color_max: recipe.STYLE.DISPLAY_COLOR_MAX ? recipe.STYLE.DISPLAY_COLOR_MAX : '',
        og_range: recipe.STYLE.OG_RANGE ? recipe.STYLE.OG_RANGE : '',
        fg_range: recipe.STYLE.FG_RANGE ? recipe.STYLE.FG_RANGE : '',
        ibu_range: recipe.STYLE.IBU_RANGE ? recipe.STYLE.IBU_RANGE : '',
        carb_range: recipe.STYLE.CARB_RANGE ? recipe.STYLE.CARB_RANGE : '',
        color_range: recipe.STYLE.COLOR_RANGE ? recipe.STYLE.COLOR_RANGE : '',
        abv_range: recipe.STYLE.ABV_RANGE ? recipe.STYLE.ABV_RANGE : '',
      } : null,
    };
  });

  // Debug: Log the final mapped recipes
  console.log('Imported Recipes:', importedRecipes.value);
}

const existingRecipeNames = ref([]);

async function fetchExistingRecipeNames() {
  try {
    const response = await fetch('http://localhost:8000/recipes');
    if (response.ok) {
      const data = await response.json();
      existingRecipeNames.value = data.map(recipe => recipe.name);
    } else {
      throw new Error('Failed to fetch existing recipes');
    }
  } catch (error) {
    console.error('Error fetching existing recipes:', error);
  }
}

async function importRecipes() {
  await fetchExistingRecipeNames();  // Fetch existing recipe names
  const maxRetries = 3;

  for (const recipe of importedRecipes.value) {
    if (existingRecipeNames.value.includes(recipe.name)) {
      console.log(`Recipe "${recipe.name}" already exists. Skipping.`);
      continue;  // Skip if the recipe name already exists
    }

    let attempts = 0;
    let success = false;

    while (attempts < maxRetries && !success) {
      try {
        attempts++;
        const response = await fetch('http://localhost:8000/recipes', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(recipe),
        });

        if (!response.ok) {
          const errorData = await response.json();
          if (errorData.detail === "Recipe with this name already exists") {
            console.log(`Recipe "${recipe.name}" already exists. Skipping.`);
            success = true;
            continue;
          }
          throw new Error('Failed to create recipe');
        }

        success = true;
        console.log(`Recipe "${recipe.name}" imported successfully.`);
      } catch (error) {
        console.error(`Attempt ${attempts} failed for recipe "${recipe.name}": ${error}`);
        if (attempts >= maxRetries) {
          console.error(`Failed to import recipe "${recipe.name}" after ${attempts} attempts.`);
        }
      }
    }
  }

  open.value = false;
  window.location.reload();
}
</script>

<template>
  <AlertDialog :open="open">
    <AlertDialogTrigger>
      <button @click="open = true">Import Recipes</button>
    </AlertDialogTrigger>
    <AlertDialogContent aria-describedby="dialog-description">
      <AlertDialogHeader>
        <AlertDialogTitle>Import Recipes from BeerXML</AlertDialogTitle>
        <AlertDialogDescription id="dialog-description">
          Choose a BeerXML file to import recipes.
        </AlertDialogDescription>
      </AlertDialogHeader>
      <input type="file" @change="handleFileChange" accept=".xml" />
      <div v-if="importedRecipes.length > 0">
        <h2>Imported Recipes:</h2>
        <ul>
          <li v-for="recipe in importedRecipes" :key="recipe.id">
            {{ recipe.name }}
          </li>
        </ul>
      </div>
      <AlertDialogFooter>
        <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
        <AlertDialogAction @click="importRecipes">Import</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
