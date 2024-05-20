<script setup>
import { ref, version } from 'vue';
import { parseString } from 'xml2js';
import { v4 as uuidv4 } from 'uuid';

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
} from '@/components/ui/alert-dialog'

const { loading, open } = useHelpers();
const importedRecipes = ref([]);

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
  parseString(beerXMLContent, (err, result) => {
    if (err) {
      console.error('Error parsing BeerXML:', err);
      return;
    }

    // Check if the XML contains recipes
    if (!result.RECIPES || !result.RECIPES.RECIPE) {
      console.error('No recipes found in BeerXML');
      return;
    }

    const recipes = result.RECIPES.RECIPE;

    // Debug: Log the recipes to inspect their structure
    console.log('Parsed Recipes:', recipes);

    importedRecipes.value = recipes.map((recipe) => {
      // Debug: Log each recipe before mapping
      console.log('Mapping Recipe:', recipe);

      return {
        name: recipe.NAME ? recipe.NAME[0] : '', // String
        version: recipe.VERSION ? parseInt(recipe.VERSION[0]) : 0, // Integer
        type: recipe.TYPE ? recipe.TYPE[0] : '', // String
        brewer: recipe.BREWER ? recipe.BREWER[0] : '', // String
        asst_brewer: recipe.ASST_BREWER ? recipe.ASST_BREWER[0] : '', // String
        batch_size: recipe.BATCH_SIZE ? parseFloat(recipe.BATCH_SIZE[0]) : 0, // Float
        boil_size: recipe.BOIL_SIZE ? parseFloat(recipe.BOIL_SIZE[0]) : 0, // Float
        boil_time: recipe.BOIL_TIME ? parseInt(recipe.BOIL_TIME[0]) : 0, // Integer
        efficiency: recipe.EFFICIENCY ? parseFloat(recipe.EFFICIENCY[0]) : 0, // Float
        notes: recipe.NOTES ? recipe.NOTES[0] : '', // String
        taste_notes: recipe.TASTE_NOTES ? recipe.TASTE_NOTES[0] : '', // String
        taste_rating: recipe.TASTE_RATING ? parseFloat(recipe.TASTE_RATING[0]) : 0, // Integer
        og: recipe.OG ? parseFloat(recipe.OG[0]) : 0, // Float
        fg: recipe.FG ? parseFloat(recipe.FG[0]) : 0, // Float
        fermentation_stages: recipe.FERMENTATION_STAGES ? parseInt(recipe.FERMENTATION_STAGES[0]) : 0, // Integer
        primary_age: recipe.PRIMARY_AGE ? parseInt(recipe.PRIMARY_AGE[0]) : 0, // Integer
        primary_temp: recipe.PRIMARY_TEMP ? parseFloat(recipe.PRIMARY_TEMP[0]) : 0, // Float
        secondary_age: recipe.SECONDARY_AGE ? parseInt(recipe.SECONDARY_AGE[0]) : 0, // Integer
        secondary_temp: recipe.SECONDARY_TEMP ? parseFloat(recipe.SECONDARY_TEMP[0]) : 0, // Float
        tertiary_age: recipe.TERTIARY_AGE ? parseInt(recipe.TERTIARY_AGE[0]) : 0, // Integer
        age: recipe.AGE ? parseInt(recipe.AGE[0]) : 0, // Integer
        age_temp: recipe.AGE_TEMP ? parseFloat(recipe.AGE_TEMP[0]) : 0, // Float
        carbonation_used: recipe.CARBONATION_USED ? recipe.CARBONATION_USED[0] : '', // String
        //carbonation_date: recipe.CARBONATION_DATE ? recipe.CARBONATION_DATE[0] : '', // String
        est_og: recipe.EST_OG ? parseFloat(recipe.EST_OG[0]) : 0, // Float
        est_fg: recipe.EST_FG ? parseFloat(recipe.EST_FG[0]) : 0, // Float
        est_color: recipe.EST_COLOR ? parseFloat(recipe.EST_COLOR[0]) : 0, // Float
        ibu: recipe.IBU ? parseFloat(recipe.IBU[0]) : 0, // Float
        ibu_method: recipe.IBU_METHOD ? recipe.IBU_METHOD[0] : '', // String
        est_abv: recipe.EST_ABV ? parseFloat(recipe.EST_ABV[0]) : 0, // Float
        abv: recipe.ABV ? parseFloat(recipe.ABV[0]) : 0, // Float
        actual_efficiency: recipe.ACTUAL_EFFICIENCY ? parseFloat(recipe.ACTUAL_EFFICIENCY[0]) : 0, // Float
        calories: recipe.CALORIES ? parseFloat(recipe.CALORIES[0]) : 0, // Float
        display_batch_size: recipe.DISPLAY_BATCH_SIZE ? recipe.DISPLAY_BATCH_SIZE[0] : '', // String
        display_boil_size: recipe.DISPLAY_BOIL_SIZE ? recipe.DISPLAY_BOIL_SIZE[0] : '', // String
        display_og: recipe.DISPLAY_OG ? recipe.DISPLAY_OG[0] : '', // String
        display_fg: recipe.DISPLAY_FG ? recipe.DISPLAY_FG[0] : '', // String
        display_primary_temp: recipe.DISPLAY_PRIMARY_TEMP ? recipe.DISPLAY_PRIMARY_TEMP[0] : '', // String
        display_secondary_temp: recipe.DISPLAY_SECONDARY_TEMP ? recipe.DISPLAY_SECONDARY_TEMP[0] : '', // String
        display_tertiary_temp: recipe.DISPLAY_TERTIARY_TEMP ? recipe.DISPLAY_TERTIARY_TEMP[0] : '', // String
        display_age_temp: recipe.DISPLAY_AGE_TEMP ? recipe.DISPLAY_AGE_TEMP[0] : '', // String


        // Hops
        hops: recipe.HOPS && Array.isArray(recipe.HOPS[0].HOP) ? recipe.HOPS[0].HOP.map((hop) => ({
          //version: hop.VERSION ? parseInt(hop.VERSION[0]) : 0, // Integer (Not used in either schema)

          // MasterHopBase:
          name: hop.NAME ? hop.NAME[0] : '', // String (MasterHopBase)
          origin: hop.ORIGIN ? hop.ORIGIN[0] : '', // String (MasterHopBase)
          alpha: hop.ALPHA ? parseFloat(hop.ALPHA[0]) : 0, // Float (MasterHopBase)
          type: hop.TYPE ? hop.TYPE[0] : '', // String (MasterHopBase)
          form: hop.FORM ? hop.FORM[0] : '', // String (MasterHopBase)
          beta: hop.BETA ? parseFloat(hop.BETA[0]) : 0, // Float (MasterHopBase)
          hsi: hop.HSI ? parseFloat(hop.HSI[0]) : 0, // Float (MasterHopBase)

          // RecipeHopBase:
          amount: hop.AMOUNT ? parseFloat(hop.AMOUNT[0]) : 0, // Float (RecipeHopBase)
          use: hop.USE ? hop.USE[0] : '', // String (RecipeHopBase)
          time: hop.TIME ? parseInt(hop.TIME[0]) : 0, // Integer (RecipeHopBase)
          notes: hop.NOTES ? hop.NOTES[0] : '', // String (RecipeHopBase)
          display_amount: hop.DISPLAY_AMOUNT ? hop.DISPLAY_AMOUNT[0] : '', // String (RecipeHopBase)
          inventory: hop.INVENTORY ? parseFloat(hop.INVENTORY[0]) : 0, // Float (RecipeHopBase)
          display_time: hop.DISPLAY_TIME ? hop.DISPLAY_TIME[0] : '', // String (RecipeHopBase)
        })) : [],

        // Fermentables
        fermentables: recipe.FERMENTABLES && Array.isArray(recipe.FERMENTABLES[0].FERMENTABLE) ? recipe.FERMENTABLES[0].FERMENTABLE.map((fermentable) => ({
          name: fermentable.NAME ? fermentable.NAME[0] : '', // String
          // version: fermentable.VERSION ? parseInt(fermentable.VERSION[0]) : 0, // Integer - Not used
          type: fermentable.TYPE ? fermentable.TYPE[0] : '', // String
          amount: fermentable.AMOUNT ? parseFloat(fermentable.AMOUNT[0]) : 0, // Float

          yield_: fermentable.YIELD ? parseFloat(fermentable.YIELD[0]) : 0, // Float
          color: fermentable.COLOR ? parseInt(fermentable.COLOR[0]) : 0, // Float
          // add_after_boil: fermentable.ADD_AFTER_BOIL ? fermentable.ADD_AFTER_BOIL[0] : '', // Boolean - Not used
          origin: fermentable.ORIGIN ? fermentable.ORIGIN[0] : '', // String
          supplier: fermentable.SUPPLIER ? fermentable.SUPPLIER[0] : '', // String
          notes: fermentable.NOTES ? fermentable.NOTES[0] : '', // String
          // coarse_fine_diff: fermentable.COARSE_FINE_DIFF ? parseFloat(fermentable.COARSE_FINE_DIFF[0]) : 0, // Float - Not used
          // moisture: fermentable.MOISTURE ? parseFloat(fermentable.MOISTURE[0]) : 0, // Float - Not used
          // diastatic_power: fermentable.DIASTATIC_POWER ? parseFloat(fermentable.DIASTATIC_POWER[0]) : 0, // Float - Not used
          // protein: fermentable.PROTEIN ? parseFloat(fermentable.PROTEIN[0]) : 0, // Float - Not used
          // max_in_batch: fermentable.MAX_IN_BATCH ? parseFloat(fermentable.MAX_IN_BATCH[0]) : 0, // Float - Not used
          // recommend_mash: fermentable.RECOMMEND_MASH ? fermentable.RECOMMEND_MASH[0] : '', // Boolean - Not used
          // ibu_gal_per_lb: fermentable.IBU_GAL_PER_LB ? parseFloat(fermentable.IBU_GAL_PER_LB[0]) : 0, // Float - Not used
          // display_amount: fermentable.DISPLAY_AMOUNT ? fermentable.DISPLAY_AMOUNT[0] : '', // String - Not used
          // inventory: fermentable.INVENTORY ? parseFloat(fermentable.INVENTORY[0]) : 0, // Float - Not used
          potential: fermentable.POTENTIAL ? parseInt(fermentable.POTENTIAL[0]) : 0, // Integer
          // display_color: fermentable.DISPLAY_COLOR ? fermentable.DISPLAY_COLOR[0] : '', // String - Not used
          cost_per_unit: fermentable.COST_PER_UNIT ? parseFloat(fermentable.COST_PER_UNIT[0]) : 0, // Float
          manufacturing_date: fermentable.MANUFACTURING_DATE ? parseDate(fermentable.MANUFACTURING_DATE[0]) : null, // Date
          expiry_date: fermentable.EXPIRY_DATE ? parseDate(fermentable.EXPIRY_DATE[0]) : null, // Date
          lot_number: fermentable.LOT_NUMBER ? fermentable.LOT_NUMBER[0] : '', // String
          exclude_from_total: fermentable.EXCLUDE_FROM_TOTAL ? fermentable.EXCLUDE_FROM_TOTAL[0] : 'False', // Boolean
          not_fermentable: fermentable.NOT_FERMENTABLE ? fermentable.NOT_FERMENTABLE[0] : 'False', // Boolean
          description: fermentable.DESCRIPTION ? fermentable.DESCRIPTION[0] : '', // String
          substitutes: fermentable.SUBSTITUTES ? fermentable.SUBSTITUTES[0] : '', // String
          used_in: fermentable.USED_IN ? fermentable.USED_IN[0] : '', // String
          recipe_id: fermentable.RECIPE_ID ? parseInt(fermentable.RECIPE_ID[0]) : 0, // Integer
          inventory_id: fermentable.INVENTORY_ID ? parseInt(fermentable.INVENTORY_ID[0]) : 0, // Integer
          batch_id: fermentable.BATCH_ID ? parseInt(fermentable.BATCH_ID[0]) : 0, // Integer
        })) : [],



        // Yeasts
        yeasts: recipe.YEASTS && Array.isArray(recipe.YEASTS) ? recipe.YEASTS.map((yeast) => ({
          name: yeast.NAME ? yeast.NAME[0] : '', // String
          version: yeast.VERSION ? parseInt(yeast.VERSION[0]) : 0, // Integer
          type: yeast.TYPE ? yeast.TYPE[0] : '', // String
          form: yeast.FORM ? yeast.FORM[0] : '', // String
          amount: yeast.AMOUNT ? parseFloat(yeast.AMOUNT[0]) : 0, // Float
          amount_is_weight: yeast.AMOUNT_IS_WEIGHT ? yeast.AMOUNT_IS_WEIGHT[0] : 'False', // Boolean
          laboratory: yeast.LABORATORY ? yeast.LABORATORY[0] : '', // String
          product_id: yeast.PRODUCT_ID ? yeast.PRODUCT_ID[0] : '', // String
          min_temperature: yeast.MIN_TEMPERATURE ? parseFloat(yeast.MIN_TEMPERATURE[0]) : 0, // Float
          max_temperature: yeast.MAX_TEMPERATURE ? parseFloat(yeast.MAX_TEMPERATURE[0]) : 0, // Float
          flocculation: yeast.FLOCCULATION ? yeast.FLOCCULATION[0] : '', // String
          attenuation: yeast.ATTENUATION ? parseFloat(yeast.ATTENUATION[0]) : 0, // Float
          notes: yeast.NOTES ? yeast.NOTES[0] : '', // String
          best_for: yeast.BEST_FOR ? yeast.BEST_FOR[0] : '', // String
          times_cultured: yeast.TIMES_CULTURED ? parseInt(yeast.TIMES_CULTURED[0]) : 0, // Integer
          max_reuse: yeast.MAX_REUSE ? parseInt(yeast.MAX_REUSE[0]) : 0, // Integer
          add_to_secondary: yeast.ADD_TO_SECONDARY ? yeast.ADD_TO_SECONDARY[0] : 'False', // Boolean
          display_amount: yeast.DISPLAY_AMOUNT ? yeast.DISPLAY_AMOUNT[0] : '', // String
          display_min_temp: yeast.DISP_MIN_TEMP ? yeast.DISP_MIN_TEMP[0] : '', // String
          display_max_temp: yeast.DISP_MAX_TEMP ? yeast.DISP_MAX_TEMP[0] : '', // String
          inventory: yeast.INVENTORY ? parseFloat(yeast.INVENTORY[0]) : 0, // Float
          culture_date: yeast.CULTURE_DATE ? parseDate(yeast.CULTURE_DATE[0]) : null, // Date
        })) : [],

        // Miscs
        miscs: recipe.MISCS && Array.isArray(recipe.MISCS) ? recipe.MISCS.map((misc) => ({
          name: misc.NAME ? misc.NAME[0] : '', // String
          version: misc.VERSION ? parseInt(misc.VERSION[0]) : 0, // Integer
          type: misc.TYPE ? misc.TYPE[0] : '', // String
          use: misc.USE ? misc.USE[0] : '', // String
          time: misc.TIME ? parseInt(misc.TIME[0]) : 0, // Integer
          amount: misc.AMOUNT ? parseFloat(misc.AMOUNT[0]) : 0, // Float
          amount_is_weight: misc.AMOUNT_IS_WEIGHT ? misc.AMOUNT_IS_WEIGHT[0] : 'False', // Boolean
          use_for: misc.USE_FOR ? misc.USE_FOR[0] : '', // String
          notes: misc.NOTES ? misc.NOTES[0] : '', // String
          display_amount: misc.DISPLAY_AMOUNT ? misc.DISPLAY_AMOUNT[0] : '', // String
          inventory: misc.INVENTORY ? parseFloat(misc.INVENTORY[0]) : 0, // Float
          display_time: misc.DISPLAY_TIME ? misc.DISPLAY_TIME[0] : '', // String
          batch_size: misc.BATCH_SIZE ? parseFloat(misc.BATCH_SIZE[0]) : 0, // Float
        })) : [],

        // Waters
        waters: recipe.WATERS && Array.isArray(recipe.WATERS) ? recipe.WATERS.map((water) => ({
          name: water.NAME ? water.NAME[0] : '', // String
          version: water.VERSION ? parseInt(water.VERSION[0]) : 0, // Integer
          amount: water.AMOUNT ? parseFloat(water.AMOUNT[0]) : 0, // Float
          calcium: water.CALCIUM ? parseFloat(water.CALCIUM[0]) : 0, // Float
          bicarbonate: water.BICARBONATE ? parseFloat(water.BICARBONATE[0]) : 0, // Float
          sulfate: water.SULFATE ? parseFloat(water.SULFATE[0]) : 0, // Float
          chloride: water.CHLORIDE ? parseFloat(water.CHLORIDE[0]) : 0, // Float
          sodium: water.SODIUM ? parseFloat(water.SODIUM[0]) : 0, // Float
          magnesium: water.MAGNESIUM ? parseFloat(water.MAGNESIUM[0]) : 0, // Float
          ph: water.PH ? parseFloat(water.PH[0]) : 0, // Float
          notes: water.NOTES ? water.NOTES[0] : '', // String
          display_amount: water.DISPLAY_AMOUNT ? water.DISPLAY_AMOUNT[0] : '', // String
        })) : [],

        // Mash
        mash: recipe.MASH && Array.isArray(recipe.MASH) ? recipe.MASH.map((mash) => ({
          name: mash.NAME ? mash.NAME[0] : '', // String
          version: mash.VERSION ? parseInt(mash.VERSION[0]) : 0, // Integer
          grain_temp: mash.GRAIN_TEMP ? parseFloat(mash.GRAIN_TEMP[0]) : 0, // Float
          tun_temp: mash.TUN_TEMP ? parseFloat(mash.TUN_TEMP[0]) : 0, // Float
          sparge_temp: mash.SPARGE_TEMP ? parseFloat(mash.SPARGE_TEMP[0]) : 0, // Float
          ph: mash.PH ? parseFloat(mash.PH[0]) : 0, // Float
          notes: mash.NOTES ? mash.NOTES[0] : '', // String
          tun_weight: mash.TUN_WEIGHT ? parseFloat(mash.TUN_WEIGHT[0]) : 0, // Float
          tun_specific_heat: mash.TUN_SPECIFIC_HEAT ? parseFloat(mash.TUN_SPECIFIC_HEAT[0]) : 0, // Float
          equip_adjust: mash.EQUIP_ADJUST ? mash.EQUIP_ADJUST[0] : '', // String
          display_grain_temp: mash.DISPLAY_GRAIN_TEMP ? mash.DISPLAY_GRAIN_TEMP[0] : '', // String
          display_tun_temp: mash.DISPLAY_TUN_TEMP ? mash.DISPLAY_TUN_TEMP[0] : '', // String
          display_sparge_temp: mash.DISPLAY_SPARGE_TEMP ? mash.DISPLAY_SPARGE_TEMP[0] : '', // String
        })) : [],

        // Fermentation
        fermentations: recipe.FERMENTATION && Array.isArray(recipe.FERMENTATION) ? recipe.FERMENTATION.map((fermentation) => ({
          name: fermentation.NAME ? fermentation.NAME[0] : '', // String
          version: fermentation.VERSION ? parseInt(fermentation.VERSION[0]) : 0, // Integer
          temp: fermentation.TEMP ? parseFloat(fermentation.TEMP[0]) : 0, // Float
          time: fermentation.TIME ? parseInt(fermentation.TIME[0]) : 0, // Integer
          notes: fermentation.NOTES ? fermentation.NOTES[0] : '', // String
          display_temp: fermentation.DISPLAY_TEMP ? fermentation.DISPLAY_TEMP[0] : '', // Strinq
        })) : [],


        // Style
        style: recipe.STYLE ? {
          name: recipe.STYLE[0].NAME ? recipe.STYLE[0].NAME[0] : '', // String
          version: recipe.STYLE[0].VERSION ? parseInt(recipe.STYLE[0].VERSION[0]) : 0, // Integer
          category: recipe.STYLE[0].CATEGORY ? recipe.STYLE[0].CATEGORY[0] : '', // String
          category_number: recipe.STYLE[0].CATEGORY_NUMBER ? parseInt(recipe.STYLE[0].CATEGORY_NUMBER[0]) : 0, // Integer
          style_letter: recipe.STYLE[0].STYLE_LETTER ? recipe.STYLE[0].STYLE_LETTER[0] : '', // String
          style_guide: recipe.STYLE[0].STYLE_GUIDE ? recipe.STYLE[0].STYLE_GUIDE[0] : '', // String
          type: recipe.STYLE[0].TYPE ? recipe.STYLE[0].TYPE[0] : '', // String
          og_min: recipe.STYLE[0].OG_MIN ? recipe.STYLE[0].OG_MIN[0] : '', // String
          og_max: recipe.STYLE[0].OG_MAX ? recipe.STYLE[0].OG_MAX[0] : '', // String
          fg_min: recipe.STYLE[0].FG_MIN ? recipe.STYLE[0].FG_MIN[0] : '', // String
          fg_max: recipe.STYLE[0].FG_MAX ? recipe.STYLE[0].FG_MAX[0] : '', // String
          ibu_min: recipe.STYLE[0].IBU_MIN ? recipe.STYLE[0].IBU_MIN[0] : '', // String
          ibu_max: recipe.STYLE[0].IBU_MAX ? recipe.STYLE[0].IBU_MAX[0] : '', // String
          color_min: recipe.STYLE[0].COLOR_MIN ? recipe.STYLE[0].COLOR_MIN[0] : '', // String
          color_max: recipe.STYLE[0].COLOR_MAX ? recipe.STYLE[0].COLOR_MAX[0] : '', // String
          carb_min: recipe.STYLE[0].CARB_MIN ? recipe.STYLE[0].CARB_MIN[0] : '', // String
          carb_max: recipe.STYLE[0].CARB_MAX ? recipe.STYLE[0].CARB_MAX[0] : '', // String
          abv_max: recipe.STYLE[0].ABV_MAX ? recipe.STYLE[0].ABV_MAX[0] : '', // String
          abv_min: recipe.STYLE[0].ABV_MIN ? recipe.STYLE[0].ABV_MIN[0] : '', // String
          notes: recipe.STYLE[0].NOTES ? recipe.STYLE[0].NOTES[0] : '', // String
          profile: recipe.STYLE[0].PROFILE ? recipe.STYLE[0].PROFILE[0] : '', // String
          ingredients: recipe.STYLE[0].INGREDIENTS ? recipe.STYLE[0].INGREDIENTS[0] : '', // String
          examples: recipe.STYLE[0].EXAMPLES ? recipe.STYLE[0].EXAMPLES[0] : '', // String
          display_og_min: recipe.STYLE[0].DISPLAY_OG_MIN ? recipe.STYLE[0].DISPLAY_OG_MIN[0] : '', // String
          display_og_max: recipe.STYLE[0].DISPLAY_OG_MAX ? recipe.STYLE[0].DISPLAY_OG_MAX[0] : '', // String
          display_fg_min: recipe.STYLE[0].DISPLAY_FG_MIN ? recipe.STYLE[0].DISPLAY_FG_MIN[0] : '', // String
          display_fg_max: recipe.STYLE[0].DISPLAY_FG_MAX ? recipe.STYLE[0].DISPLAY_FG_MAX[0] : '', // String
          display_color_min: recipe.STYLE[0].DISPLAY_COLOR_MIN ? recipe.STYLE[0].DISPLAY_COLOR_MIN[0] : '', // String
          display_color_max: recipe.STYLE[0].DISPLAY_COLOR_MAX ? recipe.STYLE[0].DISPLAY_COLOR_MAX[0] : '', // String
          og_range: recipe.STYLE[0].OG_RANGE ? recipe.STYLE[0].OG_RANGE[0] : '', // String
          fg_range: recipe.STYLE[0].FG_RANGE ? recipe.STYLE[0].FG_RANGE[0] : '', // String
          ibu_range: recipe.STYLE[0].IBU_RANGE ? recipe.STYLE[0].IBU_RANGE[0] : '', // String
          carb_range: recipe.STYLE[0].CARB_RANGE ? recipe.STYLE[0].CARB_RANGE[0] : '', // String
          color_range: recipe.STYLE[0].COLOR_RANGE ? recipe.STYLE[0].COLOR_RANGE[0] : '', // String
          abv_range: recipe.STYLE[0].ABV_RANGE ? recipe.STYLE[0].ABV_RANGE[0] : '', // String
        } : null,
        // Continue mapping other fields similarly...
      };
    });

    // Debug: Log the final mapped recipes
    console.log('Imported Recipes:', importedRecipes.value);
  });
}
async function importRecipes() {
  for (const recipe of importedRecipes.value) {
    try {
      // Log the request details before making the request
      console.log('Request:', {
        url: 'http://localhost:8000/recipes',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(recipe),
      });

      const response = await fetch('http://localhost:8000/recipes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(recipe),
      });

      if (!response.ok) {
        throw new Error('Failed to create recipe');
      }
      // close the dialog
      open.value = false;
      window.location.reload(); // refresh the parent page

      console.log(`Recipe "${recipe.name}" imported successfully.`);
      console.log('recipe:', recipe);
    } catch (error) {
      console.error(error);
    }
  }
}

</script>

<template>
  <AlertDialog :open="open">
    <AlertDialogTrigger>
      <button @click="open = true">Import Recipes</button>
    </AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Import Recipes from BeerXML</AlertDialogTitle>
        <input type="file" @change="handleFileChange" accept=".xml" />
        <div v-if="importedRecipes.length > 0">
          <h2>Imported Recipes:</h2>
          <ul>
            <li v-for="recipe in importedRecipes" :key="recipe.id">
              {{ recipe.name }}
            </li>
          </ul>
        </div>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
        <AlertDialogAction @click="importRecipes">Import</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
