<template>
    <div class="border-2 p-4">
        <div>
            <label for="notes">Notes:</label>
            <textarea id="notes" v-model="batch.notes" required placeholder="Optional"
                class="border-2 border-gray-300 rounded-lg p-2 w-full"></textarea>
        </div>
    </div>
</template>

<script>
export default {
    props: ['batch']
};
</script>