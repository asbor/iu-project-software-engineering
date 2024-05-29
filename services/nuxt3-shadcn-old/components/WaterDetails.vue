<template>
    <div class="border-2 p-4">
        <header>
            <h2 class="text-xl font-semibold">Water</h2>
        </header>
        <div>
            <label for="water">Water:</label>
            <input type="text" id="water" v-model="batch.water" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full">
        </div>
    </div>
</template>

<script>
export default {
    props: ['batch']
};
</script>