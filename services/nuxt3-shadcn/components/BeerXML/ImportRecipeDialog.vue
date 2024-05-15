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

function getValueOrDefault(field) {
  return field ? field[0] : '';
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

    // Map each recipe to the format expected by importedRecipes
    importedRecipes.value = recipes.map((recipe) => ({
      id: uuidv4(), // Generate UUID for each recipe
      name: recipe.NAME[0],
      type: getValueOrDefault(recipe.TYPE),
      version: parseFloat(getValueOrDefault(recipe.VERSION)),
      brewer: getValueOrDefault(recipe.BREWER),
      asst_brewer: getValueOrDefault(recipe.ASST_BREWER),
      batch_size: parseFloat(getValueOrDefault(recipe.BATCH_SIZE)),
      boil_size: parseFloat(getValueOrDefault(recipe.BOIL_SIZE)),
      boil_time: parseInt(getValueOrDefault(recipe.BOIL_TIME)),
      efficiency: parseFloat(getValueOrDefault(recipe.EFFICIENCY)),
      //mash: getValueOrDefault(recipe.MASH),
      notes: getValueOrDefault(recipe.NOTES),
      taste_notes: getValueOrDefault(recipe.TASTE_NOTES),
      taste_rating: parseFloat(getValueOrDefault(recipe.TASTE_RATING)),
      og: parseFloat(getValueOrDefault(recipe.OG)),
      fg: parseFloat(getValueOrDefault(recipe.FG)),
      fermentation_stages: parseInt(getValueOrDefault(recipe.FERMENTATION_STAGES)),
      primary_age: parseInt(getValueOrDefault(recipe.PRIMARY_AGE)),
      primary_temp: parseFloat(getValueOrDefault(recipe.PRIMARY_TEMP)),
      secondary_age: parseInt(getValueOrDefault(recipe.SECONDARY_AGE)),
      secondary_temp: parseFloat(getValueOrDefault(recipe.SECONDARY_TEMP)),
      tertiary_age: parseInt(getValueOrDefault(recipe.TERTIARY_AGE)),
      age: parseInt(getValueOrDefault(recipe.AGE)),
      age_temp: parseFloat(getValueOrDefault(recipe.AGE_TEMP)),
      carbonation_used: getValueOrDefault(recipe.CARBONATION_USED),
      //carbonation_date: getValueOrDefault(recipe.DATE),
      est_og: parseFloat(getValueOrDefault(recipe.EST_OG)),
      est_fg: parseFloat(getValueOrDefault(recipe.EST_FG)),
      est_color: parseFloat(getValueOrDefault(recipe.EST_COLOR)),
      ibu: parseFloat(getValueOrDefault(recipe.IBU)),
      ibu_method: getValueOrDefault(recipe.IBU_METHOD),
      est_abv: parseFloat(getValueOrDefault(recipe.EST_ABV)),
      abv: parseFloat(getValueOrDefault(recipe.ABV)),
      actual_efficiency: parseFloat(getValueOrDefault(recipe.ACTUAL_EFFICIENCY)),
      calories: parseFloat(getValueOrDefault(recipe.CALORIES)),
      display_batch_size: getValueOrDefault(recipe.DISPLAY_BATCH_SIZE),
      display_boil_size: getValueOrDefault(recipe.DISPLAY_BOIL_SIZE),
      display_og: getValueOrDefault(recipe.DISPLAY_OG),
      display_fg: getValueOrDefault(recipe.DISPLAY_FG),
      display_primary_temp: getValueOrDefault(recipe.DISPLAY_PRIMARY_TEMP),
      display_secondary_temp: getValueOrDefault(recipe.DISPLAY_SECONDARY_TEMP),
      display_tertiary_temp: getValueOrDefault(recipe.DISPLAY_TERTIARY_TEMP),
      display_age_temp: getValueOrDefault(recipe.DISPLAY_AGE_TEMP),

      // Map hops if present
      hops: recipe.HOPS && recipe.HOPS[0].HOP ? recipe.HOPS[0].HOP.map((hop) => ({
        id: uuidv4(), // Generate UUID for each hop
        name: getValueOrDefault(hop.NAME),
        origin: getValueOrDefault(hop.ORIGIN),
        alpha: parseFloat(getValueOrDefault(hop.ALPHA)),
        amount: parseFloat(getValueOrDefault(hop.AMOUNT)),
        use: getValueOrDefault(hop.USE),
        time: parseInt(getValueOrDefault(hop.TIME)),
        notes: getValueOrDefault(hop.NOTES),
        type: getValueOrDefault(hop.TYPE),
        form: getValueOrDefault(hop.FORM),
        beta: parseFloat(getValueOrDefault(hop.BETA)),
        hsi: parseFloat(getValueOrDefault(hop.HSI)),
        display_amount: getValueOrDefault(hop.DISPLAY_AMOUNT),
        inventory: parseFloat(getValueOrDefault(hop.INVENTORY)),
        display_time: getValueOrDefault(hop.DISPLAY_TIME),
      })) : [],
    }));

  });
}
async function importRecipes() {
  for (const recipe of importedRecipes.value) {
    try {
      // Log the request details before making the request
      console.log('Request:', {
        url: 'http://localhost:8000/recipe',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(recipe),
      });

      const response = await fetch('http://localhost:8000/recipe', {
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
