<template>
    <AlertDialog :open="open">
        <!-- Dialog content -->
    </AlertDialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps({
    equipment: Object,
    open: Boolean
});

const formData = ref({
    id: null,
    name: '',
    version: 1,
    // Add more properties as needed
});

const saveEquipment = async () => {
    // Save logic
};

// Watch for changes in equipment prop
watch(() => props.equipment, (newValue) => {
    if (newValue) {
        // Update formData with equipment data
        formData.value = { ...newValue };
    }
});
</script>