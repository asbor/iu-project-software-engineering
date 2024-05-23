<template>
    <div>
        <header class="mb-8">
            <h1 class="text-2xl font-semibold">Create New Batch</h1>
        </header>
        <form @submit.prevent="createBatch">
            <div class="mb-4">
                <label for="recipe" class="block text-sm font-medium text-gray-700">Recipe</label>
                <select id="recipe" v-model="newBatch.recipe_id" required class="mt-1 block w-full">
                    <option value="" disabled>Select a recipe</option>
                    <option v-for="recipe in recipes" :key="recipe.id" :value="recipe.id">{{ recipe.name }}</option>
                </select>
            </div>
            <div class="mb-4">
                <label for="batch_name" class="block text-sm font-medium text-gray-700">Batch Name</label>
                <input type="text" id="batch_name" v-model="newBatch.batch_name" required class="mt-1 block w-full" />
            </div>
            <div class="mb-4">
                <label for="batch_number" class="block text-sm font-medium text-gray-700">Batch Number</label>
                <input type="number" id="batch_number" v-model="newBatch.batch_number" required
                    class="mt-1 block w-full" />
            </div>
            <div class="mb-4">
                <label for="batch_size" class="block text-sm font-medium text-gray-700">Batch Size (L)</label>
                <input type="number" id="batch_size" v-model="newBatch.batch_size" required class="mt-1 block w-full" />
            </div>
            <div class="mb-4">
                <label for="brewer" class="block text-sm font-medium text-gray-700">Brewer</label>
                <input type="text" id="brewer" v-model="newBatch.brewer" required class="mt-1 block w-full" />
            </div>
            <div class="mb-4">
                <label for="brew_date" class="block text-sm font-medium text-gray-700">Brew Date</label>
                <input type="date" id="brew_date" v-model="newBatch.brew_date" required class="mt-1 block w-full" />
            </div>
            <div class="flex justify-end">
                <Button type="submit">Create Batch</Button>
            </div>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { Button } from '@/components/ui/button';

// Define interface for recipe
interface Recipe {
    id: string;
    name: string;
}

// Define interface for new batch
interface NewBatch {
    recipe_id: string;
    batch_name: string;
    batch_number: number;
    batch_size: number;
    brewer: string;
    brew_date: string;
}

const recipes = ref<Recipe[]>([]);
const newBatch = ref<NewBatch>({
    recipe_id: '',
    batch_name: '',
    batch_number: 1, // Default batch number
    batch_size: 0,
    brewer: '',
    brew_date: '',
});
const loading = ref(false);
const router = useRouter();

async function fetchRecipes() {
    try {
        loading.value = true;
        const response = await fetch('http://localhost:8000/recipes', {
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

async function createBatch() {
    try {
        const response = await fetch('http://localhost:8000/batches', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newBatch.value),
        });
        if (!response.ok) {
            throw new Error('Failed to create batch');
        }
        router.push('/batches'); // Redirect to batches list
    } catch (error) {
        console.error(error);
    }
}

onMounted(fetchRecipes);
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
