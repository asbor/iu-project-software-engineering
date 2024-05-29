<template>
    <div class="border-2 p-4">
        <div>
            <h2 class="text-xl font-semibold">Batch Recipe</h2>
            <p><strong>Recipe Name:</strong> {{ batch.recipe?.name }}</p>
            <p><strong>Type:</strong> {{ batch.recipe?.type }}</p>
            <p><strong>ABV:</strong> {{ batch.recipe?.abv }}</p>
            <p><strong>OG:</strong> {{ batch.recipe?.og }}</p>
            <p><strong>FG:</strong> {{ batch.recipe?.fg }}</p>
            <p><strong>IBU:</strong> {{ batch.recipe?.ibu }}</p>
            <NuxtLink :to="{ name: 'recipes-id', params: { id: batch.recipe?.id } }">
                View Recipe Details
            </NuxtLink>
        </div>
    </div>
</template>

<script>
export default {
    props: ['batch']
};
</script>