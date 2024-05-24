<template>
    <i :class="iconClass" :style="{ fontSize: size + 'px' }"></i>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
    name: {
        type: String,
        required: true,
    },
    size: {
        type: Number,
        default: 24,
    },
});

const iconClass = computed(() => `mdi ${props.name}`);
</script>

<style scoped>
/* You can customize the icon styles here */
.mdi {
    font-family: 'Material Design Icons';
    font-weight: normal;
    font-style: normal;
    display: inline-block;
    text-decoration: inherit;
    text-transform: none;
    letter-spacing: normal;
    word-wrap: normal;
    white-space: nowrap;
    direction: ltr;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
</style>
