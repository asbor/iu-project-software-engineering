<script setup lang="ts">
import { ref } from 'vue';

const { loading, open } = useHelpers();

async function triggerBackendScript() {
    try {
        const response = await fetch('http://localhost:8000/refresh-beer-styles', {
            method: 'POST',
        });
        const result = await response.json();
        console.log(result.message);
    } catch (error) {
        console.error('Error triggering backend script:', error);
    }
}
</script>

<template>
    <button @click="triggerBackendScript">Trigger Script</button>
</template>
