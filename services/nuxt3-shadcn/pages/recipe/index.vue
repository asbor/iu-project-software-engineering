<template>
  <div>
    <header class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-2xl font-semibold">Recipes</h1>
      </div>
      <div>
        <div class="flex gap-4">
          <Button asChild>
            <NuxtLink href="/recipe/recipeCardWindow">Show cards</NuxtLink>
          </Button>
          <Button asChild>
            <NuxtLink href="/recipe/newRecipe">New recipe</NuxtLink>
          </Button>
          <Button asChild>
            <BeerXMLImportRecipeDialog />
          </Button>
        </div>
      </div>
    </header>
    <div v-if="loading" class="text-center">Loading...</div>
    <div v-else>
      <div style="width: 1600px; height: 800px;">
        <Table style="height: 100%; width: 100%;">
          <TableCaption>A list of your recipes.</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead>id</TableHead>
              <TableHead>name</TableHead>
              <TableHead>type</TableHead>
              <TableHead>brewer</TableHead>
              <TableHead>asst_brewer</TableHead>
              <TableHead>batch_size</TableHead>
              <TableHead>boil_size</TableHead>
              <TableHead>boil_time</TableHead>
              <TableHead>efficiency</TableHead>
              <TableHead>mash</TableHead>
              <TableHead>notes</TableHead>
              <TableHead>taste_notes</TableHead>
              <TableHead>taste_rating</TableHead>
              <TableHead>og</TableHead>
              <TableHead>fg</TableHead>
              <TableHead>carbonation</TableHead>
              <TableHead>fermentation_stages</TableHead>
              <TableHead>primary_age</TableHead>
              <TableHead>primary_temp</TableHead>
              <TableHead>secondary_age</TableHead>
              <TableHead>secondary_temp</TableHead>
              <TableHead>tertiary_age</TableHead>
              <TableHead>age</TableHead>
              <TableHead>age_temp</TableHead>
              <TableHead>carbonation_used</TableHead>
              <TableHead>date</TableHead>
              <TableHead>est_og</TableHead>
              <TableHead>est_fg</TableHead>
              <TableHead>est_color</TableHead>
              <TableHead>ibu</TableHead>
              <TableHead>ibu_method</TableHead>
              <TableHead>est_abv</TableHead>
              <TableHead>abv</TableHead>
              <TableHead>actual_efficiency</TableHead>
              <TableHead>calories</TableHead>
              <TableHead>display_batch_size</TableHead>
              <TableHead>display_boil_size</TableHead>
              <TableHead>display_og</TableHead>
              <TableHead>display_fg</TableHead>
              <TableHead>display_primary_temp</TableHead>
              <TableHead>display_secondary_temp</TableHead>
              <TableHead>display_tertiary_temp</TableHead>
              <TableHead>display_age_temp</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <!-- Loop through recipes and display each recipe -->
            <template v-for="recipe in recipes" :key="recipe.id">
              <TableRow>
                <TableCell>{{ recipe.id }}</TableCell>
                <TableCell>{{ recipe.name }}</TableCell>
                <TableCell>{{ recipe.type }}</TableCell>
                <TableCell>{{ recipe.brewer }}</TableCell>
                <TableCell>{{ recipe.asst_brewer }}</TableCell>
                <TableCell>{{ recipe.batch_size }}</TableCell>
                <TableCell>{{ recipe.boil_size }}</TableCell>
                <TableCell>{{ recipe.boil_time }}</TableCell>
                <TableCell>{{ recipe.efficiency }}</TableCell>
                <TableCell>{{ recipe.mash }}</TableCell>
                <TableCell>{{ recipe.notes }}</TableCell>
                <TableCell>{{ recipe.taste_notes }}</TableCell>
                <TableCell>{{ recipe.taste_rating }}</TableCell>
                <TableCell>{{ recipe.og }}</TableCell>
                <TableCell>{{ recipe.fg }}</TableCell>
                <TableCell>{{ recipe.carbonation }}</TableCell>
                <TableCell>{{ recipe.fermentation_stages }}</TableCell>
                <TableCell>{{ recipe.primary_age }}</TableCell>
                <TableCell>{{ recipe.primary_temp }}</TableCell>
                <TableCell>{{ recipe.secondary_age }}</TableCell>
                <TableCell>{{ recipe.secondary_temp }}</TableCell>
                <TableCell>{{ recipe.tertiary_age }}</TableCell>
                <TableCell>{{ recipe.age }}</TableCell>
                <TableCell>{{ recipe.age_temp }}</TableCell>
                <TableCell>{{ recipe.carbonation_used }}</TableCell>
                <TableCell>{{ recipe.carbonation_date }}</TableCell>
                <TableCell>{{ recipe.est_og }}</TableCell>
                <TableCell>{{ recipe.est_fg }}</TableCell>
                <TableCell>{{ recipe.est_color }}</TableCell>
                <TableCell>{{ recipe.ibu }}</TableCell>
                <TableCell>{{ recipe.ibu_method }}</TableCell>
                <TableCell>{{ recipe.est_abv }}</TableCell>
                <TableCell>{{ recipe.abv }}</TableCell>
                <TableCell>{{ recipe.actual_efficiency }}</TableCell>
                <TableCell>{{ recipe.calories }}</TableCell>
                <TableCell>{{ recipe.display_batch_size }}</TableCell>
                <TableCell>{{ recipe.display_boil_size }}</TableCell>
                <TableCell>{{ recipe.display_og }}</TableCell>
                <TableCell>{{ recipe.display_fg }}</TableCell>
                <TableCell>{{ recipe.display_primary_temp }}</TableCell>
                <TableCell>{{ recipe.display_secondary_temp }}</TableCell>
                <TableCell>{{ recipe.display_tertiary_temp }}</TableCell>
                <TableCell>{{ recipe.display_age_temp }}</TableCell>
                <TableCell class="text-right">
                  <!-- Add buttons for actions like edit or delete -->
                  <Button asChild class="mr-2">
                    <NuxtLink :href="`/recipe/${recipe.id}`">Edit</NuxtLink>
                  </Button>

                  <!-- Delete button -->
                  <Button @click="deleteRecipe(recipe.id)">Delete</Button>
                </TableCell>
              </TableRow>
            </template>
          </TableBody>
        </Table>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { ref, onMounted } from 'vue';

// Define interface for recipe 
interface Recipe {
  id: string;
  name: string;
  type: string;
  brewer: string;
  asst_brewer: string;
  batch_size: number;
  boil_size: number;
  boil_time: number;
  efficiency: number;
  mash: string;
  notes: string;
  taste_notes: string;
  taste_rating: number;
  og: number;
  fg: number;
  carbonation: string;
  fermentation_stages: number;
  primary_age: number;
  primary_temp: number;
  secondary_age: number;
  secondary_temp: number;
  tertiary_age: number;
  age: number;
  age_temp: number;
  carbonation_used: string;
  carbonation_date: string;
  est_og: number;
  est_fg: number;
  est_color: number;
  ibu: number;
  ibu_method: string;
  est_abv: number;
  abv: number;
  actual_efficiency: number;
  calories: number;
  display_batch_size: string;
  display_boil_size: string;
  display_og: string;
  display_fg: string;
  display_primary_temp: string;
  display_secondary_temp: string;
  display_tertiary_temp: string;
  display_age_temp: string;

}

const recipes = ref<Recipe[]>([]);
const selectedRecipe = ref<Recipe | null>(null);
const loading = ref(false);

async function fetchRecipes() {
  try {
    loading.value = true;
    const response = await fetch('http://localhost:8000/recipe', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error('Failed to fetch recipes');
    }
    const data = await response.json();
    recipes.value = data;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
}

function deleteRecipe(id: string) {
  if (!confirm('Are you sure you want to delete this recipe?')) {
    return;
  }

  // Delete the recipe
  fetch(`http://localhost:8000/recipe/${id}`, {
    method: 'DELETE',
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete recipe');
      }
      // Remove the deleted recipe from the list
      recipes.value = recipes.value.filter((recipe) => recipe.id !== id);
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(fetchRecipes);
</script>
