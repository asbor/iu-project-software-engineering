<script setup>
import { ref } from 'vue';
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

    // Map each recipe to the format expected by importedRecipes
    importedRecipes.value = recipes.map((recipe) => ({
      id: uuidv4(), // Generate UUID for each recipe
      name: recipe.NAME[0],
      version: parseInt(recipe.VERSION[0]), // Convert version to integer
      type: recipe.TYPE[0],
      brewer: recipe.BREWER[0],
      asst_brewer: '', // Add asst_brewer if needed, currently empty string
      batch_size: parseInt(recipe.BATCH_SIZE[0]), // Assuming BATCH_SIZE is available in BeerXML
      boil_size: parseInt(recipe.BOIL_SIZE[0]), // Assuming BOIL_SIZE is available in BeerXML
      boil_time: parseInt(recipe.BOIL_TIME[0]), // Assuming BOIL_TIME is available in BeerXML
      efficiency: parseInt(recipe.EFFICIENCY[0]), // Assuming EFFICIENCY is available in BeerXML
      hop: '', // Add hop field if needed, currently empty string
      fermentable: '', // Add fermentable field if needed, currently empty string
      misc: '', // Add misc field if needed, currently empty string
      yeast: '', // Add yeast field if needed, currently empty string
      water: '', // Add water field if needed, currently empty string
      style: '', // Add style field if needed, currently empty string
      equipment: '', // Add equipment field if needed, currently empty string
      mash: '', // Add mash field if needed, currently empty string
      notes: '', // Add notes field if needed, currently empty string
      taste_notes: '', // Add taste_notes field if needed, currently empty string
      taste_rating: 0, // Add taste_rating field if needed, currently 0
      og: 0, // Add og field if needed, currently 0
      fg: 0, // Add fg field if needed, currently 0
      carbonation: 0, // Add carbonation field if needed, currently 0
      fermentation_stages: 0, // Add fermentation_stages field if needed, currently 0
      primary_age: 0, // Add primary_age field if needed, currently 0
      primary_temp: 0, // Add primary_temp field if needed, currently 0
      secondary_age: 0, // Add secondary_age field if needed, currently 0
      secondary_temp: 0, // Add secondary_temp field if needed, currently 0
      tertiary_age: 0, // Add tertiary_age field if needed, currently 0
      age: 0, // Add age field if needed, currently 0
      age_temp: 0, // Add age_temp field if needed, currently 0
      carbonation_used: '', // Add carbonation_used field if needed, currently empty string
      date: new Date(), // Assuming date is available in BeerXML, set to current date for now
      est_og: 0, // Add est_og field if needed, currently 0
      est_fg: 0, // Add est_fg field if needed, currently 0
      est_color: 0, // Add est_color field if needed, currently 0
      ibu: 0, // Add ibu field if needed, currently 0
      ibu_method: '', // Add ibu_method field if needed, currently empty string
      est_abv: 0, // Add est_abv field if needed, currently 0
      abv: 0, // Add abv field if needed, currently 0
      actual_efficiency: 0, // Add actual_efficiency field if needed, currently 0
      calories: 0, // Add calories field if needed, currently 0
      display_batch_size: '', // Add display_batch_size field if needed, currently empty string
      display_boil_size: '', // Add display_boil_size field if needed, currently empty string
      display_og: '', // Add display_og field if needed, currently empty string
      display_fg: '', // Add display_fg field if needed, currently empty string
      display_primary_temp: '', // Add display_primary_temp field if needed, currently empty string
      display_secondary_temp: '', // Add display_secondary_temp field if needed, currently empty string
      display_tertiary_temp: '', // Add display_tertiary_temp field if needed, currently empty string
    }));
  });
}
async function importRecipes() {
  for (const recipe of importedRecipes.value) {
    try {
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
      console.log(`Recipe "${recipe.name}" imported successfully.`);
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
