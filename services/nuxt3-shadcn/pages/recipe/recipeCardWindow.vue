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

async function fetchRecipes() {
    try {
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

<template>
    <div class="grid w-full gap-4">
        <header class="flex items-start justify-between">
            <div class="grow">
                <h1>Recipe</h1>
            </div>
            <ProductNewDialog />
            <BeerXMLImportRecipeDialog />
        </header>
        <main class="grid w-full gap-4">
            <div>
                <input type="text" placeholder="Search for recipe"
                    class="w-full p-2 border border-neutral-200 rounded bg-neutral-200" />
            </div>
            <div class="grid gap-4 lg:grid-cols-4">
                <BeerCard v-for='( recipe, index ) in recipes' :card="recipe" :key='index' />
            </div>
        </main>
        <footer>

        </footer>
    </div>
</template>